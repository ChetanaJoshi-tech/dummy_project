# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from clinet_data.core.database import SessionLocal, engine
from clinet_data import crud, schemas
from typing import List

from clinet_data.core import models

# Create the tables in the database (if not already created)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Tables created successfully!"}        

# Create a user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, name=user.name, email=user.email)

# Get all users
@app.get("/users/", response_model=List[schemas.User])
def get_users( db: Session = Depends(get_db)):
    return crud.get_users(db=db)

# Create a post for a user
@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, title=post.title, content=post.content, user_id=post.owner_id)



# Get a user by ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_users(db=db, post_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Update a user
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, name=user.name, email=user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete a user
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

    
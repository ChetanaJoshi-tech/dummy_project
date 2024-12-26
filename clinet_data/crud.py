# crud.py
from sqlalchemy.orm import Session
from clinet_data.core.models import User, Post

# Create a new user
def create_user(db: Session, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get users with pagination
def get_users(db: Session):
    return db.query(User).all()

# Create a new post for a user
def create_post(db: Session, title: str, content: str, user_id: int):
    db_post = Post(title=title, content=content, owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post



# Update a user's details
def update_user(db: Session, user_id: int, name: str = None, email: str = None):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if name:
            db_user.name = name
        if email:
            db_user.email = email
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete a user by ID
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# --- Post CRUD Operations ---

# Get a single post by ID
def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

# Update a post's details
def update_post(db: Session, post_id: int, title: str = None, content: str = None):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        if title:
            db_post.title = title
        if content:
            db_post.content = content
        db.commit()
        db.refresh(db_post)
    return db_post

# Delete a post by ID
def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

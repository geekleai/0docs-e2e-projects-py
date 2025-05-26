from fastapi import APIRouter, HTTPException
from typing import Dict, List
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


# In-memory storage
users_db: Dict[int, User] = {
    1: User(id=1, username="john_doe", email="john@example.com"),
    2: User(id=2, username="jane_smith", email="jane@example.com"),
}


@router.get("/", response_model=List[User])
def get_users():
    """Get all users"""
    return list(users_db.values())


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    """Get a specific user by ID"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


@router.post("/", response_model=User)
def create_user(user: User):
    """Create a new user"""
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user
    return user


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: User):
    """Update a user"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user_update
    return user_update
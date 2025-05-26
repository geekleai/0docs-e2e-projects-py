from typing import Dict
from models import MsgPayload
from app.services import MsgService

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
    responses={404: {"description": "Not found"}},
)

# In-memory storage (in a real app, this would be a database)
messages_service = MsgService()


@router.get("/")
def get_all_messages() -> Dict[str, Dict[int, MsgPayload]]:
    """Get all messages"""
    return {"messages": messages_service.get_all_messages()}


@router.post("/{msg_name}/")
def add_message(msg_name: str) -> Dict[str, MsgPayload]:
    """Add a new message"""
    return {"message": messages_service.add_message(msg_name)}


@router.get("/{msg_id}")
def get_message(msg_id: int) -> Dict[str, MsgPayload]:
    """Get a specific message by ID"""
    return {"message": messages_service.get_message(msg_id)}


@router.delete("/{msg_id}")
def delete_message(msg_id: int) -> Dict[str, str]:
    """Delete a message by ID"""
    messages_service.delete_message(msg_id)
    return {"message": "Message deleted successfully"}

from app.models import MsgPayload

class MsgService:

    # In-memory storage (in a real app, this would be a database)
    messages_list: dict[int, MsgPayload] = {}


    def get_all_messages(self) -> dict[str, dict[int, MsgPayload]]:
        """Get all messages"""
        return {"messages": self.messages_list}
    
    def add_message(self, msg_name: str) -> dict[str, MsgPayload]:
        """Add a new message"""
        msg_id = max(self.messages_list.keys()) + 1 if self.messages_list else 0
        self.messages_list[msg_id] = MsgPayload(msg_id=msg_id, msg_name=msg_name)
        return {"message": self.messages_list[msg_id]}
    
    def get_message(self, msg_id: int) -> dict[str, MsgPayload]:
        """Get a specific message by ID"""
        if msg_id not in self.messages_list:
            raise ValueError("Message not found")
        return {"message": self.messages_list[msg_id]}
    
    def delete_message(self, msg_id: int) -> dict[str, str]:
        """Delete a message by ID"""
        if msg_id not in self.messages_list:
            raise ValueError("Message not found")
        del self.messages_list[msg_id]
        return {"message": "Message deleted successfully"}
    
    def update_message(self, msg_id: int, msg_name: str) -> dict[str, MsgPayload]:
        """Update a message by ID"""
        if msg_id not in self.messages_list:
            raise ValueError("Message not found")
        self.messages_list[msg_id].msg_name = msg_name
        return {"message": self.messages_list[msg_id]}
    
    def clear_messages(self) -> dict[str, str]:
        """Clear all messages"""
        self.messages_list.clear()
        return {"message": "All messages cleared successfully"}
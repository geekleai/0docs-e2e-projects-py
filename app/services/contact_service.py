from typing import Dict
from app.models.contact import Contact

class ContactService:
    def __init__(self):
        self.contacts_db: Dict[int, Contact] = {}
    
    def get_all_contacts(self) -> Dict[str, Dict[int, Contact]]:
        return {"contacts": self.contacts_db}

    def add_contact(self, contact: Contact) -> Dict[str, Contact]:
        if contact.id in self.contacts_db:
            raise ValueError("Contact already exists")
        self.contacts_db[contact.id] = contact
        return {"contact": contact}

    def get_contact(self, contact_id: int) -> Dict[str, Contact]:
        if contact_id not in self.contacts_db:
            raise ValueError("Contact not found")
        return {"contact": self.contacts_db[contact_id]}

    def update_contact(self, contact_id: int, contact: Contact) -> Dict[str, Contact]:
        if contact_id not in self.contacts_db:
            raise ValueError("Contact not found")
        self.contacts_db[contact_id] = contact
        return {"contact": contact}

    def delete_contact(self, contact_id: int) -> Dict[str, str]:
        if contact_id not in self.contacts_db:
            raise ValueError("Contact not found")
        del self.contacts_db[contact_id]
        return {"message": "Contact deleted successfully"}
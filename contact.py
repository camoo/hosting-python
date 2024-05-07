import requests
from models.contact import ContactModel
from response import ResponseDTO

class Contact:
    def __init__(self, access_token):
        self.base_url = "https://api.camoo.hosting/v1/contacts/add"
        self.access_token = access_token

    def add_contact(self, contact_data: dict):
        """Adds a contact using the validated details from the Contact model."""
        if not self.access_token:
            raise ValueError("Access token is missing. Please authenticate first.")

        try:
            # Validate and create contact using Pydantic model
            contact = ContactModel(**contact_data)
        except ValueError as e:
            # Handle validation errors
            print(f"Validation error: {e}")
            return None

        # Prepare headers and make API request
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Serialize data excluding None values and using aliases for field names
        serialized_data = contact.dict(by_alias=True, exclude_none=True)

        response = requests.post(self.base_url, headers=headers, data=serialized_data)
        if response.status_code == 200:
            return ResponseDTO(response.json())
        else:
            raise Exception(f"Failed to add contact: {response.status_code} {response.text}")

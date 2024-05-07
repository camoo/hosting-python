import requests
import logging
from response import ResponseDTO

class Domain:
    def __init__(self, access_token):
        self.base_url = "https://api.camoo.hosting/v1/domains/"
        self.access_token = access_token
        logging.basicConfig(level=logging.INFO)

    def check_domain_availability(self, domain, tlds):
        """Check the availability of specified domain names."""
        if not self.access_token:
            logging.error("Access token is missing. Authentication required.")
            raise ValueError("Access token is missing. Please authenticate first.")

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'domain': domain,
            'tlds': tlds
        }
        response = self._post_request("availability", data, headers)
        return ResponseDTO(response.json())

    def register_domain(self, domain_name, years, ns, reg_contact_id, admin_contact_id, tech_contact_id, billing_contact_id):
        """Register a domain name."""
        if not self.access_token:
            logging.error("Access token is missing. Authentication required.")
            raise ValueError("Access token is missing. Please authenticate first.")

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            "domain-name": domain_name,
            "years": years,
            "ns": ns,
            "reg-contact-id": reg_contact_id,
            "admin-contact-id": admin_contact_id,
            "tech-contact-id": tech_contact_id,
            "billing-contact-id": billing_contact_id
        }
        response = self._post_request("register", data, headers)
        return ResponseDTO(response.json())

    def _post_request(self, endpoint, data, headers):
        """Helper method to send POST requests."""
        full_url = self.base_url + endpoint
        response = requests.post(full_url, data=data, headers=headers)
        if response.status_code != 200:
            logging.error(f"Failed to post data: {response.status_code} {response.text}")
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")
        return response

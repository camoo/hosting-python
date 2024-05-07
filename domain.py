import requests
import logging
from response import ResponseDTO

class Domain:
    def __init__(self, access_token):
        self.base_url = "https://api.camoo.hosting/v1/domains/availability"
        self.access_token = access_token
        # Setup basic logging
        logging.basicConfig(level=logging.INFO)

    def check_domain_availability(self, domain, tlds):
        """Check the availability of specified domain names."""
        if not self.access_token:
            logging.error("Access token is missing. Authentication required.")
            raise ValueError("Access token is missing. Please authenticate first.")

        # Data validation can be added here
        if not domain or not tlds:
            logging.error("Invalid input: Domain or TLDs are missing.")
            raise ValueError("Domain and TLDs must be provided.")

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'domain': domain,
            'tlds': tlds
        }
        try:
            response = requests.post(self.base_url, data=data, headers=headers)
            if response.status_code == 200:
                return ResponseDTO(response.json())
            else:
                logging.error(f"API Error {response.status_code}: {response.text}")
                response.raise_for_status()  # This will raise HTTPError for bad responses
        except requests.RequestException as e:
            logging.exception("Failed to check domain availability due to a network error.")
            raise ConnectionError("Network error occurred while checking domain availability.") from e


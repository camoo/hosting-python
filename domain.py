import requests
import logging
from response import ResponseDTO
import socket
from models.domain import DomainModel
from pydantic import ValidationError

class Domain:
    ACCESS_TOKEN_MISSING_MSG = "Access token is missing. Authentication required."
    ACCESS_TOKEN_MISSING_LOGIN = "Access token is missing. Please authenticate first."
    def __init__(self, access_token):
        self.base_url = "https://api.camoo.hosting/v1/domains/"
        self.access_token = access_token
        logging.basicConfig(level=logging.INFO)

    def check_domain_availability(self, domain, tlds):
        if not self.access_token:
            logging.error(self.ACCESS_TOKEN_MISSING_MSG)
            raise PermissionError(self.ACCESS_TOKEN_MISSING_LOGIN)
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {'domain': domain, 'tlds': tlds}
        response = self._post_request("availability", data, headers)
        return ResponseDTO(response.json())

    def register_domain(self, domain_name, years, ns, reg_contact_id, admin_contact_id, tech_contact_id, billing_contact_id):
        if not self.access_token:
            logging.error(self.ACCESS_TOKEN_MISSING_MSG)
            raise PermissionError(self.ACCESS_TOKEN_MISSING_LOGIN)
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

    def modify_nameservers(self, domain_id, new_nameservers):
        if not self.access_token:
            logging.error(self.ACCESS_TOKEN_MISSING_MSG)
            raise PermissionError(self.ACCESS_TOKEN_MISSING_LOGIN)

        # Validate domain_id
        if not isinstance(domain_id, int) or domain_id <= 0:
            raise ValueError("Domain ID must be a positive integer greater than zero.")

        # Validate new_nameservers
        nameservers = new_nameservers.split(',')
        if len(nameservers) < 2:
            raise ValueError("At least two nameservers are required.")

        # Check if nameservers can resolve to an IP
        for ns in nameservers:
            try:
                socket.gethostbyname(ns.strip())
            except socket.gaierror:
                raise ValueError(f"Nameserver {ns} cannot be resolved to an IP address.")

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'multipart/form-data'
        }
        data = {
            'id': domain_id,
            'ns': new_nameservers
        }
        response = self._post_request("modify-nameservers", data, headers)
        return ResponseDTO(response.json())


    def get_domain_details(self, domain_id):
        """
        Retrieves domain details by ID.

        Parameters:
        - domain_id (int): The unique identifier for the domain.

        Returns:
        - An instance of DomainModel containing the domain details.
        """
        if not self.access_token:
            logging.error(self.ACCESS_TOKEN_MISSING_MSG)
            raise PermissionError(self.ACCESS_TOKEN_MISSING_MSG)

        if not isinstance(domain_id, int) or domain_id <= 0:
            raise ValueError("Domain ID must be a positive integer greater than zero.")

        endpoint = f"details?id={domain_id}"
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self._get_request(endpoint, headers)
        if response.status_code == 200:
            try:
                domain_details = DomainModel(**response.json()['result'])
                return domain_details
            except ValidationError as e:
                logging.error("Validation error: %s", e.json())
                raise ValueError("Failed to validate domain details")
        else:
            logging.error(f"Failed to get domain details: {response.status_code} {response.text}")
            raise ConnectionError(f"HTTP Error {response.status_code}: {response.text}")


    def _get_request(self, endpoint: str, headers):
        """
        Helper method to send GET requests to the API.

        Parameters:
        - endpoint (str): The API endpoint to be appended to the base URL.
        - headers (dict): Headers to be used in the GET request.

        Returns:
        - The response from the GET request.
        """
        full_url = self.base_url + endpoint
        response = requests.get(full_url, headers=headers)
        if response.status_code != 200:
            logging.error(f"Failed to get data: {response.status_code} {response.text}")
            raise ConnectionError(f"HTTP Error {response.status_code}: {response.text}")
        return response

    def _post_request(self, endpoint: str, data, headers):
        full_url = self.base_url + endpoint
        response = requests.post(full_url, data=data, headers=headers)
        if response.status_code != 200:
            logging.error(f"Failed to post data: {response.status_code} {response.text}")
            raise ConnectionError(f"HTTP Error {response.status_code}: {response.text}")
        return response

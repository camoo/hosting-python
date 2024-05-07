import requests

class AccessToken:
    def __init__(self, email, password, base_url="https://api.camoo.hosting/v1/auth"):
        self.base_url = base_url
        self.email = email
        self.password = password
        self.token = None
        self.token_type = None
        self.expires_in = None
        self.scope = None

    def authenticate(self):
        """Authenticate with the CAMOO Hosting API and retrieve the access token."""
        data = {
            'email': self.email,
            'password': self.password
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(self.base_url, data=data, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if response_data.get('status') == 'OK' and 'result' in response_data:
                self.token = response_data['result'].get('access_token')
                self.token_type = response_data['result'].get('token_type')
                self.expires_in = response_data['result'].get('expires_in')
                self.scope = response_data['result'].get('scope')
                print("Authentication successful:", response_data.get('message'))
                return self.token
            else:
                error_message = response_data.get('message', 'Unknown error occurred.')
                raise Exception(f"Authentication Failed: {error_message}")
        else:
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")

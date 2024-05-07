class ResponseDTO:
    def __init__(self, response_data):
        self.status = response_data.get('status', 'KO')
        self.result = response_data.get('result', {})

    def is_successful(self):
        return self.status == 'OK'

    def __getitem__(self, key):
        """Allows dictionary-like access to the result directly."""
        return self.result.get(key, None)

    def __str__(self):
        """Provides a string representation of the DTO, useful for debugging."""
        return f"ResponseDTO(status={self.status}, result={self.result})"

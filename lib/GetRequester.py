# lib/GetRequester.py

import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Return raw bytes, not decoded string

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)  # This handles bytes or string automatically

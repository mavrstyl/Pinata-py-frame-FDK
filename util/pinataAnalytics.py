import json
import requests
import os

def send_post_request(body_json):
    url = "https://api.pinata.cloud/farcaster/frames/interactions"
    payload = {
        "frame_id": os.environ.get('TITLE'),
        "data": body_json
    }
    headers = {
        "Authorization": f"Bearer {os.environ.get('PINATA_JWT')}",
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

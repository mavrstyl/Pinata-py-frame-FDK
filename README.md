# A Simple Frame For Showcasing Content

## Project Variables
GATEWAY_URL=Your Pinata Gateway

PROJECT_URL=Your Server URL

FOLDER_CID=The CID hash that you want to showcase in your frame.

PINATA_JWT=This is your Pinata JWT that will be used so you can get frame analytics on your frame.

## Build Command:
pip install -r requirements.txt

## Deploy Command:
uvicorn main:app --host 0.0.0.0 --port $PORT
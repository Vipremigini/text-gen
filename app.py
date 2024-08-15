from flask import Flask, request
import requests
import time

url = 'https://jamsapi.hackclub.dev/openai/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': ''
}
data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {
            'role': 'user',
            'content': ''
        }
    ]
}

app = Flask(__name__)

@app.post("/api/get")
def get():
    response = requests.post(url, headers=headers, json=data)
    rdata = response.json()
    rtext = rdata['choices'][0]['message']['content']
    rsend = {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": rtext
      }
    }]}
  
    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": rtext
      }
    }]}

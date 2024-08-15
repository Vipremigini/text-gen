from flask import Flask, request
import requests
import os
import main

url = 'https://jamsapi.hackclub.dev/openai/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': os.environ.get("aikey")
}


app = Flask(__name__)

@app.post("/api/get")
def get():
    gen = main.gent(main.lst,100)
    data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {
            'role': 'user',
            'content': " Explain this philosohy paragraph. return in one senstence. Reply like givng an advice: " + str(gen)}]}

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

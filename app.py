from flask import Flask, request
import requests
import os
import main
import re
import psycopg2

con = psycopg2.connect(database="verceldb", user='default', password=os.environ['POSTGRES_PASSWORD'], host=os.environ["POSTGRES_HOST"])
cur = con.cursor()

url = 'https://jamsapi.hackclub.dev/openai/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': os.environ.get("aikey")
}


f = open("text.txt", "r" )
text = f.read()
text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
text = text.lower()
s = text.split()
lst = []
for i in range(len(s)-2):
    k = [s[i],s[i+1],s[i+2]]
    k = tuple(k)
    lst.append(k)

mod = main.gentmod(lst)
app = Flask(__name__)

@app.post("/api/get")
def get():
    gen = main.gent(main.lst,100,mod)
    data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {
            'role': 'user',
            'content': " Explain this philosohy paragraph. return in one senstence. Reply like givng an advice: " + str(gen)}]}

    response = requests.post(url, headers=headers, json=data)
    rdata = response.json()
    rtext = rdata['choices'][0]['message']['content']
    ctext = rtext
    qlist = []
    for i in range(len(ctext)):
        if ctext[i] == "'":
            qlist.append(i)
    for i in range(len(qlist)):
        qlist[i] = qlist[i] + 1
    for i in qlist:
        ctext = ctext[:i+1] + "'" + ctext[i+1:]
        
    com = "insert into botquotes values('" + ctext + "')"
    cur.execute(com)
    con.commit()
    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": rtext
      }
    }]}

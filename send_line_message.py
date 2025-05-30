import requests
import os

line_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
user_id = os.environ['LINE_USER_ID']

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {line_token}"
}

data = {
    "to": user_id,
    "messages": [{"type": "text", "text": "這是由 Python 程式排程發送的訊息！"}]
}

res = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=data)
print(res.status_code, res.text)

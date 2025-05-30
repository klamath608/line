import requests
import os

def send_line_message(user_id, message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {os.environ['LINE_CHANNEL_ACCESS_TOKEN']}",
        "Content-Type": "application/json"
    }
    body = {
        "to": user_id,
        "messages": [{
            "type": "text",
            "text": message
        }]
    }

    response = requests.post(url, headers=headers, json=body)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    user_id = os.environ['Uef360c65c710f997a64c572b40fd8251D']
    message = "每天早安提醒：記得喝水💧"  # 可以改成你要的文字
    send_line_message(user_id, message)

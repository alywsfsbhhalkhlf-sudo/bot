import requests
import time

TOKEN = "9214686891:AAFwB8MDYyLNYfsnWwkep60ZBT oPdnEB1K0"
URL = f"https://api.telegram.org/bot{TOKEN}/"

print("Bot is starting...")

def main():
    offset = 0
    while True:
        try:
            response = requests.get(URL + f"getUpdates?offset={offset}&timeout=30")
            data = response.json()
            if "result" in data:
                for update in data["result"]:
                    offset = update["update_id"] + 1
                    chat_id = update["message"]["chat"]["id"]
                    text = update.get("message", {}).get("text", "")

                    if text:
                        requests.post(URL + "sendMessage", json={
                            "chat_id": chat_id,
                            "text": f"أهلاً بك! وصلني ردك: {text}"
                        })
        except Exception as e:
            print("Error:", e)
        time.sleep(1)

if __name__ == "__main__":
    main()
                  

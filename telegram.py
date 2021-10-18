import requests

bot_token = "2090374960:AAF-Aa92v26R_4Jx0qcHnXODLM9eVG7r5Kk"
link = "https://api.telegram.org/bot"+ bot_token 

def sendMessage(chat_id, message):
    requests.post(link + "/sendMessage", json={
        "chat_id": chat_id,
        "text": message
    })

def getUpdates():
    return requests.post(link + "/getUpdates").json()


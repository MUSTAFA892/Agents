from flask import Flask, request, jsonify
import requests
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PHONE_NUMBER_ID = os.getenv('PHONE_NUMBER_ID')
WHATSAPP_API_URL = f'https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
MAX_WHATSAPP_TEXT_LENGTH = int(os.getenv('MAX_WHATSAPP_TEXT_LENGTH', 4096))


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and verify_token == VERIFY_TOKEN:
            return challenge, 200
        return 'Verification failed', 403

    if request.method == 'POST':
        data = request.json
        print("Incoming Data:", data)

        try:
            message = data.get('entry', [])[0].get('changes', [])[0].get('value', {}).get('messages', [])[0]
            sender_id = message['from']
            text = message['text']['body']
            print(f"From {sender_id}: {text}")

            gemini_reply = ask_gemini(text)
            send_whatsapp_text(sender_id, gemini_reply)

        except Exception as e:
            print("Error in POST handler:", e)

        return jsonify({'status': 'received'}), 200


def ask_gemini(prompt):
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[{"parts": [{"text": prompt}]}]
        )
        return response.candidates[0].content.parts[0].text.strip()
    except Exception as e:
        print("Gemini Client Error:", e)
        return "Sorry, I couldn't generate a response right now."


def send_whatsapp_text(to, message):
    if len(message) > MAX_WHATSAPP_TEXT_LENGTH:
        message = message[:MAX_WHATSAPP_TEXT_LENGTH - 3] + "..."

    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }

    response = requests.post(WHATSAPP_API_URL, headers=headers, json=payload)
    print("WhatsApp Response:", response.status_code, response.text)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Use PORT from env, default to 8000
    app.run(host="0.0.0.0", port=port, debug=True)


from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# استبدل هذا بالتوكن الخاص ببوت تيليجرام
TELEGRAM_BOT_TOKEN = "6485013903:AAGaHv7785q0TuQwfmQtmavOz0sVk1qFQrk"
TELEGRAM_CHAT_ID = "5687308408"  # ضع هنا Chat ID الخاص بك

# دالة لإرسال الرسائل إلى تيليجرام
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    response = requests.post(url, json=data)
    return response.json()

# نقطة استقبال من HTML
@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    user_message = data.get("message", "")

    if user_message:
        send_to_telegram(user_message)
        return jsonify({"status": "تم الإرسال"})
    else:
        return jsonify({"error": "الرسالة فارغة"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_message}]
    }
    r = requests.post(API_URL, headers=headers, json=body)
    reply = r.json().get("choices", [{}])[0].get("message", {}).get("content", "Sem resposta")
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

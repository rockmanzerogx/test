from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)
API_KEY = os.getenv("DEEPSEEK_API_KEY")  # Render inyectará esta variable
API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}]
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))  # ¡Importante para Render!
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables de entorno desde .env

app = Flask(__name__)
API_KEY = os.getenv("DEEPSEEK_API_KEY")  # Guarda tu API Key en .env
API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/")
def home():
    return render_template("index.html")

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
    


    if response.status_code == 200:
        ai_response = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": ai_response})
    else:
        return jsonify({"error": "No se pudo obtener respuesta"}), 500

if __name__ == "__main__":
    app.run(debug=True)
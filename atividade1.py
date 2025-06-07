from flask import Flask, request, jsonify
import requests
import threading
from pyngrok import conf, ngrok

app = Flask(__name__)

PUBLIC_ENDPOINT = "https://callback-iot.onrender.com/data"

@app.route("/data", methods=["GET"])
def get_data():
    try:
        response = requests.get(PUBLIC_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        return jsonify(data[-2:]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/visualize", methods=["POST"])
def visualize():
    try:
        payload = request.get_json()
        if not payload:
            return jsonify({"error": "Nenhum dado recebido"}), 400
        return jsonify({"message": "Dados recebidos com sucesso", "data": payload}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

PORT = 5001
def run_app():
    app.run()

threading.Thread(target=lambda: app.run(port=PORT)).start()

conf.get_default().auth_token =  "26vdzXz3bq5yUp7IcKUskikXsML_x9PSfrbQHVokbPDCSVo7"

ngrok.kill()
public_url = ngrok.connect(PORT)

print("API disponível em:", public_url)


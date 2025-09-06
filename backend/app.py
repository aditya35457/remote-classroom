from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/v1/health', methods=['GET'])
def health():
    return jsonify({"status":"ok"})

@app.route('/v1/auth/login', methods=['POST'])
def login():
    data = request.json or {}
    # placeholder: in real app validate credentials
    if data.get("email"):
        return jsonify({"token":"dev-token"}), 200
    return jsonify({"error":"missing email"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)

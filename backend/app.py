from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["http://127.0.0.1:5500"])

@app.before_request
def log_request():
    print("\n -- Incoming request --")
    print("Method : " , request.method)
    print("Path : ", request.path)
    print("Origin : ", request.headers.get("Origin"))
    
@app.after_request
def log_response(response):
    print("Status Code : ", response.status_code)
    return response

@app.route("/test-get", methods=["GET"])
def test_get():
    return jsonify({"message" : "TESTING GET MESSAGE - SUCCESS"})

@app.route("/test-post", methods=["POST"])
def test_post():
    data = request.json
    return jsonify({"received" : data})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
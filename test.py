from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def checkip():
    get = requests.get("https://api.myip.com/").json()
    ip = get.get('ip')
    return jsonify({"message": f"IP Server {ip}"})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request, render_template
from api.github import GitHub_report

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/github", methods=["GET"])
def github():
    user_name = request.args.get("user")
    if not user_name:
        return jsonify({"error": "Falta el parámetro 'user'"}), 400
    
    report = GitHub_report(user_name)
    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)


import requests

def check_rate_limit():
    url = "https://api.github.com/rate_limit"
    response = requests.get(url).json()
    print(response)  # Muestra el límite en la consola
    return response

check_rate_limit()
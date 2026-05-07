from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure DevSecOps Lab Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

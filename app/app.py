from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

scan_results = [
    {
        "severity": "HIGH",
        "package": "openssl",
        "cve": "CVE-2025-1234"
    },
    {
        "severity": "MEDIUM",
        "package": "flask",
        "cve": "CVE-2025-5678"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        scan_results=scan_results,
        timestamp=datetime.now()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0")

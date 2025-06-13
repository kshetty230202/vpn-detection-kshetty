from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload():
    ip = request.form.get("ipAddress")
    print(f"IP address: {ip}")

    # Dummy test payload for now
    payload = {
        "country": "United States",
        "isp": "Google LLC",
        "is_proxy": False,
        "is_hosting": False
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        data = response.json()
        print(f"Backend response: {response.json()}")
    except Exception as e:
        data = {"label": f"Request failed: {str(e)}"}

    return render_template("upload.html", result=data.get("label", "Error: No label"))

if __name__ == "__main__":
    app.run(debug=True)
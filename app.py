from flask import Flask, send_file, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def serve_image_and_log():
    ip = request.remote_addr
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[VISITOR LOG] {time} | IP: {ip}")

    return send_file("myfaith.jpg", mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

from flask import Flask, send_file, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def serve_image_and_log():
    ip = request.remote_addr
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
    log_file.write(f"{time} - {ip}\n")
    print(f"[LOG] {time} - {ip}")

    return send_file("myfaith.jpg", mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)


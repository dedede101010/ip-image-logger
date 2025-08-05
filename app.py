from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    with open("ip_log.txt", "a") as log_file:
        log_file.write(f"{time} - {ip}\n")

    return "IP logged."

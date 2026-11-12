"""MIS2001 Week 9 - Hands-on Exercise 1
A minimal self-contained Flask app deployed on a local server.
Run:  python app.py
Then open http://localhost:8000  or  http://<your-LAN-IP>:8000 from other devices.
"""

import socket

from flask import Flask, render_template

app = Flask(__name__)

PORT = 8000


def get_lan_ip() -> str:
    """Return the LAN IP other devices on the same Wi-Fi can use to reach us."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Does not actually send any packet, only resolves the outgoing interface.
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


@app.route("/")
def hands_on_1():
    return render_template("hands-on-1.html")


@app.route("/health")
def health():
    return {"status": "ok", "port": PORT}


if __name__ == "__main__":
    ip = get_lan_ip()
    print("=" * 60)
    print(" MIS2001 Week 9 - Exercise 1 : local server deployment")
    print("-" * 60)
    print(f"  Local   : http://127.0.0.1:{PORT}")
    print(f"  Network : http://{ip}:{PORT}")
    print("=" * 60)
    # host="0.0.0.0" is REQUIRED so that other devices can reach the app.
    app.run(host="0.0.0.0", port=PORT, debug=False)

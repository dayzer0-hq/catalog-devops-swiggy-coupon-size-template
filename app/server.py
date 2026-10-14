"""Swiggy coupon service

Deliberately small. What this board is about is everything AROUND this file.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8080"))


def payload():
    return {"code": "SAVE50", "max_discount_paise": 15000}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"{self.command} {self.path}", flush=True)
        if self.path.split("?")[0] in ("/coupon", "/"):
            body = json.dumps(payload()).encode()
            code = 200
        else:
            body = json.dumps({"error": "not found"}).encode()
            code = 404
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # the print above is the log line; this silences the default one


if __name__ == "__main__":
    print(f"Swiggy coupon service listening on {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

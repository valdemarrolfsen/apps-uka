#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os


class SPAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        full_path = self.translate_path(self.path)
        if self.path != "/" and not os.path.exists(full_path):
            self.path = "/index.html"
        return super().do_GET()


def run(host="127.0.0.1", port=8000):
    server = HTTPServer((host, port), SPAHandler)
    print(f"Serving SPA on http://{host}:{port}/ (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()

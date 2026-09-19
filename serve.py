#!/usr/bin/env python3
"""Local preview server for the site.

Same as `python3 -m http.server 8000` but tells the browser never to cache,
so every refresh shows the file as it is on disk.

    python3 serve.py            # http://localhost:8000
    python3 serve.py 8080       # another port
"""
import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), NoCacheHandler) as httpd:
        print(f"Serving on http://localhost:{PORT}  (Ctrl-C to stop)")
        httpd.serve_forever()

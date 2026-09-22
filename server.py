from http.server import BaseHTTPRequestHandler, HTTPServer import json
PATCHES = []
class Handler(BaseHTTPRequestHandler): def do_GET(self): if self.path == “/patches”: self.send_response(200) self.send_header(“Content-Type”, “application/json”) self.end_headers() self.wfile.write(json.dumps(PATCHES).encode()) else: self.send_response(404) self.end_headers()
if name == “main”: HTTPServer((“0.0.0.0”, 8000), Handler).serve_forever()

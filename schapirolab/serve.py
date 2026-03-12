#!/usr/bin/env python3
import http.server

PORT = 3456
DIRECTORY = '/Users/aschapir/Downloads/schapirolab'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with http.server.HTTPServer(('', PORT), Handler) as httpd:
    httpd.serve_forever()

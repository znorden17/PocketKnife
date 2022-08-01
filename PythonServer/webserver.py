#! /usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import time


PORT: int = 8000
HOST_NAME: str = ''


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.path.encode())


# class requestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('content-type', 'text/html')
#         self.end_headers()
#         self.wfile.write('Hello World'.encode())


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, PORT), requestHandler)
    print(f"SERVER STARTED | HOSTNAME: {HOST_NAME} | PORT: {PORT}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print(f"\nSERVER TERMINATED")


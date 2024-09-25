from http.server import BaseHTTPRequestHandler, HTTPServer
from .lib import Pasuwado, Generator

index_content: str
styles_content: bytes

with open("pasuwado/index.html") as index_file:
    index_content = index_file.read()

with open("pasuwado/styles.css") as styles_file:
    styles_content = styles_file.read().encode()

generator = Generator(Pasuwado())


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        content = index_content.replace("{a}", generator.generate(16)).encode()

        match self.path:
            case "/styles.css":
                content = styles_content
            case _:
                self.send_header("Content-Type", "text/html")
                self.end_headers()

        self.wfile.write(content)


server = HTTPServer(("0.0.0.0", 80), RequestHandlerClass=RequestHandler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()

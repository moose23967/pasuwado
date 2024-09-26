from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any

from pybars import Compiler

from .random_number_generator import RandomNumberGenerator
from .random_password_generator import RandomPasswordGenerator

index_template: Any
styles_content: bytes

with open("pasuwado/index.hbs") as index_file:
    index_content = index_file.read()

    index_template_compiler = Compiler()
    index_template = index_template_compiler.compile(index_content)

with open("pasuwado/styles.css") as styles_file:
    styles_content = styles_file.read().encode()

random_password_generator = RandomPasswordGenerator(RandomNumberGenerator())


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        content = index_template(
            {"password": random_password_generator.generate(16)}
        ).encode()

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

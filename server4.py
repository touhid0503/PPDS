from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PDF_PATH = "CSE_434_PPDS_Lab_Assignment.pdf"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/hello":
            self.handle_hello()

        elif self.path == "/pdf":
            self.handle_pdf()

        elif self.path == "/html":
            self.handle_html()

        else:
            self.send_error(404, "Not Found")

    # ── /hello ──────────────────────────────────────────
    def handle_hello(self):
        response = b"Hello, this is a simple HTTP server!"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    # ── /pdf ─────────────────────────────────────────────
    def handle_pdf(self):
        if not os.path.exists(PDF_PATH):
            self.send_error(404, "PDF file not found!")
            return

        with open(PDF_PATH, "rb") as f:
            data = f.read()

        self.send_response(200)
        self.send_header("Content-Type", "application/pdf")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    # ── /html ────────────────────────────────────────────
    def handle_html(self):
        html = """
        <html>
            <head><title>Simple Page</title></head>
            <body style="font-family: Arial; text-align:center; margin-top:50px;">
                <h1>Welcome to My Simple HTTP Server</h1>
                <p>This is an example HTML response.</p>
                <a href="/pdf">Click here to view the sample PDF</a>
            </body>
        </html>
        """.encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(html)))
        self.end_headers()
        self.wfile.write(html)

    # suppress default request logs (optional, remove to see logs)
    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), Handler)
    print("✅ Server started on port 8080")
    print("👉 Try:")
    print("   http://localhost:8080/hello")
    print("   http://localhost:8080/pdf")
    print("   http://localhost:8080/html")
    server.serve_forever()

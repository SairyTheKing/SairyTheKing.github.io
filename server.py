from http.server import HTTPServer, SimpleHTTPRequestHandler

class NoCorsHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # tells ngrok to skip the browser warning page
        # so Discord and other crawlers can fetch files directly
        self.send_header("ngrok-skip-browser-warning", "1")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def log_message(self, format, *args):
        # cleaner terminal output
        print(f"  {self.address_string()} - {args[0]} {args[1]}")

if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("", port), NoCorsHandler)
    print(f"\n  sairy's server running at http://localhost:{port}")
    print(f"  press Ctrl+C to stop\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  server stopped")

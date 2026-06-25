from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if not self.path.startswith("/"):
                self.send_error(400, "Bad Request")
                return

            with open("../app/templates/contacts.html", "r", encoding="utf-8") as file:
                html_content = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(html_content.encode("utf-8"))

        except FileNotFoundError:
            self.send_error(500, "Template file not found")

        except Exception as e:
            print(f"Ошибка сервера: {e}")
            self.send_error(500, "Internal Server Error")


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), MyHandler)
    print("Сервер запущен: http://localhost:8080")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        server.server_close()
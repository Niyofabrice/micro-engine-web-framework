class Response:
    def __init__(self, http_version="HTTP/1.1", status_code=None, status_message="", headers={}, message=""):
        self.http_version = http_version
        self.status_code = status_code
        self.status_message = status_message
        self.headers = headers
        if "Content-Length" not in headers:
            self.headers |= {"Content-Length": f"{len(message)}"}
        self.message = message
    
    def __str__(self):
        return f"{self.http_version} {self.status_code} {self.status_message}\r\n{"\r\n".join(f"{key}: {value}" for key, value in self.headers.items())}\r\n\r\n{self.message}"

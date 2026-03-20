class Request:
    """
    Class to help transform raw text into structured Python objects
    """
    def __init__(self, request):
        self.is_valid = True
        self.method = None
        self.headers = {}
        self.body = {}

        if len(request.split("\r\n\r\n", 1)) >= 2:

            head, body = request.split("\r\n\r\n", 1)
            self.body = body
            
            if len(head.split("\r\n", 1)) >= 2:
                request_line, headers = head.split("\r\n", 1)

                for line in headers.split("\r\n"):
                    key, value = line.split(":", 1)
                    self.headers |= {key.strip(): value.strip()}
            
                
                method, path, http_version = request_line.split(" ", 2)

                self.method = method
                self.path = path
                self.http_version = http_version
        else:
            self.is_valid = False
    

    def __str__(self):
        return f"{self.method} {self.path} {self.http_version}\r\n{"\r\n".join(f"{key}: {value}" for key, value in self.headers.items())}\r\n\r\n{self.body}"

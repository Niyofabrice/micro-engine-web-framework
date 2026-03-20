import inspect

class Router:
    def __init__(self):
        self.routes = {}

    def route(self, path, method):
        def routing(func):
            async def wrapper(*args, **kwargs):
                if inspect.iscoroutinefunction(func):
                    return await func(*args, **kwargs)
                return func(*args, **kwargs)
            self.routes.update({(path, method): wrapper})
            return wrapper
        return routing
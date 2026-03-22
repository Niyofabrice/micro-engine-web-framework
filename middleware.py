import time

class TimingMiddleware:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        duration = time.time() - self.start_time
        status = "SUCCESS" if exc_type is None else f"FAILED ({exc_type.__name__})"
        print(f"[METRIC] Request processed in {duration:.4f}s | Status: {status}")



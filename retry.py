import time, random

def retry(times):
    def outer(fn):
        def inner(*a, **kw):
            for i in range(times):
                try:
                    return fn(*a, **kw)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
                    time.sleep(1)
            raise Exception("All retries failed")
        return inner
    return outer

@retry(3)
def unstable_task():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

print(unstable_task())

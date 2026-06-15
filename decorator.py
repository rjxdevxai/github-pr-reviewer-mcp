def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func()
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper


@debug
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(2, 3))

def lazy_singleton(func):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = func(*args, **kwargs)
        return instance

    return wrapper


def provides(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

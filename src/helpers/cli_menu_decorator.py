paths = []

def cli_menu(path):
    def decorator(cls):
        def wrapper(*args, **kwargs):
            instance = cls(*args, **kwargs)

            paths.append((path, instance))

            return instance

        return wrapper

    return decorator

def configure_plugin_decorator(func):
    def wrapper(*args):
        kwargs = {key: value for key, value in args}
        return func(**kwargs)

    return wrapper

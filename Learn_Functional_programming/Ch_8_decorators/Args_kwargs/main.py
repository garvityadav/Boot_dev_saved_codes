def args_logger(*args, **kwargs):
    number = 1
    for arg in args:
        print(f"{number}. {arg}")
        number += 1

    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")

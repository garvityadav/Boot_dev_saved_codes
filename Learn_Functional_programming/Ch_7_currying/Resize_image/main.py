def new_resizer(max_width, max_height):
    def inner_fun(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def innermost_fun(width, height):
            nonlocal max_width, max_height, min_width, min_height
            width = min(max_width, width)
            width = max(min_width, width)
            height = min(max_height, height)
            height = max(min_height, height)
            return width, height

        return innermost_fun

    return inner_fun

def css_styles(initial_styles):
    copy = initial_styles.copy()

    def add_style(selector, property, value):
        if selector in copy.keys():
            copy[selector][property] = value
        else:
            copy[selector] = {property: value}
        return copy

    return add_style

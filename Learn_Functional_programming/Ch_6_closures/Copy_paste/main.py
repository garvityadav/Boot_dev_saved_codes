def new_clipboard(initial_clipboard):
    copy = initial_clipboard.copy()

    def copy_to_clipboard(key, value):
        copy[key] = value

    def paste_from_clipboard(key):
        if key in copy.keys():
            return copy[key]
        else:
            return ""

    return copy_to_clipboard, paste_from_clipboard

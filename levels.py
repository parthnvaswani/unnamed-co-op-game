import os.path


def max_level():
    max_level = 0
    while os.path.exists(f"levels/level{max_level}_data"):
        max_level += 1
    max_level -= 1
    return max_level

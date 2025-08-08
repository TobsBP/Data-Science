import sys

def get_sys_path():
    """Return the current system path."""
    return sys.path

print("Current system path:")

for path in get_sys_path():
    print(path)
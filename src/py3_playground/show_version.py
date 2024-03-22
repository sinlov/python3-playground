import platform


def show_python_version():
    print(''.join(['python version:'.ljust(24, ' '), platform.python_version()]))

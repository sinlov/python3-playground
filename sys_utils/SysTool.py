__author__ = 'sinlov'

import os
import platform


class SysTool:

    def __init__(self):
        pass

    @staticmethod
    def is_sys_windows():
        return platform.system() == "Windows"

    @staticmethod
    def find_cli_abs_path(cli_path, cwd_full_path):
        # type: (str, str) -> str
        if cli_path == '.':
            return cwd_full_path
        if cli_path.startswith('./'):
            return os.path.join(cwd_full_path, cli_path.lstrip('./'))
        if os.path.exists(cli_path):
            if cli_path.startswith(os.path.sep):
                return cli_path
            else:
                return os.path.join(cwd_full_path, cli_path)
        else:
            path_join = os.path.join(cwd_full_path, cli_path)
            return os.path.abspath(path_join)

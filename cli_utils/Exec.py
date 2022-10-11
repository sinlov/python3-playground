import os
import shlex
import subprocess
from subprocess import CompletedProcess


class Exec:

    @staticmethod
    def run(cli_string, cwd=None, timeout=int(5 * 60 * 1), is_shell=False):
        # type: (str, str, int,bool) -> CompletedProcess
        if is_shell:
            cmd_string_list = cli_string
        else:
            cmd_string_list = shlex.split(cli_string)
            # print log
        sub = subprocess.run(cmd_string_list, cwd=cwd,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=is_shell,
                             timeout=timeout,
                             bufsize=128)
        return sub

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

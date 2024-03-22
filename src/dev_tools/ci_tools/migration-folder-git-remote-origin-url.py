#!/usr/bin/env python
# flake8: noqa

import optparse
import os
import shlex
import subprocess
from subprocess import CompletedProcess

git_target_from = "gitea.parlor.sinlov.cn"
git_target_to = "gitea.sinlov.cn"

hint_help_info = """
this script for migration git remote origin url

more information see script code.
"""

cwd_path = os.getcwd()


class Exec:
    @staticmethod
    def run(cli_string, cwd=None, timeout=int(5 * 60 * 1), is_shell=False):
        # type: (str, str, int,bool) -> CompletedProcess
        if is_shell:
            cmd_string_list = cli_string
        else:
            cmd_string_list = shlex.split(cli_string)
            # print log
        sub = subprocess.run(
            cmd_string_list,
            cwd=cwd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=is_shell,
            timeout=timeout,
            bufsize=128,
        )
        return sub

    @staticmethod
    def exec(cli_string, cwd=None, timeout=int(5 * 60 * 1), is_shell=False):
        # type: (str, str, int, bool) -> (int, str, str)
        if is_shell:
            cmd_string_list = cli_string
        else:
            cmd_string_list = shlex.split(cli_string)
            # print log
        sub = subprocess.run(
            cmd_string_list,
            cwd=cwd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=is_shell,
            timeout=timeout,
            bufsize=128,
        )
        return sub.returncode, sub.stdout.decode(), sub.stderr.decode()

    @staticmethod
    def find_cli_abs_path(cli_path, cwd_full_path):
        # type: (str, str) -> str
        if cli_path == ".":
            return cwd_full_path
        if cli_path.startswith("./"):
            return os.path.join(cwd_full_path, cli_path.lstrip("./"))
        if os.path.exists(cli_path):
            if cli_path.startswith(os.path.sep):
                return cli_path
            else:
                return os.path.join(cwd_full_path, cli_path)
        else:
            path_join = os.path.join(cwd_full_path, cli_path)
            return os.path.abspath(path_join)


def start_migration_by_folder(folder, from_git_host, to_git_host) -> int:
    if not os.path.exists(folder):
        print(f"error path not exist: {folder}")
        return 0
    if os.path.isfile(folder):
        print(f"error not dir as path: {folder}")
        return 0
    cnt = 0
    for want_git_dir in os.listdir(folder):
        want_migration_folder = os.path.join(folder, want_git_dir)
        if os.path.isfile(want_migration_folder):
            continue
        git_hide_path = os.path.join(want_migration_folder, ".git")
        if not os.path.exists(git_hide_path) or os.path.isfile(git_hide_path):
            print(f"-> want migration folder not git work path: {want_migration_folder}")
            continue
        # print(f'~> start migration path: {want_migration_folder}')
        code, out, err = Exec.exec("git config --get remote.origin.url", want_migration_folder)
        if code != 0:
            print(f"err: {err}")
            continue
        now_url = out.strip()
        if from_git_host not in now_url:
            print(f"~> pass migration path: {want_migration_folder} remote.origin.url: {now_url}")
            continue
        new_url = now_url.replace(from_git_host, to_git_host, 1)
        print(f"new_url {new_url}")
        m_code, m_out, m_err = Exec.exec(
            f"git config remote.origin.url {new_url}", want_migration_folder
        )
        if m_code != 0:
            print(f"~> change remote.origin.url err at {want_migration_folder} to {new_url}")
            continue
        cnt += 1
        print(f"-> finish migration path: {want_migration_folder} to new url {new_url}")
    return cnt


if __name__ == "__main__":
    self_parser = optparse.OptionParser(
        "\n\t%prog -f [git host] -t [git host] [target dir]\n" + hint_help_info
    )
    self_parser.add_option(
        "-f",
        "--from",
        dest="from_git_host",
        type="string",
        help=f"want migration from host, default [ {git_target_from} ]",
        default=git_target_from,
        metavar=git_target_from,
    )
    self_parser.add_option(
        "-t",
        "--to",
        dest="to_git_host",
        type="string",
        help=f"to target git host, default [ {git_target_to} ]",
        default=git_target_to,
        metavar=git_target_to,
    )
    _parse_opt, _parse_args = self_parser.parse_args()

    migration_folder = cwd_path
    if len(_parse_args) == 0:
        print("_parse_args is zero")
        migration_folder = cwd_path
    else:
        migration_folder = Exec.find_cli_abs_path(_parse_args[0], cwd_path)
    print("=> migration_folder", migration_folder)
    m_count = 0
    m_count += start_migration_by_folder(
        migration_folder, _parse_opt.from_git_host, _parse_opt.to_git_host
    )
    print()
    print("=> migration count", m_count)

#!/usr/bin/env python3

import optparse
import os
import platform
import shlex
import subprocess
import sys
import time
import getpass
import logging
import logging.handlers
from subprocess import CompletedProcess

cli_version = '1.0.0'

cwd_path = os.getcwd()


class PLog:
    """
    init Plog like this
    ----------
    PLog.check_runtime()

    PLog.set_verbose(False) # will close [ debug info ] log

    PLog.set_no_color(False) # not use color

    PLog.init_logger(PLog.find_now_time_format('%Y-%m-%d-%H_%M_%S')) # init log file by time

    then use like
    ----------

    PLog.info()

    PLog.debug()

    PLog.warning()

    PLog.error()
    """

    def __init__(self):
        pass

    _runtime_version_error = """
This script must run python 3.7.+
"""

    ERROR = '\033[91m'
    OK_GREEN = '\033[96m'
    WARNING = '\033[93m'
    OK_BLUE = '\033[94m'
    HEADER = '\033[95m'
    WRITE = '\033[98m'
    BLACK = '\033[97m'
    END_LI = '\033[0m'

    _is_verbose = False
    _is_no_color = False
    _logger = None

    @staticmethod
    def check_runtime():
        """
        check runtime must python 3.7+

        :return: check error will exit
        """
        PLog.log('Python version %s' % platform.python_version(), 'd')
        version_split = platform.python_version().split('.')
        if version_split[0] != '3':
            PLog.log(PLog._runtime_version_error, 'e', True)
            exit(1)
        if version_split[1] < '7':
            PLog.log(PLog._runtime_version_error, 'e', True)
            exit(1)

    @staticmethod
    def find_now_time_format(format_time=str):
        # type: (str) -> str
        return time.strftime(format_time, time.localtime(time.time()))

    @staticmethod
    def init_logger(tag=str, log_dir='logs', prefix='plog', postfix='log', level=logging.DEBUG):
        # type: (str, str,str, str, any) ->  logging.Logger | None
        """
        init log file like

        PLog.init_logger(PLog.find_now_time_format('%Y-%m-%d-%H_%M_%S'))

        :param tag: log tag, most use time format
        :param log_dir: log file save folder, default: logs
        :param prefix: log file prefix, default is: plog
        :param postfix: log file postfix, default is: log
        :param level: log level save, default is: logging.DEBUG
        :return: logging.Logger | None, init fail when return None.
        """
        log_path = os.path.join(os.getcwd(), log_dir)
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        if not os.path.exists(log_path):
            return None
        log_file = os.path.join(log_dir, '{0}-{1}.{2}'.format(prefix, tag, postfix))
        handler = logging.handlers.RotatingFileHandler(
            filename=log_file, maxBytes=1024 * 1024, backupCount=5)
        # fmt = '%(asctime)s %(levelname)s %(name)s %(filename)s - %(message)s'
        fmt = '%(asctime)s %(levelname)s %(name)s - %(message)s'
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        PLog._logger = logging.getLogger(getpass.getuser())
        PLog._logger.addHandler(handler)
        PLog._logger.setLevel(level)
        return PLog._logger

    @staticmethod
    def set_verbose(verbose=False):
        """
        will close [ debug info ] log

        :param verbose: show [ debug info ] log must set True
        :return: None
        """
        PLog._is_verbose = verbose

    @staticmethod
    def set_no_color(no_color=False):
        """
        set no color out put

        :param no_color: default False
        :return: None
        """
        PLog._is_no_color = no_color

    @staticmethod
    def script_cur_dir_path():
        """
        get this script cur file path

        :return:
        """
        path = sys.path[0]
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

    @staticmethod
    def _is_sys_windows():
        return platform.system() == "Windows"

    @staticmethod
    def _log_tuple_to_str(info: tuple):
        if len(info) == 0:
            return ''
        p_l = []
        for i in info:
            p_l.append(str(i))
        l_join = ''.join(p_l)
        return l_join

    @staticmethod
    def log_normal(*info):
        t_str = PLog._log_tuple_to_str(info)
        if not PLog._is_sys_windows():
            print(PLog.WRITE + t_str + PLog.END_LI)
        else:
            print(t_str)

    @staticmethod
    def log_assert(*info):
        t_str = PLog._log_tuple_to_str(info)
        if not PLog._is_sys_windows():
            print(PLog.BLACK + t_str + PLog.END_LI)
        else:
            print(t_str)

    @staticmethod
    def log_info(*info):
        t_str = PLog._log_tuple_to_str(info)
        if not PLog._is_sys_windows():
            print(PLog.OK_GREEN + t_str + PLog.END_LI)
        else:
            print(t_str)

    @staticmethod
    def log_debug(*info):
        t_str = PLog._log_tuple_to_str(info)
        if not PLog._is_sys_windows():
            print(PLog.OK_BLUE + t_str + PLog.END_LI)
        else:
            print(t_str)

    @staticmethod
    def log_warning(*info):
        t_str = PLog._log_tuple_to_str(info)
        if not PLog._is_sys_windows():
            print(PLog.WARNING + t_str + PLog.END_LI)
        else:
            print(t_str)

    @staticmethod
    def log_error(*info):
        t_str = PLog._log_tuple_to_str(info)
        if not PLog._is_sys_windows():
            print(PLog.ERROR + t_str + PLog.END_LI)
        else:
            print(t_str)

    @staticmethod
    def log(msg, lev=str, must=False):
        # type: (str, str, bool) -> None
        """
        log only out std

        :param msg: log message
        :param lev: i d w e a
        :param must: default False
        :return: any
        """
        if not PLog._is_sys_windows():
            if PLog._is_no_color:
                print('%s' % msg)
                return
            if lev == 'i':
                if PLog._is_verbose or must:
                    PLog.log_info('%s' % msg)
            elif lev == 'd':
                if PLog._is_verbose or must:
                    PLog.log_debug('%s' % msg)
            elif lev == 'w':
                PLog.log_warning('%s' % msg)
            elif lev == 'e':
                PLog.log_error('%s' % msg)
            elif lev == 'a':
                PLog.log_assert('%s' % msg)
            else:
                if PLog._is_verbose or must:
                    PLog.log_normal('%s' % msg)
        else:
            if lev == 'w' or lev == 'e':
                print('%s\n' % msg)
            else:
                if PLog._is_verbose or must:
                    print('%s\n' % msg)

    @staticmethod
    def log_writer(msg, lev=str, must=False):
        # type: (str, str, bool) -> None
        """
        log out std and log file

        :param msg: log message
        :param lev: i d w e a
        :param must: default False
        :return: any
        """
        PLog.log(msg, lev, must)
        if PLog._logger is None:
            return
        if PLog._is_sys_windows():
            if lev == 'w' or lev == 'e':
                PLog._logger.warning(msg)
            elif lev == 'e':
                PLog._logger.error(msg)
            else:
                if PLog._is_verbose or must:
                    PLog._logger.info(msg)
        else:
            if lev == 'i':
                if PLog._is_verbose or must:
                    PLog._logger.info(msg)
            elif lev == 'd':
                if PLog._is_verbose or must:
                    PLog._logger.debug(msg)
            elif lev == 'w':
                PLog._logger.warning(msg)
            elif lev == 'e':
                PLog._logger.error(msg)
            elif lev == 'a':
                PLog._logger.error(msg)
            else:
                if PLog._is_verbose or must:
                    PLog._logger.info(msg)

    @staticmethod
    def info(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, 'i', must)

    @staticmethod
    def debug(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, 'd', must)

    @staticmethod
    def warning(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, 'w', must)

    @staticmethod
    def error(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, 'e', must)


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
    def exec(cli_string, cwd=None, timeout=int(5 * 60 * 1), is_shell=False):
        # type: (str, str, int, bool) -> (int, str, str)
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
        return sub.returncode, sub.stdout.decode(), sub.stderr.decode()

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


class OptDefClass:
    hint_help_info = """
Version :{0}

must use library by
    pip3 install XXX=x.x.x
more information see script code.
""".format(cli_version)

    cwd_script_file_name = sys.argv[0][sys.argv[0].rfind(os.sep) + 1:]
    enter_error_info = """
    Your input error
        Usage:
            python {0} --help
    or input:
        ./{0} -h to see help
    """.format(cwd_script_file_name)

    msg_open_force_mode = r'! warning open force mode'
    msg_interrupt_generate = r'generate interrupt, if you want to continue use --force'

    def __init__(self):
        self._parse_options = None
        self._parse_args = None
        self_parser = optparse.OptionParser('\n\t%prog' + ' -h\n\t%prog -v -c\n' + OptDefClass.hint_help_info)
        self_parser.add_option('-v', dest='v_verbose', action="store_true",
                               help="[-|+] see verbose",
                               default=False)
        self_parser.add_option('--no-log', dest='no_log', action="store_true",
                               help="[+|-] close cli log at path -> logs",
                               default=False)
        self_parser.add_option('--no-color', dest='no_color', action="store_true",
                               help="[+|-] close color cli out put",
                               default=False)
        self_parser.add_option('--force', dest='force', action="store_true",
                               help="[-|+] do job force, ignore warning",
                               default=False)
        self_parser.add_option('-c', '--clean', dest='c_clean', action="store_true",
                               help="[-|+] clean after cli",
                               default=False)
        self_parser.add_option('--config-file', dest='config_file', type="string",
                               help="config file default is config.json",
                               default="",
                               metavar="config.json")
        self._parse_options, self._parse_args = self_parser.parse_args()

    def this_script_name(self):
        # type: () -> str
        return self.cwd_script_file_name

    def opt(self):
        return self._parse_options

    def args(self):
        return self._parse_args

    def check_args_size_not_zero(self):
        if len(self._parse_args) == 0:
            print(
                'Error input args size is zero {0}'.format(
                    OptDefClass.enter_error_info)
            )
            raise Exception()

    def verification(self):
        if not self._parse_options.f_targetFile or not self._parse_options.c_clean:
            exit('ERROR!must support --clean and --targetFile parameters!')


if __name__ == '__main__':
    PLog.check_runtime()

    opt = OptDefClass()
    opt.check_args_size_not_zero()
    opt.verification()

    options = opt.opt()
    # --verbose
    if options.v_verbose:
        PLog.set_verbose(options.v_verbose)
    # --no-log
    if not options.no_log:
        PLog.init_logger(PLog.find_now_time_format('%Y-%m-%d-%H_%M_%S'))
    # --no-color
    if options.no_color:
        PLog.set_no_color(options.no_color)

    # --force
    if options.force:
        PLog.log_writer(OptDefClass.msg_open_force_mode, 'w')

    # --clean
    if options.c_clean:
        PLog.log_writer('now clean flag {0} force flag {1}'.format(options.c_clean, options.force), 'd')

    if options.config_file:
        config_file_path = options.config_file
    else:
        config_file_path = Exec.find_cli_abs_path('config.json', cwd_path)
    PLog.log('-> load config_file_path: {0}'.format(config_file_path), 'd')
    if not os.path.exists(config_file_path):
        PLog.log_writer('-> load config_file_path not exist: {0}'.format(config_file_path), 'e')

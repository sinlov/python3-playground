# -*- coding: utf-8 -*-

__author__ = 'sinlov'

import getpass
import os
import platform
import sys
import time
import logging
import logging.handlers


class PLog:
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
    def init_logger(tag=str, level=logging.DEBUG):
        # type: (str, any) -> bool
        log_path = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        if not os.path.exists(log_path):
            return False
        log_file = os.path.join('logs', 'log_{0}.log'.format(tag))
        handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
        # fmt = '%(asctime)s %(levelname)s %(name)s %(filename)s - %(message)s'
        fmt = '%(asctime)s %(levelname)s %(name)s - %(message)s'
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        PLog._logger = logging.getLogger(getpass.getuser())
        PLog._logger.addHandler(handler)
        PLog._logger.setLevel(level)
        return True

    @staticmethod
    def set_verbose(verbose=False):
        PLog._is_verbose = verbose

    @staticmethod
    def set_no_color(no_color=False):
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
    def log_normal(info):
        if not PLog._is_sys_windows():
            print(PLog.WRITE + info + PLog.END_LI)
        else:
            print(info)

    @staticmethod
    def log_assert(info):
        if not PLog._is_sys_windows():
            print(PLog.BLACK + info + PLog.END_LI)
        else:
            print(info)

    @staticmethod
    def log_info(info):
        if not PLog._is_sys_windows():
            print(PLog.OK_GREEN + info + PLog.END_LI)
        else:
            print(info)

    @staticmethod
    def log_debug(info):
        if not PLog._is_sys_windows():
            print(PLog.OK_BLUE + info + PLog.END_LI)
        else:
            print(info)

    @staticmethod
    def log_warning(info):
        if not PLog._is_sys_windows():
            print(PLog.WARNING + info + PLog.END_LI)
        else:
            print(info)

    @staticmethod
    def log_error(info):
        if not PLog._is_sys_windows():
            print(PLog.ERROR + info + PLog.END_LI)
        else:
            print(info)

    @staticmethod
    def log(msg, lev=str, must=False):
        # type: (str, str, bool) -> None
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
    def info(msg, must=False):
        PLog.log_writer(msg, 'i', must)

    @staticmethod
    def debug(msg, must=False):
        PLog.log_writer(msg, 'd', must)

    @staticmethod
    def warning(msg, must=False):
        PLog.log_writer(msg, 'w', must)

    @staticmethod
    def error(msg, must=False):
        PLog.log_writer(msg, 'e', must)

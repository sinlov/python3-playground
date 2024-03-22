# flake8: noqa
__author__ = "sinlov"

import getpass
import logging
import logging.handlers
import os
import platform
import sys
import time


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
This script must run python 3.8.+
"""

    ERROR = "\033[91m"
    OK_GREEN = "\033[96m"
    WARNING = "\033[93m"
    OK_BLUE = "\033[94m"
    HEADER = "\033[95m"
    WRITE = "\033[98m"
    BLACK = "\033[97m"
    END_LI = "\033[0m"

    _is_verbose = False
    _is_no_color = False
    _logger = None

    @staticmethod
    def check_runtime():
        """
        check runtime must python 3.8+

        :return: check error will exit
        """
        PLog.log("Python version %s" % platform.python_version(), "d")
        version_split = platform.python_version().split(".")
        if int(version_split[0]) != 3:
            PLog.log(PLog._runtime_version_error, "e", True)
            exit(1)
        if int(version_split[1]) < 8:
            PLog.log(PLog._runtime_version_error, "e", True)
            exit(1)

    @staticmethod
    def find_now_time_format(format_time=str):
        # type: (str) -> str
        return time.strftime(format_time, time.localtime(time.time()))

    @staticmethod
    def init_logger(tag=str, log_dir="logs", prefix="plog", postfix="log", level=logging.DEBUG):
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
        log_file = os.path.join(log_dir, "{0}-{1}.{2}".format(prefix, tag, postfix))
        handler = logging.handlers.RotatingFileHandler(
            filename=log_file, maxBytes=1024 * 1024, backupCount=5
        )
        # fmt = '%(asctime)s %(levelname)s %(name)s %(filename)s - %(message)s'
        fmt = "%(asctime)s %(levelname)s %(name)s - %(message)s"
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
            return ""
        p_l = []
        for i in info:
            p_l.append(str(i))
        l_join = "".join(p_l)
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
                print("%s" % msg)
                return
            if lev == "i":
                if PLog._is_verbose or must:
                    PLog.log_info("%s" % msg)
            elif lev == "d":
                if PLog._is_verbose or must:
                    PLog.log_debug("%s" % msg)
            elif lev == "w":
                PLog.log_warning("%s" % msg)
            elif lev == "e":
                PLog.log_error("%s" % msg)
            elif lev == "a":
                PLog.log_assert("%s" % msg)
            else:
                if PLog._is_verbose or must:
                    PLog.log_normal("%s" % msg)
        else:
            if lev == "w" or lev == "e":
                print("%s\n" % msg)
            else:
                if PLog._is_verbose or must:
                    print("%s\n" % msg)

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
            if lev == "w" or lev == "e":
                PLog._logger.warning(msg)
            elif lev == "e":
                PLog._logger.error(msg)
            else:
                if PLog._is_verbose or must:
                    PLog._logger.info(msg)
        else:
            if lev == "i":
                if PLog._is_verbose or must:
                    PLog._logger.info(msg)
            elif lev == "d":
                if PLog._is_verbose or must:
                    PLog._logger.debug(msg)
            elif lev == "w":
                PLog._logger.warning(msg)
            elif lev == "e":
                PLog._logger.error(msg)
            elif lev == "a":
                PLog._logger.error(msg)
            else:
                if PLog._is_verbose or must:
                    PLog._logger.info(msg)

    @staticmethod
    def info(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, "i", must)

    @staticmethod
    def debug(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, "d", must)

    @staticmethod
    def warning(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, "w", must)

    @staticmethod
    def error(*msg, must=False):
        t_str = PLog._log_tuple_to_str(msg)
        PLog.log_writer(t_str, "e", must)

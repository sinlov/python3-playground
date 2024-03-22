# flake8: noqa

__author__ = "sinlov"

import shlex
import subprocess
from subprocess import CompletedProcess


class ExecUtil:
    def __init__(self):
        pass

    """
    执行默认超时时间 3 * 60 * 1 秒
    """
    out_of_time_default = int(3 * 60 * 1)

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
    def execute_cli(cli_string, cwd=None, timeout=None, is_shell=False):
        """执行一个SHELL命令
            封装了subprocess的Popen方法, 支持超时判断，支持读取stdout和stderr
            如果没有指定标准输出和错误输出的管道，因此会打印到屏幕上
            另外的，可以通过返回的 returncode 来判断是否成执行


            支持超时原理：
                subprocess.poll()方法：检查子进程是否结束了，如果结束了
                设定并返回码，放在subprocess.returncode变量中
        参数:
          :param cli_string 运行命令字符串
          :param cwd 运行命令时更改路径，如果被设定，子进程会直接先更改当前路径到cwd
          :param timeout 超时时间，秒，支持小数，精度0.1秒，默认不输入无超时
          :param is_shell 是否通过shell运行,使用 shlex.split 来解析
        :return: return class Popen(object)
        :raises: Exception: 执行超时
        """
        if is_shell:
            cmd_string_list = cli_string
        else:
            cmd_string_list = shlex.split(cli_string)
        if timeout:
            end_time = timeout
        else:
            end_time = ExecUtil.out_of_time_default
            # print log
        sub = subprocess.run(
            cmd_string_list,
            cwd=cwd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=is_shell,
            timeout=end_time,
            bufsize=128,
        )
        # while sub.poll() is None:
        #     if is_info:
        #         stdout_readline = sub.stdout.readline()
        #         print(sub.stdout.readline())
        #         PLog.log_writer(stdout_readline, 'v', True)
        #         stderr_readline = sub.stderr.readline()
        #         print(sub.stderr.readline())
        #         PLog.log_writer(stderr_readline, 'v', True)
        #     time.sleep(0.1)
        #     if timeout:
        #         if end_time <= datetime.datetime.now():
        #             raise Exception('Timeout：%s' % cli_string)
        # try:
        #     out = sub.communicate()[0]
        #     print(out)
        # except Exception as e:
        #     print('execute_cli fast read err: %s' % e)
        #     pass
        return sub

    @staticmethod
    def exec_cli(cmd_string, cwd=None, time_out=None, is_shell=False):
        # type: (str,str, int, bool) -> bool
        """执行一个SHELL命令
            封装了subprocess的Popen方法, 支持超时判断，支持读取stdout和stderr
            默认开启打印执行输出，不可修改
            操时已经使用 max_out_of_time 设置
        参数:
          :param cmd_string 运行命令字符串
          :param cwd 运行命令时更改路径，如果被设定，子进程会直接先更改当前路径到cwd
          :param time_out 超时时间，秒，支持小数，精度0.1秒，默认不输入 超时使用 max_out_of_time 设置
          :param is_shell 是否通过shell运行,使用 shlex.split 来解析
        :return: return class Popen(object)
        :raises: Exception: 执行超时
        """
        try:
            if time_out is None:
                time_out = ExecUtil.out_of_time_default
            # PLog.log(
            #     '\ncli -> %s\ncwd -> %s\ntimeOut -> %s\nis_shell -> %s\n' % (cmd_string, cwd, time_out, is_shell),
            #     'v', True)
            command_out = ExecUtil.execute_cli(cmd_string, cwd, time_out, is_shell, True)
            if command_out.returncode == 0:
                # PLog.log_writer('{0}'.format(command_out.stdout.decode()), 'i', True)
                # PLog.log_writer('{0}'.format(command_out.stderr.decode()), 'w', True)
                return True
            else:
                # PLog.log_writer('{0}'.format(command_out.stdout.decode()), 'i', True)
                # PLog.log_writer('{0}'.format(command_out.stderr.decode()), 'e', True)
                return False
        except Exception as e:
            print("cmd_line error %s" % e)
            # PLog.log('cmd_line %s\nError info %s' % (cmd_string, str(e)), 'e', True)
            return False

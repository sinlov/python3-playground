import multiprocessing
import os
import platform
import threading

import psutil


def print_cpu_info():
    print('multiprocessing.current_process().ident', multiprocessing.cpu_count())
    thread = threading.currentThread()
    print('threading.ident', thread.ident)
    print('psutil.cpu_count', psutil.cpu_count())
    # print('cpu_percent', psutil.cpu_percent(percpu=True))
    if platform.system() == 'Linux':
        p = psutil.Process(os.getpid())
        print('process.cpu_affinity', p.cpu_affinity())
        print('process.cpu_num', p.cpu_num())
    pass

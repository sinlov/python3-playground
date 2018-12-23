# coding=utf-8

__author__ = 'sinlov'

from multiprocessing import Pool


class _Singleton(object):
    _instance = None

    def __new__(cls, *args: object, **kw: object):
        if not cls._instance:
            cls._instance = super(_Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MobiusRing(_Singleton):
    __write_count = 10

    def _sync_signal(self, num):
        return num

    def write_file(self, file_name: str, content: str, encoding='utf-8'):
        with open(file_name, 'a+', encoding=encoding) as f:
            f.writelines(str(content))

    def do(self):
        # e1 = time.time()
        pool = Pool()
        for i in range(self.__write_count):
            pool.apply_async(self._sync_signal, (i,), callback=self.write_file)
        pool.close()
        pool.join()
        # e2 = time.time()
        # print(float(e2 - e1))

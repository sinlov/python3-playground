# coding=utf-8

__author__ = "sinlov"

from multiprocessing import Pool


class _Singleton(object):
    _instance = None

    def __new__(cls, *args: object, **kw: object):
        if not cls._instance:
            cls._instance = super(_Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MobiusRing(_Singleton):
    __write_path = ""
    __write_count = 10
    __write_line_content = ""

    def set_write_path(self, path: str):
        self.__write_path = path

    def set_write_count(self, count: int):
        self.__write_count = count

    def set_write_line_content(self, content: str):
        self.__write_line_content = content

    def _sync_signal(self, num):
        return num

    def __write_file(self):
        with open(self.__write_path, "a+", encoding="utf-8") as f:
            f.writelines(str(self.__write_line_content))

    def do(self):
        # e1 = time.time()
        pool = Pool()
        for i in range(self.__write_count):
            pool.apply_async(self._sync_signal, (i,), callback=self.__write_file)
        pool.close()
        # pool.join()
        # e2 = time.time()
        # print(float(e2 - e1))

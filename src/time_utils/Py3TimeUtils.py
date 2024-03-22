import datetime
import time


class Py3TimeUtils:
    def __init__(self):
        pass

    @staticmethod
    def now_unix_timestamp():
        # type: () -> float
        return time.time()

    @staticmethod
    def now_unix_timestamp_second():
        # type: () -> int
        """
        now unix timestamp second
        :return:
        """
        return int(round(time.time()))

    @staticmethod
    def now_unix_timestamp_millisecond():
        # type: () -> int
        return int(round(time.time() * 1000))

    @staticmethod
    def now_unix_timestamp_microsecond():
        # type: () -> int
        return int(round(time.time() * 1000000))

    @staticmethod
    def now_time_format(fmt="%Y-%m-%d %H:%M:%S.%f"):
        # type: (str) -> str
        return datetime.datetime.now().strftime(fmt)

    @staticmethod
    def time_to_second(dt, fmt="%Y-%m-%d %H:%M:%S"):
        # type: (str, str) -> int
        """
        time str to second
        :param dt: like 2012-03-04 12:34:56
        :param fmt: %Y-%m-%d %H:%M:%S
        :return: int
        """
        return int(time.mktime(time.strptime(dt, fmt)))

    @staticmethod
    def timestamp_second_fmt(ts, fmt="%Y-%m-%d %H:%M:%S"):
        # type: (int, str) -> str
        """
        timestamp second
        :param ts: like 1515774430
        :param fmt: %Y-%m-%d %H:%M:%S
        :return: time
        """
        return time.strftime(fmt, time.localtime(ts))

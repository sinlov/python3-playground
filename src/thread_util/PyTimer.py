import threading
import time

from . import _logging


class PyTimer:
    on_stop = None
    """
    on_stop: function
            Callback object which is called when we get error.
            on_error has 1 arguments.
            The 1st argument is this class object.
    """

    on_error = None
    """
    on_error: function
            Callback object which is called when we get error.
            on_error has 2 arguments.
            The 1st argument is this class object.
            The 2nd argument is exception object.
    """

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.main_th = None
        self.running = False
        self.keep_running = False

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                _logging.error("error from callback {}: {}".format(callback, e))
                if self.on_error:
                    self.on_error(self, e)

    def _run_func(self):
        """
        run func
        :return:
        """
        th = threading.Thread(target=self.func, args=self.args, kwargs=self.kwargs)
        # th.setDaemon(True)
        th.daemon = True
        th.start()

    def _start(self, interval, once):
        if interval < 0.010:
            interval = 0.010

        if interval < 0.050:
            dt = interval / 10
        else:
            dt = 0.005

        if once:
            deadline = time.time() + interval
            while time.time() < deadline:
                time.sleep(dt)

            # call the scheduled event function, when the scheduled time is up
            self._run_func()
        else:
            self.running = True
            deadline = time.time() + interval
            while self.running:
                while time.time() < deadline:
                    time.sleep(dt)

                # update the next scheduled time
                deadline += interval

                # call the scheduled event function, when the scheduled time is up
                if self.running:
                    self._run_func()

    def start(self, interval, once=False):
        """
        start timer

        interval    - Timing interval Floating point with a maximum accuracy of 10 milliseconds in seconds
        once        - Whether to start only once. The default value is consecutive
        """
        th = threading.Thread(target=self._start, args=(interval, once))
        # th.setDaemon(True)
        th.daemon = True
        th.start()

    def run_forever(self, interval, once=False):
        self.keep_running = True
        self.main_th = threading.Thread(target=self._start, args=(interval, once))
        # self.main_th.setDaemon(True)
        self.main_th.daemon = True
        self.main_th.start()
        self.main_th.join()

    def stop(self):
        """
        stop timer
        """
        self.running = False
        if self.main_th and self.main_th.is_alive():
            self.keep_running = False
        if self.on_stop:
            self._callback(self.on_stop)

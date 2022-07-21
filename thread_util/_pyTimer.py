import time
import threading


class PyTimer:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.running = False

    def _run_func(self):
        """
        run func
        :return:
        """
        th = threading.Thread(target=self.func, args=self.args, kwargs=self.kwargs)
        th.setDaemon(True)
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
        th.setDaemon(True)
        th.start()

    def stop(self):
        """
        stop timer
        """
        self.running = False

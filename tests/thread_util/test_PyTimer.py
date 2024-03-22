import time
import unittest

from src.thread_util import PyTimer


class PyTimerTests(unittest.TestCase):
    py_timer = None
    cnt = 1

    def do_simple_timer(self, name):
        if self.cnt == 10 and self.py_timer is not None:
            print(time.time(), "time stop")
            self.py_timer.stop()
        print(time.time(), "time up", "class %s name %s" % (self.cnt, name))
        self.cnt += 1

    def on_py_timer_stop(self, pytimer):
        print(time.time(), "on_py_timer_stop")
        pass

    def test_simple_once(self):
        self.py_timer = PyTimer.PyTimer(self.do_simple_timer, "foo")
        self.py_timer.on_stop = self.on_py_timer_stop
        self.py_timer.run_forever(interval=1, once=False)

        # input('enter return\n')

        self.assertEqual(True, True)  # add assertion here


if __name__ == "__main__":
    unittest.main()

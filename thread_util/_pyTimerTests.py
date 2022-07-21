import time
import unittest

from thread_util._pyTimer import PyTimer


class PyTimerTests(unittest.TestCase):
    py_timer = None
    cnt = 1

    def do_simple_timer(self, name):
        if self.cnt == 10 and self.py_timer is not None:
            print(time.time(), 'time stop')
            self.py_timer.stop()
        print(time.time(), 'time up', 'class %s name %s' % (self.cnt, name))
        self.cnt += 1

    def test_simple_once(self):
        self.py_timer = PyTimer(self.do_simple_timer, 'foo')
        self.py_timer.start(interval=1, once=False)

        input('enter return\n')

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

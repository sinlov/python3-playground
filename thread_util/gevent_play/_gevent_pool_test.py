import time
import unittest

import gevent
from gevent.pool import Pool


class GEventPoolTests(unittest.TestCase):

    def pool_simple_each_biz(self, cnt):
        print(time.time(), '-> pool_simple_each_biz start cnt', cnt)
        gevent.sleep(cnt)
        print(time.time(), '-> pool_simple_each_biz end cnt', cnt)
        self.assertNotEqual(0, cnt)
        return cnt

    def test_pool_simple(self):
        print(time.time(), '-> test_pool_simple start')
        gp = Pool(2)
        apps = [
            gp.spawn(self.pool_simple_each_biz, 1),
            gp.spawn(self.pool_simple_each_biz, 2),
            gp.spawn(self.pool_simple_each_biz, 3),
            gp.spawn(self.pool_simple_each_biz, 4),
            gp.spawn(self.pool_simple_each_biz, 5),
            gp.spawn(self.pool_simple_each_biz, 6)
        ]
        print(time.time(), '-> test_pool_simple wait')
        gevent.joinall(apps)

        for i, g in enumerate(apps):
            print(f'~> test_pool_simple num {i}, return {g.value}')

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

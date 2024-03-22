import time
import unittest

import gevent
from gevent import Greenlet


class GEventTestsBase(unittest.TestCase):
    def target_1(self, num):
        print(time.time(), "-> run target_1", "args", num)
        self.assertNotEqual(0, num)

    def target_1_raw_back(self, job):
        print(time.time(), "-> run target_1_raw_back", job)
        self.assertEqual(True, True)

    def target_2(self, num):
        print(time.time(), "-> run target_2", "args", num)
        if self.job_1:
            print(time.time(), "job_1.ready", self.job_1.ready())
            print(time.time(), "job_1.successful", self.job_1.successful())
        if self.job_3:
            print(time.time(), "job_3.successful", self.job_3.successful())
        self.assertNotEqual(0, num)

    def target_3(self, num):
        print(time.time(), "-> run target_3", "args", num)
        if self.job_1:
            # get() gets the value returned by the coroutine
            print(time.time(), "job_1.get()", str(self.job_1.get()))
            # dead() Determine if the coroutine is dead

            # kill() kill the running coroutine and wake up the others.
            # This coroutine will not be executed again
            self.job_1.kill()
        if self.job_2:
            # ready() Task completion returns a true value
            print(time.time(), "job_2.ready", self.job_2.ready())
            # successful() Return true on successful completion of the task, otherwise an error is thrown
            print(time.time(), "job_2.successful", self.job_2.successful())
        self.assertNotEqual(0, num)

    def test_greenlet_object(self):
        # Greenlet.spawn()  # create one and start
        job = Greenlet(self.target_1, 3)
        print(time.time(), "-> run test_greenlet_object")

        # job.loop  loop object
        # job.value Gets the returned value
        # job.exception If the run has an error, get it
        # job.exc_info  Error details

        job.start_later(1)  # start later second
        # job.start()  # start now
        job.join(10)

        self.assertEqual(True, True)  # add assertion here

    def test_double_object(self):
        self.job_1 = Greenlet(self.target_1, 1)
        self.job_2 = Greenlet(self.target_2, 2)
        self.job_3 = Greenlet(self.target_3, 3)
        jobs = [self.job_1, self.job_2, self.job_3]
        self.job_1.start_later(5)
        self.job_2.start_later(3)
        self.job_3.start_later(1)

        gevent.joinall(jobs)  # wait all greenlet

    def test_raw_link(self):
        job = Greenlet(self.target_1, 4)
        job.rawlink(self.target_1_raw_back)
        # unlink() delete link call
        # job.unlink()
        print(time.time(), "-> run test_raw_link")
        job.start_later(1)
        job.join(10)

    def target_raw_success(self, job):
        print(time.time(), "-> target_raw_success")
        self.assertNotEqual(None, job)

    def target_raw_fail(self, job):
        print(time.time(), "-> target_raw_fail", job)
        self.assertNotEqual(None, job)

    def target_raw_run(self, cnt):
        print(time.time(), "-> target_raw_run cnt:", cnt)
        self.assertEqual(True, True)

    def test_raw_link_success(self):
        self.job_raw = Greenlet(self.target_raw_run, 50)
        self.job_raw.link_value(self.target_raw_success)
        self.job_raw.start_later(1)
        self.job_raw.join(10)

    def target_raw_run_exception(self, cnt):
        print(time.time(), "-> target_raw_run_exception cnt:", cnt)
        self.assertNotEqual(0, cnt)
        raise Exception("mock some error")

    def test_raw_link_fail(self):
        job = Greenlet(self.target_raw_run_exception, 0)
        job.link_value(self.target_raw_success)
        job.link_exception(self.target_raw_fail)
        job.start_later(1)
        job.join()


if __name__ == "__main__":
    unittest.main()

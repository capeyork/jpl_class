#!/usr/bin/env python

import unittest
from MyPriorityQueue import my_priority_queue
from Queue import PriorityQueue

class TestPriority (unittest.TestCase) :

#   define a built-in priority queue object
    global my_class
    my_class = PriorityQueue
    #my_class = my_priority_queue

#   start testing
    def test_empty (self):
        t = my_class()
        self.assert_(t.empty())

    def test_qsize (self):
        t = my_class()
        self.assert_(t.qsize() == 0)

    def test_put (self):
        t = my_class()
        t.put(2)
        t.put(3)
        t.put(3)
        t.put(1)
        self.assert_(t.qsize() == 4)

    def test_put_get (self):
        t = my_class()
        t.put(3)
        t.put(4)
        t.put(2)
        t.put(5)
        self.assert_(t.qsize() == 4)
        a = t.get()
        self.assert_(a == 2)
        self.assert_(t.qsize() == 3)

        self.assert_(not t.empty())

unittest.main()


#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from StdDev import stddev

# -----------
# Test
# -----------

class TestStdDev (unittest.TestCase) :
    # ----
    # stddev
    # ----

    def test_list_3 (self) :
        x = [1,2,3]
        b = stddev(x, 0)
        self.assert_(b == 0)

    def test_list_same_elements (self) :
        x = [1,1,1]
        b = stddev(x, 0.0)
        self.assert_(b == 1.0)

    def test_empty_list (self) :
        x = []
        b = stddev(x, 0)
        self.assert_(b == 0)

    def test_float (self) :
        x = [1,2,3,4,5]
        b = stddev(x, 0.0)
        self.assert_(b == 1.58113883)

    def test_tuple (self) :
        x = (1,2,3,4,5)
        b = stddev(x, 0)
        self.assert_(b == 1.58113883)

    def test_empty_tuple (self) :
        x = ()
        b = stddev(x, 0)
        self.assert_(b == 1.58113883)

# ----
# main
# ----

print "TestStddev.py"
unittest.main()
print "Done."

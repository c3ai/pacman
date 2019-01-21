"""
Unit tests for pacman.py
Last Modified: May 15, 2018
"""

import os
import sys
import time
import unittest

if len(sys.argv) > 0:
    loc = os.path.realpath(sys.argv[1])
    if sys.version_info >= (3, 5):
        import importlib.util
        spec = importlib.util.spec_from_file_location('pacman', loc)
        pacman = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pacman)
    elif sys.version_info >= (3, 3):
        from importlib.machinery import SourceFileLoader
        pacman = SourceFileLoader('pacman', loc).load_module()
    else:
        import imp
        pacman = imp.load_source('pacman', loc)

from pacman import pacman

class TestRuntime(unittest.TestCase):

    def test_generated_smaller(self):
        self.assertEqual(pacman("runtime.txt"), (2142, 147, 148))

    def test_average_runtime(self):
        times = [self.get_runtime() for i in range(10)]
        self.assertLess(sum(times)/len(times), 0.01)

    def get_runtime(self):
        start = time.time()
        pacman("runtime.txt")
        return time.time() - start

class TestSimulation(unittest.TestCase):

    def test_generic(self):
        self.assertEqual(pacman("generic.txt"), (6, 1, 27))

    def test_edge(self):
        self.assertEqual(pacman("edge.txt"), (-1, -1, 0))

if __name__ == '__main__':
    for testClass in [TestRuntime, TestSimulation]:
        print('\n\nTest Class: {}\n'.format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)

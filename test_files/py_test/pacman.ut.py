"""
Unit tests for pacman.py
Last Modified: May 15, 2018

n.b. ensure you are running with the correct version of Python (2/3) to match
     the candidate's submission!

Usage:
  python pacman.ut.py [../path/to/submission.py]
Arguments:
  [../path/to/submission.py]
    Optional path (relative or absolute) to the location of the pacman.py file
    you want to test. Note the file isn't required to be named 'pacman.py'.
    If ommitted, it's assumed that the board text files and pacman.py code are
    in the same directory as the location you are running from.
"""

import os
import sys
import time
import unittest

# If passing in a file location, load that module first.
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

# the below line is commented out because we need the submission file
# to be in the same directory as this file to avoid errors from 
# importing local modules
#sys.path.append(os.path.dirname(loc))
from pacman import pacman

class TestRuntime(unittest.TestCase):

    def test_generated_smaller(self):
        self.assertEqual(pacman("generated-smaller.txt"), (2142, 147, 148))

    def test_average_runtime(self):
        times = [self.get_runtime() for i in range(10)]
        self.assertLess(sum(times)/len(times), 0.01)

    def get_runtime(self):
        start = time.time()
        pacman("generated-smaller.txt")
        return time.time() - start

class TestSimulation(unittest.TestCase):

    def test_borders(self):
        self.assertEqual(pacman("borders.txt"), (9, 0, 19))

    def test_walls(self):
        self.assertEqual(pacman("walls.txt"), (4, 6, 8))

    def test_generic(self):
        self.assertEqual(pacman("generic.txt"), (6, 1, 27))

    def test_initialPosition1(self):
        self.assertEqual(pacman("initialPosition1.txt"), (-1, -1, 0))

    def test_initialPosition2(self):
        self.assertEqual(pacman("initialPosition2.txt"), (-1, -1, 0))

    # def test_generated(self):
    #     self.assertEqual(pacman("generated.txt"), (14869, 4926, 894))


if __name__ == '__main__':
    for testClass in [TestRuntime, TestSimulation]:
        print('\n\nTest Class: {}\n'.format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
        # print('{} failures for class {}'.format(len(result.failures), testClass.__name__))

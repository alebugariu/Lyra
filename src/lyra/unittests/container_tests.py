"""
Container Analysis - Unit Tests
============================================
"""


import glob
import os
import unittest

import sys

from lyra.abstract_domains.assumption.container_domain import ContainerState
from lyra.engine.backward import BackwardInterpreter
from lyra.semantics.backward import DefaultBackwardSemantics

from lyra.unittests.runner import TestRunner


class ContainerTest(TestRunner):

    def interpreter(self):
        return BackwardInterpreter(self.cfgs, self.fargs, DefaultBackwardSemantics(), 3)

    def state(self):
        return ContainerState(self.variables)


def test_suite():
    suite = unittest.TestSuite()
    name = os.getcwd() + '/container/must/**.py'
    for path in glob.iglob(name):
        if os.path.basename(path) != "__init__.py":
            print(os.path.basename(path))
            suite.addTest(ContainerTest(path))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite())
    if not result.wasSuccessful():
        sys.exit(1)

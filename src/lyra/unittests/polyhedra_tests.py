"""
Polyhedra Analysis - Unit Tests
===============================

:Authors: Caterina Urban
"""


import glob
import os
import sys
import unittest

from lyra.abstract_domains.numerical.polyhedra_domain import PolyhedraStateWithSummarization
from lyra.engine.backward import BackwardInterpreter
from lyra.engine.forward import ForwardInterpreter
from lyra.semantics.backward import DefaultBackwardSemantics
from lyra.semantics.forward import DefaultForwardSemantics
from lyra.unittests.runner import TestRunner


class ForwardPolyhedraTest(TestRunner):

    def interpreter(self):
        return ForwardInterpreter(self.cfgs, self.fargs, DefaultForwardSemantics(), 3)

    def state(self):
        return PolyhedraStateWithSummarization(self.variables)


class BackwardPolyhedraTest(TestRunner):

    def interpreter(self):
        return BackwardInterpreter(self.cfgs, self.fargs, DefaultBackwardSemantics(), 3)

    def state(self):
        return PolyhedraStateWithSummarization(self.variables)


def forward():
    suite = unittest.TestSuite()
    name = os.getcwd() + '/numerical/polyhedra/forward/**.py'
    for path in glob.iglob(name):
        if os.path.basename(path) != "__init__.py":
            print('forward/' + os.path.basename(path))
            suite.addTest(ForwardPolyhedraTest(path))
    return suite


def backward():
    suite = unittest.TestSuite()
    name = os.getcwd() + '/numerical/polyhedra/backward/**.py'
    for path in glob.iglob(name):
        if os.path.basename(path) != "__init__.py":
            print('backward/' + os.path.basename(path))
            suite.addTest(BackwardPolyhedraTest(path))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result1 = runner.run(forward())
    success1 = result1.wasSuccessful()
    result2 = runner.run(backward())
    success2 = result2.wasSuccessful()
    if not success1 or not success2:
        sys.exit(1)

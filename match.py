from functools import singledispatch
from typing import Sequence
from types import FunctionType

class Match:
    def __init__(self, match):
        self._match = match
        self._matched = False
        self._result = None
        self._returned_result = False

    @property
    def match(self):
        return self._match

    @property
    def result(self):
        if self._matched:
            return self._result       
        else:
            raise ValueError("Nothing matched. Result not available.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type: 
            return False
        if not self._matched:
            raise ValueError("Match cases incomplete.")

    def __or__(self, other):
        """ Enable the use of the | symbol between match instances"""
        return self if self._matched else other
    orelse = __or__        

    def __gt__(self, f):
        """ Enable the use of the > symbol for result processing"""
        if self._matched and not self._returned_result:
            self._result = f(self._match)
            self._returned_result = True
            return self._result
    then = __gt__

    def __call__(self, pattern):
        if not self._matched:
            self._matched = cmp(pattern, self._match)
        return self

@singledispatch
def cmp(pattern, match):
    return pattern in (match, ...)

@cmp.register(FunctionType)
def _(f, pattern):
    return f(pattern)

@cmp.register(type)
def _(pattern, match):
    return isinstance(match, pattern)

@cmp.register(Sequence)
def _(pattern, match):
    return all(cmp(p, m) for p, m in zip(pattern, match))      

@cmp.register(Match)
def _(other, _):
    return other._matched
#!/usr/bin/env python
import sys
import os
import time
import pytest
import pdb




#===============================================================================
# def func(x):
#     return x + 1
#  
# def test_answer():
#     assert func(3) == 5
#===============================================================================




#===============================================================================
# def f():
#     raise SystemExit(1)
# 
# def test_mytest():
#     with pytest.raises(SystemExit):
#             f()
#===============================================================================




#===============================================================================
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert 'a' in x
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, 'check')
#===============================================================================




#===============================================================================
# def test_needsfiles(tmpdir):
#     print (tmpdir)
#     assert 0
#===============================================================================



#@pytest.mark.skip(reason="no way of currently testing this")
#@pytest.mark.xfail
#@pytest.mark.xfail(strict=True)
#@pytest.mark.fail(msg='hi', pytrace=False)
def test_abc():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2























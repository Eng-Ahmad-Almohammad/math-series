import math_series.series as func

""" Testing for fibonacci function """
def test_fibonacci_zero():
    actual =  func.fibonacci(0)
    expected  = 0
    assert actual == expected

def test_fibonacci_one():
    actual =  func.fibonacci(1)
    expected  = 1
    assert actual == expected


def test_fibonacci_negative():
    actual =  func.fibonacci(-5)
    expected  = "Negative values are not allowable"
    assert actual == expected


def test_fibonacci_else():
    actual =  func.fibonacci(6)
    expected  = 8
    assert actual == expected

""" Testing for lucas function """

def test_lucas_zero():
    actual =  func.lucas(0)
    expected  = 2
    assert actual == expected


def test_lucas_one():
    actual =  func.lucas(1)
    expected  = 1
    assert actual == expected



def test_lucas_negative():
    actual =  func.lucas(-5)
    expected  = "Negative values are not allowable"
    assert actual == expected


def test_lucas_else():
    actual =  func.lucas(6)
    expected  = 18
    assert actual == expected


""" Testing for non_fibonacci_lucas function """


def test_non_fibonacci_lucas_zero():
    actual =  func.non_fibonacci_lucas(0,2,4)
    expected  = 2
    assert actual == expected


def test_non_fibonacci_lucas_one():
    actual =  func.non_fibonacci_lucas(1,2,4)
    expected  = 4
    assert actual == expected



def test_non_fibonacci_lucas_negative():
    actual =  func.non_fibonacci_lucas(-5,2,4)
    expected  = "Negative values are not allowable"
    assert actual == expected


def test_non_fibonacci_lucas_else():
    actual =  func.non_fibonacci_lucas(3,2,4)
    expected  = 10
    assert actual == expected
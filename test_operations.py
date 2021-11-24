import math

import operations


def test_suma():
    # TESTING
    assert operations.suma(3, 3) == 6
    assert operations.suma(0, 0) == 0
    assert operations.suma(-3, 3) == 0
    assert operations.suma(-4, -5) == -9


def test_resta():
    # TESTING
    assert operations.resta(3, 3) == 0
    assert operations.resta(0, 0) == 0
    assert operations.resta(-3, 3) == -6
    assert operations.resta(-4, -5) == 1


def test_mult():
    # TESTING
    assert operations.mult(3, 3) == 9
    assert operations.mult(0, 0) == 0
    assert operations.mult(-3, 3) == -9
    assert operations.mult(-4, -5) == 20


def test_div():
    # TESTING
    assert operations.div(3, 3) == 1
    assert math.isnan(operations.div(10, 0))
    assert operations.div(-3, 3) == -1
    assert operations.div(-10, -5) == 2


def test_square_root():
    assert operations.square(9) == 3
    assert operations.square(0) == 0
    assert math.isnan(operations.square(-9))


def test_factorial():
    assert operations.factorial(5) == 120
    assert operations.factorial(0) == 1
    assert operations.factorial(1) == 1
    assert math.isnan(operations.factorial(1.4))
    assert math.isnan(operations.factorial(-4))

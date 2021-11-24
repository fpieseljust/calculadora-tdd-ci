import math


def suma(sumand1, sumand2):
    return sumand1 + sumand2


def resta(minuend, sustraend):
    return minuend - sustraend


def mult(mult1, mult2):
    return mult1 * mult2


def div(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError as e:
        import math
        return math.nan


def square(radicand):
    try:
        return math.sqrt(radicand)
    except ValueError as e:
        return math.nan


def factorial(num):
    if(num >= 0 and type(num) == int):
        result = 1
        while(num > 1):
            result = num * result
            num = num - 1
        return result
    else:
        return math.nan


factorial(1.4)

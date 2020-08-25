#!/bin/python3

import math
import os
import random
import re
import sys

"""python: square Accumulate root"""
def consumer():
    while True:
        x = yield
        print(x)


def producer(n):
    for _ in range(n):
        x = int(input())
        yield x


# Complete the 'rooter', 'squarer', and 'accumulator' function below.

def rooter():
    # Write your code here
    sq_root = 0
    while True:
        sq_root = yield math.floor(math.sqrt(sq_root))


def squarer():
    # Write your code here
    square = 0
    while True:
        square = yield square ** 2


def accumulator():
    # Write your code her
    sum_of_square = 0
    while True:
        sum_of_square += yield sum_of_square


def pipeline(prod, workers, cons):
    for num in prod:
        for i, w in enumerate(workers):
            num = w.send(num)
        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()


if __name__ == '__main__':
    order = input().strip()

    n = int(input())

    prod = producer(n)

    cons = consumer()
    next(cons)

    root = rooter()
    next(root)

    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, eval(order), cons)



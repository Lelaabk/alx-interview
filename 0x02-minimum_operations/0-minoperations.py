#!/usr/bin/python3
""" Minoperation """

def minOperations(n):
    """ Calculates the min number of operations needed to achieve n char."""
    if n <= 1:
        return 0
    
    op = 0
    div = 2

    while n > 1:
        if n % div == 0:
            op += div
            n //= div
        else:
            div += 1

    return op
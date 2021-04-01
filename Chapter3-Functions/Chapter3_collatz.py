#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:18:40 2021

@author: niamhrigney
"""

def collatz(number):
    """If number is even (number // 2) else (3 * number + 1)
    Args:
        number (int): number to collatz
    Returns:
        int: collatz number
    """
    
    if number > 1:
        steps = 0
        while number != 1:
            if number % 2 == 0:
                print('Number is even and will be divided by 2 without a decimal: ' + str(number // 2))
                number = number // 2
                steps += 1   
            else:
                
                print('Number is odd and will be multiplied by 3 and 1 added to it: ' + str(3 * number + 1))
                number = 3 * number + 1
                steps += 1

    print('Collatz finished in ' + str(steps) + ' steps')


if __name__ == '__main__':
    
    try:
        collatz(int(input('Choose any integer greater than 1: ')))
    except ValueError:
        print('Non-Integer entered, program will exit')
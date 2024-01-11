#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fib_sequence = [0, 1]
        num1 = 0
        num2 = 1

        for _ in range(2, length):
            next_num = num1 + num2
            fib_sequence.append(next_num)
            num1, num2 = num2, next_num

        print(fib_sequence)

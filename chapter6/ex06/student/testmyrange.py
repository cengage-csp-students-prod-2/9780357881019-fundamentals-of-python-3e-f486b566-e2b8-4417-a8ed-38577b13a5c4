"""
Author: Ashley Francis
Date written: 02/17/2025
Assignment: Module 05 Practice Exercise 6-6
This program is designed to output a list of integers, without
producing a range object.
"""

def myRange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0 or (start < stop and step < 0) or (start > stop and step > 0):
        return []

    result = []
    if start < stop:
        while start < stop:
            result.append(start)
            start += step
    else:
        while start > stop:
            result.append(start)
            start += step

    return result

if __name__ == "__main__":
    print(myRange(5))          # [0, 1, 2, 3, 4]
    print(myRange(1, 5))       # [1, 2, 3, 4]
    print(myRange(5, 1))       # [5, 4, 3, 2]
    print(myRange(1, 10, 2))   # [1, 3, 5, 7, 9]
    print(myRange(10, 1, -2))  # [10, 8, 6, 4, 2]
    print(myRange(1, 10, 0))   # []
    print(myRange(10, 1, 0))   # []
    print(myRange(1, 10, -1))  # []
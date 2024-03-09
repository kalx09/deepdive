# Given a number N, find all factors of N.
#
# Example:
#
# N = 6
# factors = {1, 2, 3, 6}
# Make sure the returned array is sorted.

# 0(n) solution
# def solution(A):
#     if A == 0:
#         return 0
#     result = []
#     for i in range(A,0,-1):
#         if A%i == 0:
#             result.append(i)
#     result.sort()
#     return result
#
#
# print(solution(6))

# A Better (than Naive) Solution to find all divisors
import math


# method to print the divisors
def printDivisors(n):
    # Note that this loop runs till square root
    i = 1
    result = []
    while i <= math.sqrt(n):
        # print(math.sqrt(n))

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                print(i, end=" ")
                result.append(i)
            else:
                # Otherwise print both
                print(i, int(n / i), end=" ")
                result.append(i)
                result.append(int(n/i))
        i = i + 1
    result.sort()
    return result


print(printDivisors(30))

def solution(A):
    # sort the Aay
    A.sort()

    # Swap adjacent elements
    for i in range(0, len(A) - 1, 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    return A

print(solution([ 5, 1, 3, 2, 4 ]))
#1,7,2,8,3

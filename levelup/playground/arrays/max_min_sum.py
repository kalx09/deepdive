def solution(A):
    A.sort()
    return max(A) + min(A)

print(solution([-2, 1, -4, 5, 3]))

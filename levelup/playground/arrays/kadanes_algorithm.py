"""
Maximum Sum Subarray Problem (Kadane’s Algorithm)
Given an integer array, find a contiguous subarray within it that has the largest sum.
For example,
Input:  {-2, 1, -3, 4, -1, 2, 1, -5, 4}
Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6

https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""


def find_max_sum(list_obj):
    max_no = max(list_obj)
    
    if max_no < 0:
        return max_no
    
    max_so_far = 0
    max_ending_here = 0
    start_index = 0
    end_index = 0
    s = 0

    for i in range(len(list_obj)):
        max_ending_here = max_ending_here + list_obj[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start_index = s
            end_index = i

        if max_ending_here < 0:
            s = i+1
        # max_ending_here = max(max_ending_here, 0)
        # max_so_far = max(max_ending_here, max_so_far)
    return max_so_far, list_obj[start_index:end_index+1]


# print(find_max_sum([-8, -3, -6, -2, -5, -4]))
print(find_max_sum([5,7,-5,10,-1,3,-19,5]))

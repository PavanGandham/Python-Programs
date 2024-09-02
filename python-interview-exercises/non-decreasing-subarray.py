'''
You are given an array of integers, A. Find the length of the longest subarray whose elements are in non-decreasing order. 
Input format is, the first line contains N denoting the size of the array, A. 
The next line contains n space separated denoting the elements of the array.
Output format should be, print the length of the longest subarray whose elements are in non-decreasing order.

Example:
7
1 2 2 3 1 1 2
'''

def length_of_longest_non_decreasing_subarray(A):
    if not A:
        return 0
    max_len = 1
    curr_len = 1

    for i in range(0, len(A)):
        if A[i] <= A[i+1]:
            curr_len+=1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1
    max_len = max(max_len, curr_len)
    return max_len

# Read input
N = int(input())
A = list(map(int, input().split()))

length_of_longest_non_decreasing_subarray(A)
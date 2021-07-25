# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:

# Input: n = 3
# Output: [-1,0,1]
# Example 3:

# Input: n = 1
# Output: [0]
# Constraints:
# 1 <= n <= 1000

def solution(N):
    # write your code in Python 3.6
    mid = [0]
    right = list(range(N+1, N+1+N//2))
    left = list(map(lambda a: a*-1, right))
    if N % 2:
        result = right + mid + left
    else:
        result = right + left
    return result

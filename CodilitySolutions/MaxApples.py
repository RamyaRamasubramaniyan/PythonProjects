# Alice and Bob work in a beautiful orchard. There are N apple trees in the orchard. 
# The apple trees are arranged in a row and they are numbered from 1 to N.
# Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from L consecutive trees. 
# They want to choose two disjoint segments (one consisting of K trees for Alice and the other consisting of L trees for Bob) so as not to disturb each other. 
# What is the maximum number of apples that they can collect? 
# Write a function that given an array A consisting of N integers denating the number of apples on each apple tree in the row, 
# and integers K and L denoting, respectively, thenumber of trees that Alice and Bob can choose when collecting, 
# returns the maximum number of apples that can be collected by them, or -1 if there are no such intervals. 

# For example, given A =[6, 1,4,6,3,2,7,4], K=3, L=2, your function should return 24, because Alice can choose trees 3 to 5 and collect 4 + 6 + 3 = 13 apples, 
# and Bob can choose trees 7 to 8 and collect 7 + 4 = 11 apples. Thus, they will collect 13 + 11 = 24 apples in total, and that is the maximum number that can be achieved.
# Given A = [10, 19, 15], K = 2, L = 2, your function should return -1, because it is not possible for Alice and Bob to choose two disjoint intervals. 
# Assume that: N is an integer within the range [2..600]; K and L are integers within the range [1 .. N-1];
#   each element of array A is an integer within the range [1..500] In your solution focus on correctness.
# The performance of your solution will not be the focus of the assessment.

# P.s: did not receive 100% in result - task score 14 - Improvemennts / Suggestions Welcome

def solution(A, K, L):
    # write your code in Python 3.6
    k_max = checkmaxapples(A, K, L)
    l_max = checkmaxapples(A, L, K)
    result = max(k_max, l_max)
    return result

def checkmaxapples(A, K, L):
    if K+L > len(A):
        return -1
    sum_ = [0]*1000
    max_ = -1
    a = 0
    b = a+K
    sum_[0] = A[0]
    for i in range(1, len(A)):
        sum_[i] =sum_[i-1]+ A[i]
    for a in range(a+K-1, len(A)):
        if a > 0:
            x = sum_[a+K-1]-sum_[a-1]
        else:
            x = sum_[a+K-1]
        a=+1
        for b in range(b+L-1, len(A)):
            if b > 0:
                y = sum_[b+L-1]-sum_[b-1]
            else:
                x = sum_[b+L-1]
            b=+1
            if x + y > max_:
                max_ = x+y
    return max_

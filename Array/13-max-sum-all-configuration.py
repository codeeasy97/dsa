#Max sum in the configuration

"""
Algorithm
1. compute S0 and Sum of all arr elem.
2. To make next Configuration- 
Run a loop from 0 to N-1 and compute formula
S1 = S0 + (Sum - N*arr[N-1-i])
where arr[N-1-i] is last elem
......
This formula goes same for all configuration.

"""
"""
All Iteration for arr = [8,3,1,2]
S0 = 8*0 + 3*1 + 1*2 + 2*3 = 11
formula for S1 where i = 0
S(i+1) = S(i) + (sum - N*arr[N-1-i])
S(0+1) = S0 + (sum - N* arr[N-1-i])
S1  = 11 + (14 - 4* arr[4-1-0])
S1  = 11 + (14 - 4* arr[3])
S1  = 11 + (14 - 4*2)
S1 = 11 + (14 - 8)
S1  = 11 + (6)
S1 = 17
------------------------------------
formula for S2 where i = 1
S(i+1) = S(i) + (sum - N*arr[N-1-i])
S(1+1) = S1 + (sum - N* arr[N-1-i])
S2  = 17 + (14 - 4* arr[4-1-1])
S2  = 17 + (14 - 4* arr[2])
S2  = 17 + (14 - 4*1)
S1 = 17 + (14 - 4)
S2 = 17 + (10)
S2 = 27

and so on for all configuration
"""
#Method 2: TC - O(n) SC - O(1)
def maxSumInConfiguration(arr, n):
    sum = 0
    for x in arr:
        sum+=x

    cur_sum = 0
    for i in range(n):
        cur_sum += i*arr[i]

    max_sum = cur_sum

    for i in range(n):
        cur_sum = cur_sum + (sum - n*arr[n-1-i])
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


arr = [8, 3, 1, 2]
n = len(arr)
res = maxSumInConfiguration(arr, n)
print("Max Sum in Every Rotation is: ",res)
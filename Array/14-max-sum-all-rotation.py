# Maximum sum of i*arr[i] among all rotations of a given array

"""
Explanation: Lets look at all the rotations, rotate left to right
{8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
{3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
{1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
{2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*3 = 17

"""

#Method 1: TC - O(n)2 SC - O(1)
def maxSumEveryRotation(arr, n):
    max_sum = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(n):
            k = (i+j)%n
            sum+=j*arr[k]
        if sum > max_sum:
            max_sum = sum
    return max_sum



#Method 2: TC - O(n) SC - O(1)
def maxSumEveryRotationMethod2(arr, n):
    sum = 0
    for i in arr:
        sum+=i

    cur_sum = 0
    for i in range(n):
        cur_sum+=i*arr[i]
    
    max_sum = cur_sum


    for i in range(1, n):
        # si = (si-1 - (sum - arr[i-1]) + (arr[i-1]*(n-1)))
        cur_sum = (cur_sum - (sum - arr[i-1]) + arr[i-1]*(n-1))
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum



arr = [8, 3, 1, 2]
n = len(arr)
res = maxSumEveryRotation(arr, n)
print("Max Sum Every Rotation Using Brute Force is: ",res)

res = maxSumEveryRotationMethod2(arr, n)
print("Max Sum Every Rotation Optimize Approach is: ",res)
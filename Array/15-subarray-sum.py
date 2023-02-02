# Find Subarray with given sum | Set 1 (Non-negative Numbers)

#Brute Force Approach
def subArraySum(arr, sum):
    n = len(arr)
    for i in range(n):
        new_sum = arr[i]
        if new_sum == sum:
            print("given sum is at index ", i)
            return
        for j in range(i+1, n):
            new_sum = new_sum + arr[j]
            if new_sum == sum:
                print("Given sum is at index ",i, "and ", j )
                return


"""
1.make a variable put 1st element in it
2. start loop from 1st elem to end
3. add element to sum variable
4. check if sum grater remove first elem untill
    sum is not greater then given sum
5. check if sum equals given sum
"""

def slidingwindow(arr, sum):
    start = 0
    n = len(arr)
    new_sum = arr[start]
    for i in range(1,n):
        new_sum = new_sum + arr[i]
        while new_sum > sum:
            new_sum = new_sum - arr[start]
            start = start + 1
        if new_sum == sum:
            print("given sum is at index using sliding window ", start, " and ", i)
            return
    print("No subarray exist")



arr = [1, 4, 20, 3, 10, 5]
sum = 33
result = subArraySum(arr, sum)

result = slidingwindow(arr, sum)
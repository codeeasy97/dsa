# Longest Consecutive Subsequence
# arr = [1,9,3,10,4,20,2]
# {1,2,3,4} - 4
# {9,10}
# {20}
#   TC: O(NlogN) SC - O(N)
#   sort an array
#   create an empty list and add 1st arr elem
#   now iterate an arr from 2nd elem to end
#   check if curr arr ind elem is eq to prev elem + 1
#   if cond match increase count else re-initialize count by 1
#   store max to ans
#   return ans

#Using Sorting
def longConseSubsequence(arr,n):
    ans = 0
    count = 0
    arr.sort()
    new_arr = []

    #remove duplicate
    new_arr.append(arr[0])
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            new_arr.append(arr[i])
        # new_arr = [1,2,3,4,9,10,20]
    for i in range(len(new_arr)):
        if i > 0 and new_arr[i] == new_arr[i - 1] + 1:
            count+=1
        else:
            count = 1
        ans = max(ans, count)
    return ans

# Using Set - TC - O(n), SC- O(n)

# Add element to set
# check if prev ind elem not in set
# init elem to j an run while untill j in s
# outside while calculate ans by max of ans and j-arr[i]

def longConseSubsequenceUsingSet(arr,n):
    s = set()
    ans = 0
    for i in arr:
        if i not in s:
            s.add(i)

    # s = (1,9,3,10,4,20,2)
    print("\n")
    for i in range(n):
        if arr[i] - 1 not in s:
            j = arr[i] # 1|9 | 20
            print("start elem : ", j)
            while j in s:
                print("for "+str(arr[i])+ " seq no. is: ", j)
                j+=1
            print("final val of j is: ", j)
            ans = max(ans,j-arr[i]) #4 | 
            print("\n")
    return ans



arr = [1,9,3,10,4,20,2]
# res = longConseSubsequence(arr,len(arr))
# print("output is: ", res)

res = longConseSubsequenceUsingSet(arr,len(arr))
print("output is: ", res)
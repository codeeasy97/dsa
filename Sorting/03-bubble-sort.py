# Bubble Sort Algorithm

# 1.compare first two elem and swap if 2nd elem large 
# In first scan it will fix first largest element at
# its position.

# 2. Scan the array again, bubbling up the 
# second largest element.

# 3. Repeat until all elements are in order.

# Bubble Sort Algorithm
def bubbleSort(arr, n):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
        print("complete", i+1, "Pass")
    return arr

arr = [5,4,3,2,1]
n = len(arr)
res = bubbleSort(arr,n)
print(res)
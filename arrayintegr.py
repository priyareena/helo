def findMax(arr, low, high):
    max = arr[low]
    i = low
    for i in range(high+1):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [1, 30, 40, 50, 60, 70, 23, 20]
n = len(arr)
print ("The max element is %d"%
        findMax(arr, 0, n-1))
 

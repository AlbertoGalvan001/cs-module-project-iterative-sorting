def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # set indexes 
    left = 0
    right = len(arr) - 1

    while left <= right:
    # get middle
        mid = (left + right) // 2
    # check if middle is less than target
        if arr[mid] < target:
            # if so, set left to mid +1 to search to right.
            left = mid + 1
        elif arr[mid] > target:
            #if array at midddle is more than target
            # set right to mid -1 to search to left.
            right = mid - 1
        else:
            return mid        


    return -1  # not found

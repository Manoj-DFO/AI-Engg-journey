#first occurance using binary search
arr = [1, 2, 2, 2, 2, 3, 4]
target = 2

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2
    
    if arr[mid] > target:
        high = mid - 1

    elif arr[mid] < target:
        low = mid + 1

    else:
        ans = mid
        high = mid - 1

print(ans)



#last occurance using binary search
arr = [1, 2, 2, 2, 2, 3, 4]
target = 2

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2
    
    if arr[mid] > target:
        high = mid - 1

    elif arr[mid] < target:
        low = mid + 1

    else:
        ans = mid
        high = mid - 1

print(ans)

#missed element index
arr = [1, 3, 5, 6]
target = 2

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print(mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print(low)


#rotated array
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print(mid)
        break

    if arr[low] <= arr[mid]:

        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    else:

        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1

else:
    print(-1)
        
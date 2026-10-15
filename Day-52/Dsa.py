#first occurance
arr = [2, 4, 6, 8, 8, 8, 9, 11, 13]
n = 8

ans = -1

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2


    if arr[mid] >= n:

        high = mid - 1

    else:

        low = mid + 1

print(high+1)

#last occurance
arr = [2, 4, 6, 8, 8, 8, 9, 11, 13]
n = 8

ans = -1

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == n:

        ans = mid
        low = mid + 1

    elif arr[mid] <= n:

        low = mid + 1

    else:

        high = mid - 1

print(ans)


#search in rotated array
arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 3

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == k:

        print(mid)
        break

    if arr[low] == arr[high] == arr[mid]:

        low += 1
        high -= 1

    elif arr[low] <= arr[mid]:

        if arr[mid] <= k and arr[low] <= k:

            low = mid + 1

        else:

            high = mid - 1

    else:

        if arr[mid] >= k and arr[high] >= k:

            high = mid - 1

        else:

            low = mid + 1

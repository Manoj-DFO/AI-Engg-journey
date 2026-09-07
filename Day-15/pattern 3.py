# 2 pointers
arr = [1, 2, 3, 4, 6, 8, 9]
target = 10
left = 0
right = len(arr)-1
while left <= right:

    a = arr[right]+arr[left]

    if a == target:
        print(left,right)
        break

    elif a < target:
        left+=1

    else:
        right-=1

#2 pointers (only the first 5 positions matter.)
arr = [1, 2, 2, 3, 3, 4, 5, 5]
slow = 0

for fast in range(len(arr)):

    if arr[slow] != arr[fast]:
        slow += 1
        arr[slow] = arr[fast]

print(slow + 1)
print(arr)

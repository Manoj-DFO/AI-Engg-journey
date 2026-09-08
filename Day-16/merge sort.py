#To merge 2 sorted array
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged = []

arr1_pointer = 0
arr2_pointer = 0

while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):

    if arr1[arr1_pointer] < arr2[arr2_pointer]:
        merged.append(arr1[arr1_pointer])
        arr1_pointer += 1
    elif arr1[arr1_pointer] > arr2[arr2_pointer]:
        merged.append(arr2[arr2_pointer])
        arr2_pointer += 1

while arr1_pointer < len(arr1):
    merged.append(arr1[arr1_pointer])
    arr1_pointer += 1

while arr2_pointer < len(arr2):
    merged.append(arr2[arr2_pointer])
    arr2_pointer += 1

print(merged)





def merge(a,b):

    i = 0
    j = 0
    lt = []

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            lt.append(a[i])
            i += 1

        else:
            lt.append(b[j])
            j += 1

    while i < len(a):
        lt.append(a[i])
        i += 1

    while j < len(b):
        lt.append(b[j])
        j += 1

    return lt



def divide(arr):

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = divide(left)
    right = divide(right)

    return merge(left, right)




arr = [8, 3, 5, 4, 7, 6, 1, 2, 3, 7]

result = divide(arr)

print(result)
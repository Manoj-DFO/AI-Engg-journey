def permute(arr, start):

    if start == len(arr):
        print(arr)
        return

    for i in range(start, len(arr)):

        # MAKE CHOICE
        arr[start], arr[i] = arr[i], arr[start]
        print(i,start)

        # CONTINUE
        permute(arr, start + 1)
        print(i,start)
        # UNDO CHOICE
        arr[start], arr[i] = arr[i], arr[start]

arr=[1,3,4]
permute(arr,0)
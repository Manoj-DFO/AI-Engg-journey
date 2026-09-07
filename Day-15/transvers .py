#2nd largest number
arr = [12, 5, 8, 20, 3, 15]
a = arr[0]
s = None
for i in range(len(arr)):
    if arr[i] > a:
        s = a
        a = arr[i]
    elif s == None or arr[i] > s and arr[i] != a:
        s = arr[i]

print(s)
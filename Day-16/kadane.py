arr = [5, -3, 4, -8, 2, 7, -1, 3]

current = arr[0]
best = arr[0]
lt = []

for i in range(1,len(arr)):
    #current = max(arr[i], current + arr[i])
    if current < 0:
        current = 0
        start = i
    current += arr[i] 
    
    best = max(best, current)


print(best)
print(arr[start:i+1])
arr = [5, -3, 4, -8, 2, 7, -1, 3]

current = arr[0]
best = arr[0]

start = 0
best_start = 0
best_end = 0

for i in range(1, len(arr)):

    if arr[i] > current + arr[i]:
        start = i

    current = max(arr[i], current + arr[i])

    if current > best:
        best = current
        best_start = start
        best_end = i

print("Maximum sum:", best)
print("Subarray:", arr[best_start:best_end + 1])
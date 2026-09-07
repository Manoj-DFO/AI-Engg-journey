arr = [4, 2, 7, 1, 8, 3]
k = 3

sum_window = sum(arr[:k])
print(sum_window)
max_window = sum_window

for i in range(len(arr)-3):

    max_window=max(max_window , sum_window)
    sum_window = sum_window - arr[i] +arr[i+k]

print(max_window)
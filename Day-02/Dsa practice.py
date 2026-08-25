#sliding window 
arr = [1, 12, -5, -6, 50, 3]
k = 4
win_sum=arr[0]+arr[1]+arr[2]+arr[3]
max=win_sum                                    #maximum average
for i in range(len(arr)-k):
    win_sum=max-arr[i]+arr[i+k]
    if win_sum > max:
        max=win_sum
print(max/k)


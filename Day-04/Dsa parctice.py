#kadane's algorithm
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum=arr[0]
cur_sum = arr[0]
for i in range(len(arr)-1):
    cur_sum=max(cur_sum+arr[i] , arr[i])
    sum=max(sum,cur_sum)
print(sum)
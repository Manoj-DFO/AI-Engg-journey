#sliding window for variable size
arr = [4, 2, 7, 1, 8, 3]
k = 3

sum_window = sum(arr[:k])
print(sum_window)
max_window = sum_window

for i in range(len(arr)-3):

    sum_window = sum_window - arr[i] +arr[i+k]
    max_window = max(max_window , sum_window)

print(max_window)



#sliding window for variable size
arr = [2, 3, 1, 2, 4, 3]
target = 7

left=0
sum=0
min_len=10000000000

for right in range (len(arr)):

    sum = sum + arr[right]

    while sum >= target:

        len_arr=(right+1)-left
        min_len=min(min_len,len_arr)
        sum=sum-arr[left]
        left+=1
        
print(min_len)
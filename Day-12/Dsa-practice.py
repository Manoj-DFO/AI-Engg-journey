#2 pointers
arr = [1, 2, 3, 4, 6, 8, 10, 12]
target = 14
left=0
right=len(arr)-1
while left < right:
    if arr[left]+arr[right]==target:
        print(left,right)
        break
    elif arr[left]+arr[right]>target:
        right-=1
    elif arr[left]+arr[right]<target:
        left+=1

#sliding window
arr = [4, 2, 7, 1, 8, 3, 6, 5]
k = 3
window=sum(arr[:k])
wmax=window
for i in range(len(arr)-k):
    window=window-arr[i]+arr[i+k]
    wmax=max(window,wmax)
print(wmax)

#sliding window with variable size
arr = [2, 3, 1, 2, 4, 3]
target = 7
left=0
right=1
a=0
sum=0
for i in range(len(arr)-1):
    sum=sum+arr[left]+arr[right]
    if sum == target:
        if len(sum)>len(a):
            sum=sum-arr[left]
            a=sum
            left=left+1
    elif sum < target:
        right=right+1
    elif sum > target:
        left-=1
print(a)
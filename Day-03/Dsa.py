#reverse an array using 2 pointers
arr = [1, 2, 3, 4, 5 ,6]
left=0
right=len(arr)-1
while left <= right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
print(arr)



#sum=target using 2 pointers
arr = [1, 2, 3, 4, 5 ,6]
target=10
left=0
right=len(arr)-1
while left <= right:
        if arr[left]+arr[right]==target:
            print(left,right)
            break
        elif arr[left]+arr[right]<target:
            left=left+1
        else:
            right=right-1


arr = [2, 1, 5, 1, 3, 2]
k = 3
win_sum=arr[0]+arr[1]+arr[2]
max=win_sum
for i in range(len(arr)-k):
      win_sum=win_sum-arr[i]+arr[i+k]
      if win_sum > max:
            max=win_sum
print(max)



#sliding window to find minimum length of subarray whos sum is target
arr = [2, 1, 5, 2, 3, 2]
target = 7
min_length=float('inf')
sum=0
left=0
for i in range(len(arr)):
    sum=sum+arr[i] 
    while sum >= target:
        length = i - left + 1
        min_length = min(min_length, length)
        sum=sum-arr[left] 
        left=left+1
print(min_length)



#basic perfix sum
arr = [2, 4, 1, 5, 3]
prefix = [0]
for x in arr:
    prefix.append(prefix[-1] + x)
print(prefix)
print(prefix[4]-prefix[2]) #sum of index 2 and 3 = sum(2,3)



#leetcode problem
class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        count=0
        left=0
        a=''
        for i in range(len(s)):
            if s[i]=='1':
                count=count+1
            while count == k :
                c=s[left:i+1]
                if a == "" or len(c) < len(a) or (len(c) == len(a) and c < a):
                    a = c
                if s[left] == '1':
                    count=count-1
                left+=1
        return a
a=Solution()
s='100011001'


arr = [4, 6, -5, 9, 7, 5, -8]
n = 3

def largest(arr, n):

    window = sum(arr[:n])
    max_win = window

    for i in range(len(arr) - n):

        window = max_win - arr[i] + arr[i+n]
        max_win = max(max_win, window)

    return max_win

print(largest(arr, n))


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxarr(nums):

    tot = 0
    maxi = 0

    left = 0
    max_left = 0
    max_right = 0

    for i in range(len(nums)):

        if tot < 0:
            left = i
            tot = 0

        tot += nums[i]

        if tot > maxi:
            maxi = tot
            max_left = left
            max_right = i

    return maxi, nums[max_left:max_right + 1]


print(maxarr(nums))

#stair case
class Solution(object):
    def climbStairs(self, n):
        
        prev1 = 1
        prev2 = 1

        for i in range(2, n+1):

            current = prev1 + prev2

            prev2 = prev1
            prev1 = current

        return prev1
#3550. Smallest Index With Digit Sum Equal to Index
class Solution(object):
    def smallestIndex(self, nums):
        
        for i in range(len(nums)):

            n = sum(map(int, str(nums[i])))

            if n == i:
                return i

        else:
            return -1
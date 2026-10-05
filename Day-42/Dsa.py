class Solution(object):
    def majorityElement(self, nums):
        
        lt = []
        dit = {}

        for i, n in enumerate(nums):

            if n in dit:

                dit[n] += 1

            else:

                dit[n] = 1

        for m in dit:

            if dit[m] > (len(nums) // 3):

                lt.append(m)

        return lt




nums = [-2, 1, 2, 2, -2, 1, -2]



#amximum product of subarray
class Solution:
    def maxProduct(self, nums):

        maximum = nums[0]
        c_max = nums[0]
        c_min = nums[0]

        for i in range(1,len(nums)):

            n = nums[i]

            if n < 0:

                c_max, c_min = c_min, c_max

            c_max = max(n, n*c_max)
            c_min = min(n, n*c_min)

            maximum = max(maximum, c_max)

        return maximum
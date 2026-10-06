#75. Sort Colors
class Solution(object):
    def sortColors(self, nums):
                
        left = 0
        right = len(nums) - 1
        current = 0

        while current <= right:

            if nums[current] == 0:

                nums[left], nums[current] = nums[current], nums[left]

                current += 1
                left += 1

            elif nums[current] == 1:

                current += 1

            else:

                nums[right], nums[current] = nums[current], nums[right]

                right -= 1

        return nums



#15. 3Sum
class Solution(object):
    def threeSum(self, nums):

        lt = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum0 = nums[i] + nums[j] + nums[k]

                if sum0 > 0:
                    k -= 1

                elif sum0 < 0:
                    j += 1

                else:
                    lt.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and  j < k:
                        j += 1

        return lt



#31. Next Permutation
class Solution(object):
    def nextPermutation(self, nums):
        
        i = len(nums) - 1

        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i == 0:
            nums.reverse()

            return

        j = len(nums) - 1

        while j >= i and nums[j] <= nums[i-1]:
            j -= 1

        nums[i-1], nums[j] = nums[j], nums[i-1]

        nums[i:] = reversed(nums[i:])
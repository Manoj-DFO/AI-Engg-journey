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
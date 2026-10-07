#4sum
class Solution:
    def fourSum(self, nums, target):

        result = []
        
        nums.sort()

        l = len(nums)

        for first in range(l-3):

            if first > 0 and nums[first] == nums[first - 1]:

                continue

            for second in range(first + 1, l-2):

                if second > first + 1 and nums[second] == nums[second - 1]:

                    continue

                pointer1 = second + 1
                pointer2 = len(nums) - 1

                while pointer1 < pointer2:

                    total = nums[first] + nums[second] + nums[pointer1] + nums[pointer2]


                    if total > target:

                        pointer2 -= 1

                    elif total < target:

                        pointer1 += 1

                    else:

                        result.append([nums[first], nums[second], nums[pointer1], nums[pointer2]])

                        while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 + 1]:
                            pointer1 += 1

                        while pointer1 < pointer2 and nums[pointer2] == nums[pointer2 - 1]:
                            pointer2 -= 1

                        pointer1 += 1
                        pointer2 -= 1

        return result    


#88. Merge Sorted Array

class Solution:
    def merge(self, nums1, m, nums2, n):

        first = m - 1
        second = n - 1
        last = m + n -1

        while second >= 0:

            if first >= 0 and nums1[first] > nums2[second]:

                nums1[last] = nums1[first]

                first -= 1

            else:

                nums1[last] = nums2[second]

                second -= 1

            last -= 1

        
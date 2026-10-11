#xor count
class Solution:
    def subarraysWithXorK(self, nums, k):

        count = 0
        xor = 0
        dit = {0: 1}

        for n in nums:

            xor ^= n
            target = xor ^ k

            if target in dit:

                count += dit[target]

            if xor in dit:

                dit[xor] += 1

            else:

                dit[xor] = 1

        return count


#peak element
class Solution:
    def findPeakElement(self, arr):

        low = 0
        high = len(arr) - 1

        while low < high:

            mid = (high + low) // 2

            if arr[mid] < arr[mid + 1]:

                low = mid + 1

            else:

                high = mid

        return low

#search in a rotated sorted array
class Solution:
    def search(self, nums, k):

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == k:

                return True

            if nums[mid] == nums[low] == nums[high]:

                low += 1
                high -= 1

            elif nums[low] <= nums[mid]:

                if nums[low] <= k < nums[mid]:

                    high = mid - 1

                else:

                    low = mid + 1

            else:

                if nums[mid] < k <= nums[high]:

                    low = mid + 1

                else:

                    high = mid - 1

        return False


#540. Single Element in a Sorted Array
class Solution(object):
    def singleNonDuplicate(self, nums):
        
        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            if mid % 2 == 1:

                mid -= 1

            if nums[mid] == nums[mid + 1]:

                low = mid + 2

            else:

                high = mid

        return nums[low]
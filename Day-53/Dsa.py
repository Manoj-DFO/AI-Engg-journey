#Count Occurrences in a Sorted Array
class Solution:
    def countOccurrences(self, nums, target):

        ans1 = -1
        ans2 = -1

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:

                ans1 = mid
                high = mid - 1

            else:

                if nums[mid] < target:

                    low = mid + 1

                else:

                    high = mid - 1

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:

                ans2 = mid
                low = mid + 1

            else:

                if nums[mid] > target:

                    high = mid - 1

                else:

                    low = mid + 1

        if ans1 == -1:

            return 0

        return (ans2 - ans1) + 1



#find a smallest divisor
class Solution(object):
    def smallestDivisor(self, nums, threshold):

        def divisor(num):

            a = sum((n + num - 1)// num for n in nums)

            return a

        low = 1
        high = max(nums)

        ans = high

        while low <= high:

            mid = (low + high) // 2

            if divisor(mid) <= threshold:

                ans = mid
                high = mid - 1

            else:

                low = mid + 1

        return ans

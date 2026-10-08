#42. Trapping Rain Water
class Solution:
    def trap(self, height):

        left = 0
        right = len(height)  - 1

        left_min = 0
        right_min = 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:

                if left_min < height[left]:

                    left_min = height[left]

                else:

                    total_water += left_min - height[left]

                left += 1

            else:

                if right_min < height[right]:

                    right_min = height[right]

                else:

                    total_water += right_min - height[right]

                right -= 1

        return total_water


#97. Longest Consecutive Sequence in an Array
class Solution:
    def longestConsecutive(self, nums):

        numbers = set(nums)
        maximum = 0

        for n in numbers:

            if n - 1 in numbers:

                continue

            length = 1
            nex = n + 1

            while nex in numbers:

                nex += 1
                length += 1

            maximum = max(length, maximum)

        return maximum
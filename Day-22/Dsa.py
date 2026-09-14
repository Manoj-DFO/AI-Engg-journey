class Solution(object):
    def maxSubArray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = arr[0]
        best = arr[0]

        start = 0
        best_start = 0
        best_end = 0

        for i in range(1, len(arr)):

            if arr[i] > current + arr[i]:
                start = i

            current = max(arr[i], current + arr[i])

            if current > best:
                best = current

        return best

nums = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
print(a.maxSubArray(nums))
#20. Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in '({[':
                stack.append(i)

            else:
                if not stack or stack[-1] != pairs[i]:
                    return False

                stack.pop()

        return len(stack) == 0



#
nums1 = [2,4,1]
nums2 = [1,2,3,4]
maxi = nums2[-1]
dit = {}

for i in range(len(nums2)-1, -1, -1):
    
    if i == len(nums2) - 1 :
        dit[nums2[i]] = -1

    elif nums2[i] > maxi:
        maxi = nums2[i] 

        dit[nums2[i]] = maxi

    elif nums2[i] == maxi:
        dit[nums2[i]] = -1

    else:
        dit[nums2[i]] = maxi

highest = [dit[x] for x in nums1]
print(highest)
    
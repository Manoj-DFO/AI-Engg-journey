#largest odd number
class Solution(object):
    def largeOddNum(self, num):

        for i in range(len(num) - 1, -1, -1):

            if int(num[i]) % 2 != 0:

                    return num[:i+1].lstrip('0')

        return ''

#largest common prefix
class Solution:  
    def longestCommonPrefix(self, strs):

        prefix = strs[0]

        for s in strs[1:]:

            i = 0

            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:

                i += 1

            prefix = prefix[:i]

            if prefix == "":

                return ""

        return prefix
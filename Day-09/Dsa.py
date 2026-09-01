class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        dit={}
        maxlen=0
        for right ,c in enumerate(s):
            if c in dit:
                left = max(left, dit[c] + 1)
            dit[c]=right
            length=right-left+1
            maxlen=max(length,maxlen)
        return maxlen
s = "abcabcbb"
a=Solution()
print(a.lengthOfLongestSubstring(s))
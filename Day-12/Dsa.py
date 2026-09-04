#Longest Palindromic Substring(Brute Force)
# class Solution(object):
#     def longestPalindrome(self, s):
#         c=None
#         for i in range(len(s)):
#             b=''
#             a=''
#             for i in range(len(s)):
#                 a=a+s[i]
#                 b=s[i]+b
#                 if a == b:
#                     if len(a)>len(c):
#                         c=a
#         return c

# s = "babad"
# x=Solution()
# print(x.longestPalindrome(s))

#Longest Palindromic Substring(optimized)
class Solution(object):
    def longestPalindrome(self, s):
        c=''
        for i in range(len(s)):
            left=i
            right=i
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left=left-1
                right=right+1
            palindrome=s[left+1:right]
            if len(palindrome)>len(c):
                c=palindrome
            left=i
            right=i+1
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left=left-1
                right=right+1
            palindrome=s[left+1:right]
            if len(palindrome)>len(c):
                c=palindrome
        return c
s = "cbbd"
x=Solution()
print(x.longestPalindrome(s))
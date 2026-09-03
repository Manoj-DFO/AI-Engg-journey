class Solution(object):
    def isPalindrome(self, x):
        rev=''
        n=str(x)
        for i in str(x):
            rev=i+rev
        if rev == n:
            a=True
        else:
            a=False
        return a
x=121
a=Solution()
print(a.isPalindrome(x))
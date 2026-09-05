#Given a signed 32-bit integer x, return x with its digits reversed.
#If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
class Solution(object):
    def reverse(self, x):
        rev=0
        b=x
        if x < 0:
            x=-x
        while x > 0:     #str(x)[::-1]
            a=x%10
            rev=rev*10+a
            x=x//10
        if b < 0:
            rev=-rev
        if rev > 2147483647 or rev < -2147483648:
            return 0
        return rev
x=-896
y=Solution()
print(y.reverse(x))
class Solution(object):
    def myAtoi(self, s):

        i = 0
        n = len(s)
        sign = 1
        ans = 0

        if len(s) == 1 and s.isdigit():
            return int(s)

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            if ans * sign <= -2**31:
                return -2**31
            elif ans * sign >= ((2**31) - 1):
                return ((2**31) - 1)
            i += 1

        return ans * sign
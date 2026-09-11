# Unique 3-Digit Even Numbers
#You are given an array of digits called digits. Your task is to determine the number of distinct three-digit
#  even numbers that can be formed using these digits.
#Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

class Solution(object):
    def totalNumbers(self, digits):
        count = 0
        number = set()

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if j == i:
                    continue

                for k in range(len(digits)):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    number.add(num)

        return len(number)
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows > len(s):
            return s

        rows = ['']*numRows
        row = 0
        direction = 1

        for i in s:

            rows[row] += i

            if row == 0:
                direction = 1

            elif row == numRows - 1:
                direction = -1

            row = row + direction 

        return ''.join(rows)
lt = [['j','u','i','o','k'],['j','u','i','o','k'],['j','u','i','o','k']]
a = ''.join(''.join(r) for r in lt)
print(a)
m = 3
lt2 = ['']*m
lt2[1] += 'a'
lt2[1] += 'b'
lt2[1] += 'c'

lt2[2] += 'd'
lt2[2] += 'e'
lt2[2] += 'f'
lt2[2] += 'g'

lt2[0] += 'h'
lt2[0] += 'i'
lt2[0] += 'j'
lt2[0] += 'k'
lt2[0] += 'l'

print(lt2)
print(''.join(lt2))


#dsa
#6. Zigzag Conversion
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

#best time to buy and sell
def stock(lt):

    buy = lt[0]
    profit = 0

    for i in range(1,len(lt)):

        if lt[i] < buy:
            buy = lt[i]

        elif (lt[i] - profit) > profit:
            profit = lt[i] - profit

    return profit

lt = [7,1,5,3,6,4]
print(stock(lt))

#
nums = [-1,1,0,-3,3]
def pro(nums):
    product = 1
    zero = 0

    for i in nums:
        if i != 0:
            product *= i 
        elif i == 0:
            zero += 1

    if zero > 1:
        res = [0 for _ in range(len(nums))]

    elif zero == 0:
        res = [product/i for i in nums]

    else:
        res = [0 if i != 0 else product for i in nums]

    return res

print(pro(nums))

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxarr(nums):
    tot = 0
    maxi = 0

    for i in range (len(nums)):

        if tot < 0:
            left = i
            tot = 0
        tot += nums[i]
        maxi = max(maxi, tot)
    return maxi

print(maxarr(nums))

#1. 2sum
nums = [2,7,11,15]
target = 91

def sum2(nums, target):
    dit = {}
    for i,n in enumerate(nums):
        needed = target - n

        if needed in dit:
            return (dit[needed],i)

        dit[n] = i
    return -1

print(sum2(nums, target))


#2. Add Two Numbers
class Node():
    def __init__(self, val, next = None):
        self.val = val 
        self.next = next

node1 = Node(2)
node2 = Node(4)
node3 = Node(3)

node1.next = node2
node2.next =  node2

node4 = Node(7)
node5 = Node(0)
node6 = Node(8)

node4.next = node5
node5.next = node6

def sum(l1, l2):
    dummy = Node(0)
    result = dummy

    while l1 or l2 or carry:

        total = carry

        if l1:
            total += l1.val
            l1 = l1.next

        if l2:
            total += l2.val
            l2 = l2.next

        carry = total // 10
        dummy.next = Node(carry % 10)
        dummy = dummy.next

    return result.next


#3. Longest Substring Without Repeating Characters

s = "abcabcbb"
class Solution():
    def lsub(self, s):

        left = 0
        dit = {}
        length = 0

        for i,ch in enumerate(s):

            if ch in dit:
                left = max(i, dit[ch])

            dit[ch] = i

            length = max(length, (i - left)+1)

        return length

a = Solution()
print(a.lsub(s))

#5. Longest Palindromic Substring
def pal(s):

    mid = len(s) // 2
    c =''
    count = 0

    for i in range(len(s)):

        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1

        pal = s[left+1: right]

        if len(pal) > len(c):
            c = pal

        left = i
        right = i + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1

        pal = s[left+1: right+1]

        if len(pal) > len(c):
            c = pal

    return count

s = "babad"
print(pal(s))


#6. Zigzag Conversion
s = "PAYPALISHIRING"
numRows = 3

def zigzag(s, numRow):

    if len(s) == 1 or numRow > len(s):
        return s

    lt = ['']*numRow
    row = 0
    direction = 1

    for c in s:

        lt[row] = lt[row] + c

        if row == 0:
            direction = 1

        elif row == numRow - 1:
            direction = -1

        row  += direction

    return ''.join(lt)

print(zigzag(s, numRows))


#7. Reverse Integer
n = 120

sign = 1
rev = 0

if n < 0:
    sign = -1
    n = -n

while n > 0:

    a = n % 10
    rev = rev*10 + a

    n = n // 10

print(sign*rev)


#8. String to Integer (atoi)
def myAtoi(s):

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

s = "1337c0d3"
print(myAtoi(s))

#12. Integer to Roman
num = 1994

def itor(num):

    res = ''

    num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }

    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:

        while n <= num:
            res += num_map[n]
            num -= n

    return res

print(itor(num))
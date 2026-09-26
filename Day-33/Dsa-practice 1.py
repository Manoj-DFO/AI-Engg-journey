#2 sum
nums = [2,7,11,15]
target = 9
dit = {}
def sum(nums,traget):
    for i,n in enumerate(nums):

        needed = target - n

        if needed in dit:
            return [dit[needed],i]

        dit[n] = i

print(sum(nums,target))

#Longest Substring Without Repeating Characters
s = "abcabcbb"

def long(s):

    left = 0
    dit = {}
    max_len = 0

    for i in range(len(s)):

        if s[i] in dit:
            left = max(left,dit[s[i]]+1)

        dit[s[i]] = i

        max_len = max(max_len,len(s[left:i+1]))

    return max_len

print(long(s))

#5. Longest Palindromic Substring
s = "babad"

def palindrome(s):

    c = 0

    for i in range(len(s)):
        left = i
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        pal = s[left+1 : right]
        lpal = len(pal)
        c = max(lpal,c)

        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        pal = s[left+1 : right]
        lpal = len(pal)
        c = max(lpal,c)

    return c,pal

print(palindrome(s))

#Reverse Integer
x = -123

def rev(x):
    sign = 1
    revs = 0
    if x < 0:
        sign = -1
        x = x*sign

    while x > 0:
        a = x % 10
        revs = revs*10 + a

        x = x // 10

    if revs > 2147483647 or revs < -2147483648:
        return 0

    return sign*revs

print(rev(x))

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

s = "-1337c0d3"
print(myAtoi(s))

#palindrome
x = 10
def isPalindrome(x):
    rev=''
    for i in str(x):
        rev=i+rev
    return rev == str(x)

print(isPalindrome(s))

#integer to roman
num = 1994
def itr(num):
    num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
    r = ''
    for i in [1000,900,500,400,100,90,50,40,10,9,5,4]:
        while num >= i:
            r = r + num_map[i]
            num = num - i

    return r

print(itr(num))

#roman to integer
s = "MCMXCIV"
def rti(s):
    num_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    num = 0
    for i in range(len(s)-1):

        if num_map[s[i]] < num_map[s[i+1]]:
            num = num - num_map[s[i]]

        else:
            num = num + num_map[s[i]]

    num = num + num_map[s[-1]]
    return num

print(rti(s))

#longest common prefix
strs = ["flower","flow","flight"]
def lcp(strs):
    prefix = strs[0]

    for i in range (1,len(strs)):

        j = 0
        while j < len(strs[i]) and j < len(prefix) and prefix[j] == strs[i][j]:
            j += 1

        prefix = prefix[:j]

        if prefix == '':
            return ''

    return prefix

print(lcp(strs))

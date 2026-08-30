def sumodig(n):
    sum=0
    while n>0:
        a=n%10
        sum=sum+a
        n=n//10
    return sum
print(sumodig(5672))

def revs(s1):
    if len(s1)==0:
        return ''
    return revs(s1[1:])+s1[0]
s1='manoj kumar'
print(revs(s1))

def palindrome(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    return palindrome(s,start+1,end-1)
s='ana'
if palindrome(s,0,len(s)-1):
    print('is palindrome')
else:
    print('not a palindrome')
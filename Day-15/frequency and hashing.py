#frequency pattern

s = "aabbccddeefggh"
dit =  {}

for i in range(len(s)):

    if s[i] in dit:
        dit[s[i]]=dit[s[i]]+1

    else:
        dit[s[i]]=1

for ch in s:
    if dit[ch] == 1:
        print(ch)
        break


#Hashing pattern
def sum(arr,target):
    seen = {}
    for i ,n in enumerate(arr):
        needed = target - n

        if needed in seen:
            return seen[needed],i

        seen[n] = i
        
arr = [2, 7, 11, 15]
target = 9

print(sum(arr,target))


#contain any num twice
arr = [4, 2, 7, 11, 9, 5]
for i in range(len(arr)):

    if arr[i] in dit:
        print('True')
        break

    else:
        dit[arr[i]]=1

else:
    print('False')
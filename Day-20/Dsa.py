s = "MCMXCIV"

num_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

num = 0   
i = 0 

while i < len(s):

    if i+1 < len(s) and num_map[s[i]] < num_map[s[i+1]]:
        num = num + (num_map[s[i+1]] - num_map[s[i]])
        i = i + 2

    else:
        num = num_map[s[i]] + num
        i = i + 1

print(num)


#or

s = "MCMXCIV"

num_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

num = 0   
i = 0 

for i in range(len(s)):

    if i+1 < len(s) and num_map[s[i]] < num_map[s[i+1]]:
        
        num = num - num_map[s[i]]

    else:
        num = num_map[s[i]] + num

print(num)
with open('Day-17/data.txt') as f:
    data = f.read()

print(data)
word = data.split()
for i in word:
    print(i)
arr = [3, 2, 5, 1, 6, 4]
prefix = [0]
prefix_cal=0

for i in range(len(arr)):

    prefix_cal = prefix_cal + arr[i]
    prefix.append(prefix_cal)

print(prefix)

queries = [(1, 3), (2, 5), (0, 4)]

for j in queries:
    sum = prefix[j[1]+1] - prefix[j[0]]
    print(sum)
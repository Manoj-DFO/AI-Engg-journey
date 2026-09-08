arr = [1, 2, 3, -2, 5, 1]
target = 6

prefix_sum = 0
count = 0

dit = {0: 1}

for x in arr:
    prefix_sum += x

    needed = prefix_sum - target

    if needed in dit:
        count += dit[needed]

    dit[prefix_sum] = dit.get(prefix_sum, 0) + 1

print(count)
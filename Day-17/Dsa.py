#median of 2 sorted array
def findMedianSortedArrays(num1, num2):
         
    a = 0
    b = 0
    lt = []

    l1 = len(num1)
    l2 = len(num2)

    while a < l1 and b < l2:

        if num1[a] < num2[b]:
            lt.append(num1[a])
            a += 1
        else:
            lt.append(num2[b])
            b = +1

    while a < l1:

        lt.append(num1[a])
        a += 1

    while b < l2:

        lt.append(num2[b])
        b += 1

    print(lt)
    c = 0
    d = len(lt) - 1

    if len(lt) % 2 != 0:
        mid =  (c + d) // 2
        return lt[mid]


    else:
        mid = (c + d) // 2
        return (lt[mid] + lt[mid + 1]) / 2

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1,nums2))




#common prefix
strs = ["flower", "flow", "flight"]

best_str = strs[0]

for st in strs[1:]:

    i = 0

    while i < len(best_str) and i < len(st) and best_str[i] == st[i]:
        i += 1

    best_str = best_str[:i]

print(best_str)
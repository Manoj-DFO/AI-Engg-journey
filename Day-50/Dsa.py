#composite and prime number
from math import sqrt

n = int(input("Enter n: "))

prime = []
composite = []

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime.append(num)
    else:
        composite.append(num)

print("Prime numbers:", prime)
print("Composite numbers:", composite)



#Find
arr = [1,2,4,7]
target = 6

def find(arr,target):

    low = 0
    high = len(arr) - 1

    ans = len(arr)

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] >= target:
            ans = mid
            high = mid - 1

        else:

            low = mid + 1
            ans = mid

    return ans

print(find(arr,target))


#optimized prime number count
class Solution:
    def primeUptoN(self, n):

        countprime = 0

        for num in range(2, n+1):
            
            count = 0

            for i in range(2, int(num ** 0.5) + 1):

                if num % i == 0:

                    count += 1
                    
                    break

            if count == 0:

                countprime += 1 

        return countprime
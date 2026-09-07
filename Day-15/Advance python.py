#Iterator
numbers = [10, 20]
it = iter(numbers)
print(next(it))
print(iter(numbers))
print(next(it))
# print(next(it))


#generator
def numbers():
    yield from [1, 2, 3, 4]
#both are same
def numbers1():
    for x in [1, 2, 3, 4]:
        yield x

print(next(numbers()))
print(next(numbers1()))


gen = (x * 2 for x in range(5))  #For list comprehension we will use [] but for generator we use ()
print(next(gen))
print(next(gen))


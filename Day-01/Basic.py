name = "Manoj"
age = 20
height = 1.80
student = True
                                   
print(age)
print(height)
print(student)


n=int(input('enter a number'))
a=0
while n>0:
    a=a*10+n%10                            #reverese of an number using while loop
    n=n//10
print(f'reverse of a number is {a}')
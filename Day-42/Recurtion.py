def dis(n, a = 1):

    if a > n:
        return

    print(a)

    dis(n, a + 1)

dis(5)

print('\n')

def disp(n):

    if n == 0:
        return

    print(n)

    disp(n - 1)

disp(5)


#backtacking to print n to 1

print('\n')
def displ(n):

    if n == 0:
        return

    print(n)

    displ(n - 1)

displ(5)

#backtacking to print n to 1

print('\n')
def displa(n):

    if n <= 0:
        return

    displa(n-1)

    print(n)

displa(6)
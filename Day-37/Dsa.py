#stack
b = "([{}])"

def braces(b):

    stack = []
    brackets = {']':'[', '}':'{', ')':'('}

    for i in b:

        if b in '{[(':
            stack.append(i)

        else:

            if not stack:
                return False

            if stack[-1] != brackets[i]:
                return False

            stack.pop()

    return len(stack) == 0

print(braces(b))
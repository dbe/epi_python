from test_framework import generic_test


def evaluate(e):
    e = e.split(',')
    stack = []

    for c in e:
        if(c == '+'):
            stack.append(stack.pop() + stack.pop())
        elif(c == '-'):
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif(c == '*'):
            stack.append(stack.pop() * stack.pop())
        elif(c == '/'):
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
        else:
            stack.append(int(c))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))

import sys
stack_list = []
def push_X(X):
    stack_list.append(X)
    return stack_list
def pop():
    if len(stack_list) == 0:
        return -1
    else:
        return stack_list.pop(-1)
def size():
    return len(stack_list)
def empty():
    if len(stack_list) == 0:
        return 1
    else:
        return 0 
def top():
    if len(stack_list) == 0:
        return -1
    else:
        return stack_list[-1]
T = int(sys.stdin.readline())
for i in range(T):
    C = sys.stdin.readline().strip()
    if 'push' in C:
        push_list = C.split()
        X = int(push_list[1])
        push_X(X)
    elif C == 'pop':
        print(pop())
    elif C == 'size':
        print(size())
    elif C == 'empty':
        print(empty())
    elif C == 'top':
        print(top())

import sys
from collections import deque
def push_X(X):
    queue.append(X)
    return queue
def pop():
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()
def size():
    return len(queue)
def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0
def front():
    if len(queue) == 0:
        return -1
    else:
        return queue[0]
def back():
    if len(queue) == 0:
        return -1
    else:
        return queue[-1]
N = int(input())
queue = deque()
for i in range(N):
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
        elif C == 'front':
            print(front())
        elif C == 'back':
            print(back())

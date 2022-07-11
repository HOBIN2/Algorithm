import sys
T = int(input())
for i in range(T):
    VPS = sys.stdin.readline().strip()
    VPS = list(VPS)
    count = 0
    for i in VPS:
        if i == '(':
            count += 1
        elif i == ')': 
            count -= 1
        if count < 0:
            print("NO")
            break
    if count == 0:
        print('YES')
    elif count > 0:
        print('NO')
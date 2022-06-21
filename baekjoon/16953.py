N, K = map(int, input().split())
count = 1
while K != N:
    if len(str(K)) >= 2 and str(K)[-1] == '1':
        K = int(str(K)[:-1])
    elif K % 2 == 0:
        K = int(K / 2)
    else:
        count = -1
        break
    count += 1
print(count)
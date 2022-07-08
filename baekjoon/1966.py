T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    importance = list(map(int,input().split()))
    count = 0
    while True:
        max_imp = max(importance)
        out_imp = importance.pop(0)
        M -= 1
        if out_imp == max_imp:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            importance.append(out_imp)
            if M < 0:
                M = len(importance) - 1

T = int(input())
for x in range(T):
    H = int(input())        
    W = int(input())
    W_num = list(range(1,W+1))
    for i in range(H-1):
        count = 0
        for j in len(W_num):
            count += W_num[j]
            W_num[j] = count
    print(sum(W_num))
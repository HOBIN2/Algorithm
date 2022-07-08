N = int(input())
W_H_list = []
for i in range(N):
    W, H = map(int,input().split())
    W_H_list.append((W, H))

for i in W_H_list:
    rank = 1
    for j in W_H_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')
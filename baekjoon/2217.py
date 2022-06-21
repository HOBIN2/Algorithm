from audioop import reverse


def up():
    k = []
    w_list.sort(reverse=True)
    for i in range(N):
        k.append(w_list[i] * (i+1))
    return max(k)
N = int(input())
w_list = []
for i in range(N):
    w_list.append(int(input()))
print(up())
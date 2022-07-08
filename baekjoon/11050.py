N, K = map(int,input().split())
A = 1
B = 1
for i in range(K):
    A *= (N-i)
    B *= (K-i)
print(int(A/B))
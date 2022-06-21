N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    graph[i] = list(map(int,input().split()))
print(graph)
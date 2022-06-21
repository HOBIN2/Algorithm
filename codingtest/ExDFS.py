graph = [[], [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6],
         [1, 7]]

visited = [False] * 9


def DFS(graph, n, visited):
    print(visited)  
    visited[n] = True
    print('{}번 노드 방문'.format(n))
    for i in graph[n]:
        if not visited[i]:
            DFS(graph, i, visited)


DFS(graph, 1, visited)

from collections import deque

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



graph = [[], [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6],
         [1, 7]]

visited = [False] * 9


def BFS(graph, n, visited):
    queue = deque([n])
    print(queue)
    visited[n] = True
    while queue:
        v = queue.popleft()
        print('{}번째 노드'.format(v))
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


BFS(graph, 1, visited)
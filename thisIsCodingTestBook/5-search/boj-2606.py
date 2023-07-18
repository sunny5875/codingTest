from collections import deque

n = int(input())
pair = int(input())

graph = [[] for _ in range(n) ]
visited = [0] * n # -1은 아직 안간거  1은 걸린거

for _ in range(pair):
    x,y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1) #반대로도 넣어줘야하는 거 잊지 말기!!


def bfs(a, visited, graph):
    q = deque([a])
    visited[a] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                bfs(i, visited, graph)
            visited[i] = 1
    

bfs(0, visited, graph)
result = 0
for i in range(n):
    if visited[i] == 1:
        result +=1
print(result-1)



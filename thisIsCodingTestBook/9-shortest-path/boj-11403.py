INF = int(1e9) 

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b] :
                graph[a][b] = 1

for g in graph:
    print(*g)
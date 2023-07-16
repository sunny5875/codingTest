n = int(input()) #명 수 
x, y  = map(int,  input().split()) #구해야 하는 사람 번호
m = int(input()) # 부모자식 관계 수
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b  = map(int,  input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

# def f(x):
#     global visited, graph, current_index
#     return graph[current_index][x] == 1 and visited[x] == False
# result = 0
# visited[x-1] = True
# current_index = x-1
# if x != y:
#     while current_index != y-1:
#         temp = list(filter(f, range(n)))
#         if len(temp) == 0:
#             result = -1
#             break
#         else:
#             current_index = temp[0]
#             visited[current_index] = True
#             result += 1
# print(result)
count = 0
def dfs(v, count):
    visited[v] = True
    if v == y:
        print(count)
        exit()
    for i in graph[v]:
        if not visited[i]:
            dfs(i, count + 1)

dfs(x, count)
print(-1)

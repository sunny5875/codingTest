
from collections import deque

m,n,h=map(int,input().split())
#봐야 할 토마토들
next = deque()
graph=[[] for _ in range(h)]

for i in range(h):
  for j in range(n):
    graph[i].append(list(map(int,input().split())))
    for k in range(m):
      if graph[i][j][k]==1:  #익은 토마토만 next에 넣기
        next.append((i,j,k))

#방향 벡터
dx=[0,1,0,-1,0,0]
dy=[1,0,-1,0,0,0]
dz=[0,0,0,0,1,-1]

#next에서 하나씩 꺼내 bfs 실행
#next가 빈다면 더이상 살펴봐야할 좌표가 없다는 뜻이므로 종료
#bfs로 6방향 살펴보며 조건에 맞으면 기존 graph값+1을 새로운 graph에 대입하고 next에 해당 좌표를 추가하는 함수
def bfs():
    global next
    while next:
        z,x,y = next.popleft()
        for i in range(6):   
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]  
            if (0<=nx<n and 0<=ny<m and 0<=nz<h) and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny]=graph[z][x][y]+1  
                next.append((nz,nx,ny))  
  
bfs()

#graph 체크하며 0이 있다면 flag를 false로 두고 -1를 출력, 아니라면 result 계산
flag = True
result=1
for z in range(h):
  for x in range(n):
    for y in range(m):
      if graph[z][x][y]==0:
        flag = False
      else:
        print(result, graph[z][x][y])
        result = max(result,graph[z][x][y])


if flag == True:
  print(result-1)
else:
  print(-1)
n, m = map(int, input().split())
x, y, direct = map(int, input().split())
map_list = []
for i in range(m):
    map_list.append((list(map(int, input().split()))))
# 가본
d = [[0] * n] * m

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]
    if d[nx][ny] == 0 and map_list[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)

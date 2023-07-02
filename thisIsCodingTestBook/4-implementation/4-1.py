n = int(input())
route_list = list(input().split())
# 방법 1
# current_index = [1, 1]
# for item in route_list:
#     if item == "L" and current_index[1] == 1:
#         continue
#     elif item == "R" and current_index[1] == n:
#         continue
#     elif item == "U" and current_index[0] == 1:
#         continue
#     elif item == "D" and current_index[0] == n:
#         continue
#     if item == "L":
#         current_index[1] -= 1
#     elif item == "R":
#         current_index[1] += 1
#     elif item == "U":
#         current_index[0] -= 1
#     else:
#         current_index[0] += 1
# print(current_index)
# 방법 2
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
for item in route_list:
    i = move_types.index(item)
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
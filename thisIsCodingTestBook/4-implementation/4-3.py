index = list(input())
col = ord(index[0]) - 97
row = int(index[1])

step_list = [(2,1), (-2,1), (2,-1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
count = 0
for step in step_list:
    next_row = row + step[0]
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1
print(count)

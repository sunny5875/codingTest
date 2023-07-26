n = int(input())

d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4
result = ""

for _ in range(n):
    num = int(input())
    for i in range(4, num+1):
        if d[i] == 0:
            d[i] = d[i-1] + d[i-2] + d[i-3] 

    result += ('%d\n') % (d[num])

print(result, end = '\n')
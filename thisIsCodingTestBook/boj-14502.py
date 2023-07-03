n, m = map(int, input().split())
num_list = [[0] * m] * n
for i in range(n):
    num_list[i] = list(map(int, input().split()))
print(num_list)

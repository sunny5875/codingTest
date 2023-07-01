n,a= map(int,input().split())
k = list()
for i in range(n):
    k.append(int(input()))
count = 0
k.sort(reverse=True)
for coin in k:
    count += (a // coin)
    a %= coin
print(count)
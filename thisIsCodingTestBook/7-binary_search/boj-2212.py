n = int(input())
k = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

if k >= n:
    print(0)
    exit()

dist = []
for i in range(1, n):
    dist.append(arr[i] - arr[i-1])

dist.sort(reverse=True)
# 내림차순으로 정렬한 후에 제일 차이가 큰 애들을 뺴주면 됨!
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))
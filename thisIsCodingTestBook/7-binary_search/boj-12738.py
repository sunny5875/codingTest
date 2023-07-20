from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

n = int(input())
arr = list(map(int, input().split()))

result = []

for i in arr:
    k = bisect_left(result, i) #자신이 들어갈 위치 k
    if len(result) <= k: #i가 가장 큰 숫자라면
        result.append(i)
    else:
        result[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(result))
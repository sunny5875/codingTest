#방식은 맞았는데 인덱스 계산이 어려웠음 
n = int(input())

arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

d_up = [1 for i in range(n)] # 가장 긴 증가하는 부분 수열
d_down = [1 for i in range(n)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            d_up[i] = max(d_up[i], d_up[j]+1) #현재최대값 vs 이전최대값 + 현재값
        if reverse_arr[i] > reverse_arr[j]:
            d_down[i] = max(d_down[i], d_down[j]+1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = d_up[i] + d_down[n-i-1] -1

print(max(result))
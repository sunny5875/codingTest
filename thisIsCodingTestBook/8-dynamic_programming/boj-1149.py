n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


for i in range(1,n): 
    #i가 0인 경우는 이미 채워져 있으니까 굳이 계산할 필요 없음. 
    # 여기서 0이면 arr[-1]이 되어서 값 틀어짐
    arr[i][0] += min(arr[i-1][1], arr[i-1][2]) 
    arr[i][1] += min(arr[i-1][0], arr[i-1][2]) 
    arr[i][2] += min(arr[i-1][1], arr[i-1][0])

print(min(arr[n-1])) 
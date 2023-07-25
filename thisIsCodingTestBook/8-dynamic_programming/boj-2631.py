
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

d = [1] * n

# d[1] = 0
# if arr[0] > arr[1]:
#     d[2] = 1
# for i in range(3, n-2):
#     filter = [x for x in arr[:i] if x > arr[i-1]]
#     print(i, filter)
#     if len(filter) == 1:
#         if filter[0] == arr[i-2]:
#             d[i] = d[i-2] + 1
#         else:
#             d[i] = d[i-1]
#     else:
#         d[i] = d[i-1] + 1 
#     print(d)

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j]+1) # boj-2631과 동일하게 부분수열 문제! arr[i]를 포함하면서 제일 긴 부분수열 궇하기

print(n - max(d)) #부분수열이 젤 큰 걸 고르면 나머지 정렬 안된 애들을 옮겨야 하니까 n- max(d)

#문제: n * m의 matrix를 받아서 행을 선택하고 그 행의 min값인 요소를 뽑는데 가장 max값을 구해라

n,m = map(int, input().split())
result = 0
for i in range(n):
  current_max = min(list(map(int,input().split())))
  # if result < current_max:
  #   result = current_max
  result = max(result, current_max)

print(result)

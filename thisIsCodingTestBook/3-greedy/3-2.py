#문제: n,m,k를 받고 n 길이의 배열을 받아 8개의 요소의 합의 max를 구하는데 단, 같은 인덱스를 연속해서 k번 초과 받을 수 없음
#예시 
# 5 8 3
# 2 4 5 4 6
# 답: 46
# 5 7 2
# 3 4 3 4 3
# 답: 28
n,m,k  = map(int, input().split())

n_list = list(map(int,input().split()))
# max = second_max = n_list[0]
# for item in n_list:
#   if item > max:
#     second_max = max
#     max = item
#   elif second_max < item < max:
#     second_max = item
#   elif item == max: #여기 예외처리를 해줘야함!! max랑 second_max가 같을 수 있으니까!
#     second_max = item
n_list.sort()
max = n_list[-1]
second_max = n_list[-2]
# print((max * k * (m // k)) + second_max * (m % k)) 이렇게 하면 안됨! m이 k의 배수일 때 성립되지 않음
max_count = (m // (k+1)) * k + (m % (k+1))
print((max * max_count) + (second_max * (m-max_count)))

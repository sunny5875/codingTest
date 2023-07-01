# n =int(input())
# chair_list = list(input())

# result = n
# i = 0
# while i < n-1:
#    if chair_list[i] == "L" and chair_list[i+1] == "L":
#         if i != n-2:
#             result -=1
#         if i == n-3 and chair_list[i+2] == "S":
#           result +=1
#         i+=1
#    i+=1
# print(result)

n = int(input())
m = input()
#왼쪽 기준으로 가질 수 있느냐를 계산
m = m.replace('S','*') 
m = m.replace('LL','*')
if n < len(m)+1: #맨끝에 오른쪽에도 주니까 그걸 고려, 단 사람수보다 컵홀더가 많으면 사람수를 리턴
  print(n)
else:
  print(len(m)+1)
   

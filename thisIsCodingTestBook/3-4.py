n,k = map(int,input().split())
count = 0
# while(n != 1):
#   if n % k == 0:
#     n /= k
#   else:
#     n -=1
#   count +=1
# print(count)

#1을 한꺼번에 빼서 좀 더 효율적으로 해보자!
while True:
  count1 = (n % k) #나눠지도록 나머지만큼 1을 빼줘야하니까 그만큼 계산
  count += count1
  n -= count1
  if n < k: #n이 k보다 작아지면 나눌 수 없으니까 break
   break 
  else:# 그제서야 나누기
    count +=1 
    n //= k

count += (n-1)  
print(count)

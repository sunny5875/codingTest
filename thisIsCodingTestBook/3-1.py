#거스름돈 N원을 500,100,50,10원을 이용해서 동전개수 몇개가 필요한지 계산- Greedy 

a= int(input())
count = 0
coin_types= [500,100,50,10]

for coin in coin_types:
    count += (a // coin) #python에서 몫 연산자는 //이래
    a %= coin 
print(count)

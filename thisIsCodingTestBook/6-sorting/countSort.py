array = [3,4,2,5,6,1,8,10]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1


for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
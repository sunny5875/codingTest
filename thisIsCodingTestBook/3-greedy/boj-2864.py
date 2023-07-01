n, m = input().split()
n = n.replace('6', '5')
m = m.replace('6', '5')
min = int(n) + int(m)

n = n.replace('5', '6')
m = m.replace('5', '6')
max = int(n) + int(m)
print(min, max)

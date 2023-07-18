# 기준 어려웠던 문제

r,c,k = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(3) ]

def execute_r():
    global arr
    new_graph = [] 

    for i in arr:
        elem = set(i) # 한 행의 원소만 추출
        dict = [] # (원소, 갯수) 를 담을 그래프
        new_row = [] # 새로운 행이 될 그래프
        for j in elem:
            if j!=0:
                cnt = i.count(j)
                dict.append((j,cnt))

        dict.sort(key=lambda x:(x[1],x[0]))

        for k in dict:
            new_row.append(k[0])
            new_row.append(k[1])

        new_row = new_row[:100] # 100개 제한
        new_graph.append(new_row)


    max_len = max(map(len,new_graph))

	# 빈 칸은 0만큼 채워준다.
    for i in range(len(new_graph)):
        while len(new_graph[i]) !=max_len:
            new_graph[i].append(0)

    arr = new_graph


for i in range(101):
    try: # out of range 문제가 일어날 수 있기 때문에 try catch
        if arr[r-1][c-1]==k:
            print(i)
            break
    except:
        pass

    if len(arr[0]) <= len(arr):
        execute_r()
    else:
        arr = list(map(list,zip(*arr)))
        execute_r()
        arr = list(map(list,zip(*arr)))

else:
    print(-1)
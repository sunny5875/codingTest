# from queue import PriorityQueue

# n = int(input())
# arr = list(map(int, input().split()))
# queue = PriorityQueue()
# result = 0


# for i in range(n):
#     num = arr[i] - i
#     # print("num : ", num)
#     # print("queue: ", queue)
#     if queue.not_empty and queue[0] > num:
#         queue.put(num)
#         result += queue[0] - num
#         queue.get()
#         # print("result: ", result)
#         queue.put(num)
#     else:
#         queue.put(num)

#     # print("queue: ", queue)
    
# print(result)
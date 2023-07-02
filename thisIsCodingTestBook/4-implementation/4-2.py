n = int(input())
# 방법 1
# hour = 0
# minute = 0
# second = 0
#
# count = 0
# while True:
#     if '3' in str(hour) or '3' in str(minute) or '3' in str(second):
#         count += 1
#     if second == 59:
#         second = 0
#         minute += 1
#     else:
#         second += 1
#     if minute == 60:
#         minute = 0
#         hour += 1
#     if hour == n and minute == 59 and second == 59:
#         if hour == 3:
#             count += 1
#         else:
#             break
# print(count)
# 방법 2
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
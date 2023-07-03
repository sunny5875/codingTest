t = int(input())
result = ''
for i in range(t):
    func = list(input())
    n = int(input())
    num_list = input().replace('[', '').replace(']',  '').split(',')
    if num_list == ['']:
        num_list = []
    reverse_flag = False
    error_flag = False
    for j in func:
        if j == 'R':
            reverse_flag = not reverse_flag
        else:
            if len(num_list) == 0:
                error_flag = True
                break
            else:
                if reverse_flag:
                    num_list.pop()
                else:
                    num_list.pop(0)
    if error_flag != True:
        if reverse_flag:
            num_list.reverse()
        result += '[' + (','.join(num_list)) + ']\n'
    else:
        result +='error\n'
print(result)

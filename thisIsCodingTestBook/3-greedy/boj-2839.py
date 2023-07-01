def solution(n):
    if n % 5 == 0:
        return n // 5
    else:
        for i in range((n // 5), -1, -1):
            if (n - 5 * i) % 3 == 0:
                return i + (n - 5 * i) // 3
        return -1
print(solution(int(input())))

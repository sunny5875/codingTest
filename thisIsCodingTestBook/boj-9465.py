t = int(input())

for _ in range(t):
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    # 지그지그로 가기 vs 뛰어넘고 그다음 밑에 애를 고르기
    if n > 1 :
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for i in range(2, n):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))
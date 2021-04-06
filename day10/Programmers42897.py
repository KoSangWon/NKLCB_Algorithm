def solution(money):
    n = len(money)
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[1], dp[0])

    for i in range(2, n - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer = dp[n - 2]
    
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer = max(answer, dp[n - 1])
    
    return answer

print(solution([1,2,3,1]))
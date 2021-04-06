# 풀이 1
# def solution(n):
#     DIV = 1000000007
#     dp = [0] * (n+1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n + 1):
#         dp[i] = (dp[i-1] + dp[i-2]) % DIV
#     return dp[n]

# 풀이 2
def solution(n):
    DIV = 1000000007
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a % DIV

solution(5)
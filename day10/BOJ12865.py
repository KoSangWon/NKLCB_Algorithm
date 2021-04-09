# 내 풀이
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = map(int, input().split())
    for j in range(1, k + 1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])

# 재귀적 풀이
N, K = map(int, input().split())

W = [0] * (N + 1)
V = [0] * (N + 1)
for i in range(1, N + 1):
    W[i], V[i] = map(int, input().split())

dp = [dict() for _ in range(N + 1)]

def knapsack(i, w):
    if w in dp[i]:
        return dp[i][w]

    if i == 0 or w <= 0:
        return 0

    if w >= W[i]:
        val = max(knapsack(i - 1, w), knapsack(i - 1, w - W[i]) + V[i])
    else:
        val = knapsack(i - 1, w)

    dp[i][w] = val
    return val


print(knapsack(N, K))

# iteration 풀이
N, K = map(int, input().split())

W = [0] * (N + 1)
V = [0] * (N + 1)
for i in range(1, N + 1):
    W[i], V[i] = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for w in range(1, K+1):
        if w >= W[i]:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-W[i]] + V[i])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[N][K])



# iteration 풀이(최적화, 2개만 사용함)
N, K = map(int, input().split())

W = [0] * (N + 1)
V = [0] * (N + 1)
for i in range(1, N + 1):
    W[i], V[i] = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for w in range(1, K+1):
        if w >= W[i]:
            dp[i%2][w] = max(dp[(i-1)%2][w], dp[(i-1)%2][w-W[i]] + V[i])
        else:
            dp[i][w] = dp[(i-1)%2][w]
print(dp[N%2][K])



# iteration 풀이(최적화, 2개만 사용함, 더욱 최적화)
N, K = map(int, input().split())

W = [0] * (N + 1)
V = [0] * (N + 1)
for i in range(1, N + 1):
    W[i], V[i] = map(int, input().split())

need_calc = [set() for _ in range(N+1)]
need_calc[N].add(K)
for i in range(N, 0, -1):
    for w in need_calc[i]:
        need_calc[i - 1].add(w)
        if w >= W[i]:
            need_calc[i-1].add(w-W[i])

dp = [[0 for _ in range(K + 1)]for _ in range(2)]
for i in range(1, N+1):
    for w in need_calc[i]:
        if w >= W[i]:
            dp[i%2][w] = max(dp[(i-1)%2][w], dp[(i-1)%2][w-W[i]] + V[i])
        else:
            dp[i][w] = dp[(i-1)%2][w]
print(dp[N%2][K])

'''
INF = -10 ** 13

N, total_weight = map(int, input().split())

W, V = [], []

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# dp[j] := 重さj以下で得られる最大の価値
dp = [INF] * (total_weight + 1)
dp[0] = 0

for i in range(N):
    for j in range(total_weight, W[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - W[i]] + V[i])

print(max(dp))

'''

INF = -10 ** 13

N, total_weight = map(int, input().split())

W, V = [], []

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# dp[j] := 重さj以下で得られる最大の価値
dp = [INF] * (total_weight + 1)
dp[0] = 0

for i in range(N):
    for j in range(total_weight, W[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - W[i]] + V[i])

print(max(dp))

N = int(input())
h = list(map(int,input().split()))

#DPテーブルの作成
cost = [0] * N
#足場1への移動コストは0
cost[0] = 0
#足場2への移動コストは1通りしかないため固定
cost[1] = cost[0] + abs(h[0] - h[1])

#DPテーブルの更新
for i in range(2,N):
    #以降の足場への移動コストは2通りあるため、コストが小さい方を採用する
    cost[i] = min(cost[i - 1] + abs(h[i - 1] - h[i]), cost[i - 2] + abs(h[i - 2] - h[i]))

print(cost[N - 1])
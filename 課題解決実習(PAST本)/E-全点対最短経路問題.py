#1のビット列を60ビット文シフトさせてる
#ビットを一桁左シフトするごとに二倍されていく⇒1*2^60になる
INF = 1 << 60

n,m = map(int,input().split())

#全ての頂点の組についての最短距離を保存する配列を作成
dist = []
for i in range(0,n):
    dist.append([])
    for j in range(0,n):
        dist[i].append(INF)

#グラフの辺、重みを受け取る
for _ in range(0,m):
    u,v,c = map(int,input().split())
    dist[u][v] = c

#iからiまで（同じ頂点同士）の距離をゼロにする
for i in range(0,n):
    dist[i][i] = 0

#   ワーシャルフロイド法
#経由する頂点を1つずつ増やしながら更新していく
for k in range(0,n):
    #全ての始点xと終点yについてxからyの最短距離を求める
    for x in range(0,n):
        for y in range(0,n):
            #値が最小なら更新する
            dist[x][y] = min(dist[x][y],dist[x][k] + dist[k][y])


#全ての頂点の組について最短距離を合計する
ans = 0
for i in range(0,n):
    for j in range(0,n):
        ans += dist[i][j]

print(ans)
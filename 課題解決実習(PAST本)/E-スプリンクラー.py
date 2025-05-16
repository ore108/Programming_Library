n, m, q = map(int, input().split())

# グラフの初期化
graph = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(False)
    graph.append(a)

# 辺の入力
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = True
    graph[v][u] = True

#頂点のつながりを確認
#print(graph)

# 頂点の初期色
c = list(map(int, input().split()))

# クエリの処理
for i in range(q):
    query = list(map(int, input().split()))
    num = query[0]

    if num == 1:
        # クエリ形式: 1 x (スプリンクラーの起動)
        x = query[1] - 1
        print(c[x])

        # 隣接頂点をxの色で塗り替える
        for j in range(n):
            if graph[x][j]:
                c[j] = c[x]

    elif num == 2:
        # クエリ形式: 2 x y (色の変更)
        x = query[1] - 1
        y = query[2]
        print(c[x])

        # 頂点xの色をyに変更
        c[x] = y

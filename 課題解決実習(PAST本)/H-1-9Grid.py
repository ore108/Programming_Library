# 入力
n, m = map(int, input().split())
A = [list(map(str, input().strip())) for _ in range(n)]

# 無限大の値を定義 (コストの初期値として利用)
INF = 10 * 100

# 各数字に対応する位置リストを保持するためのリスト
num_group = [[] for _ in range(11)]

# 各数字の位置を num_group に分類
for i in range(n):
    for j in range(m):  
        # スタート地点を num_group[0] に格納
        if A[i][j] == "S":
            num_group[0].append((i, j))
        # ゴール地点を num_group[10] に格納
        elif A[i][j] == "G":
            num_group[10].append((i, j))
        # 数字を対応するインデックスに分類
        else:
            num_group[int(A[i][j])].append((i, j))

# 各地点への最小コストを格納する配列
cost = [[INF] * m for _ in range(n)]

# スタート地点の座標を取得
si, sj = num_group[0][0]

# スタート地点のコストを 0 に設定
cost[si][sj] = 0

# 1 から 10 まで順に最小コストを計算
for n in range(1, 11):
    for i, j in num_group[n]:  
        for i2, j2 in num_group[n - 1]:
            # 現在地点へのコストを更新
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i - i2) + abs(j - j2))
            print(cost)

# ゴール地点のコストを取得
gi, gj = num_group[10][0]

# 結果を格納
ans = cost[gi][gj]

# ゴール地点に到達不可の場合 -1 を出力、到達可能なら最小コストを出力
if ans == INF:
    print(-1)
else:
    print(ans)
#print(num_group)
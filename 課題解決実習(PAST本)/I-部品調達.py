# 無限大を表す定数として INF を定義
INF = float("inf")

# 入力として、部品の数 N とセット販売の数 M を受け取る
N, M = map(int, input().split())

# 1始まりのインデックスにするため、ダミーの要素を追加
S = [0] 
C = [0]  

# 各セットの部品情報とコストを処理
for i in range(M):
    s, c = input().split() 
    s_value = 0  # 部品セットのビット表現を初期化
    for j in range(N):  # 各部品についてビットを設定
        if s[j] == "Y":  # 部品がセットに含まれる場合
            s_value |= 2 ** j  # 該当するビットを立てる
    S.append(s_value)  # ビット表現をリストに追加
    C.append(int(c))  # コストをリストに追加

# 全部の部品が揃った状態（集合としてあり得るものの個数）　　
ALL = 2 ** N  

#DPテーブルの作成
cost = [[INF] * ALL for _ in range(M + 1)]

# 初期状態（何も操作していない状態で全部品オフ）のコストは 0
cost[0][0] = 0


# 動的計画法で最小コストを計算
for i in range(1, M + 1):  # 各セットを順に処理
    for n in range(ALL):  # 各部品状態を順に処理
        # セット i を購入しない場合の遷移
        cost[i][n] = min(cost[i][n], cost[i - 1][n])

        # セット i を購入する場合の遷移
        cost[i][n | S[i]] = min(cost[i][n | S[i]], cost[i - 1][n] + C[i])

# 全部品が揃った状態（ALL - 1）の最小コストを取得
ans = cost[M][ALL - 1]

# 最小コストが初期値（INF）のままであれば、解が存在しない
if ans == INF:
    ans = -1

# 結果を出力
print(ans)

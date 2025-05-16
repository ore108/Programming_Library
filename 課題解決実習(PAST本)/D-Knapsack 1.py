N, W = map(int, input().split())

#1始まりにするために先頭にダミーを入れる
ws = [0]
vs = [0]

for i in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

#DPテーブルの初期化
#DP[i][j] = i番目までのアイテムで重さj以下のときの最大価値
DP = [[-float("inf")] * (W + 1) for _ in range(N + 1)]

#何も選んでいないときの価値を0とする
DP[0][0] = 0


for i in range(1, N + 1): #N個のアイテムを順番に見る
    for j in range(W + 1): #0~Wまでをチェックしていく
        # アイテムiを選ばない場合（上の段からそのまま引き継いでくる）
        DP[i][j] = DP[i - 1][j]

        # アイテムiを選ぶ場合の価値を計算して、最大値を比較して更新
        if j - ws[i] >= 0:#アイテムiを選んでも重さの制限を超えないとき
            #i-1番目のアイテムから重さj - ws[i]以下のときに得られる最大価値　+ アイテムiの価値vs[i]
            DP[i][j] = max(DP[i][j], DP[i - 1][j - ws[i]] + vs[i])
            
#DPテーブルの最終行で重さw以下の範囲の最大価値をとる
ans = max(DP[N])
print(ans)

MOD = 10007

N = int(input())
sekinin = input()

# dp[i][S]：i日目に参加者のビットマスクがSのときのスケジュール数
dp = [[0] * 8 for _ in range(N + 1)]

# 初日はJ君が鍵を持っているので、J君だけ参加しているパターン(001)で1通り
dp[0][1] = 1

# 各日について処理する
for i in range(N):
    for S in range(8):  # Sは今日の参加者（ビットで表す 000～111）

        # 責任者が今日の参加者に含まれていなければスキップ
        if sekinin[i] == "J" and (S & 1) == 0:
            continue
        if sekinin[i] == "O" and (S & 2) == 0:
            continue
        if sekinin[i] == "I" and (S & 4) == 0:
            continue

        for T in range(8):  # Tは昨日の参加者
            # 昨日と今日で鍵の受け渡しができるか（共通する人がいるか）
            if S & T != 0:
                dp[i + 1][S] = (dp[i + 1][S] + dp[i][T]) % MOD

# 最終日のすべての参加パターンを合計して答えとする
print(sum(dp[N]) % MOD)

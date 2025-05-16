N = int(input())
S = input()

min_turn = float("inf")


sum_W = [0]
sum_E = [0]

#西を向いている人数を累積和で数える
#sum_W[i] = (i番目の人までに西を向いていた人の人数)
for i in range(0, N):
    if S[i] == "W":
        sum_W.append(sum_W[i] + 1)
    else:
        sum_W.append(sum_W[i])

#東を向いている人数を累積和で数える
#sum_E[i] = (i番目の人までに東を向いていた人の人数)
for i in range(0, N):
    if S[i] == "E":
        sum_E.append(sum_E[i] + 1)
    else:
        sum_E.append(sum_E[i])

#各人iをリーダーにした場合の向き直す人の回数を計算
for i in range(1, N):
    w = sum_W[i] #i番目の人より左側にいる西を向いている人の数
    e = sum_E[N] - sum_E[i + 1] #i番目の人よりも右側にいる東を向いている人の数
    turn = w + e  #向き直す人の合計人数
    min_turn = min(min_turn, turn)

print(min_turn)

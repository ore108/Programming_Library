from collections import defaultdict

# 入力を受け取る
N, X = list(map(int, input().split()))

# 品物を2つのグループ（偶数番目と奇数番目）に分ける
A = []  # 偶数番目の品物
B = []  # 奇数番目の品物

for i in range(N):
    w = int(input())
    if i % 2 == 0:
        A.append(w)
    else:
        B.append(w)

# n の i 番目のビットが 1 かどうかを判定する関数
def has_bit(n, i):
    return (n & (2**i) > 0)

# グループ B の重さの合計ごとに、選び方の個数を記録する辞書
dic = defaultdict(int)

# グループ B の全ての選び方を列挙し、それぞれの重さの合計を計算
for n in range(2**len(B)):  # B に含まれる品物のすべての選び方を試す
    s = 0  # 現在の重さの合計
    for i in range(len(B)):  # B の各品物について
        if has_bit(n, i):  # n の選び方において i 番目の品物を選んでいるか？
            s += B[i]  # 選んだ品物の重さを加算
    dic[s] += 1  # 重さ s が作れる選び方をカウント

# 答えを記録する変数 (重さがぴったり X になる選び方の総数)
ans = 0

# グループ A の全ての選び方を列挙し、重さが X になる選び方を数える
for n in range(2**len(A)):  # A に含まれる品物のすべての選び方を試す
    s = 0  # 現在の重さの合計
    for i in range(len(A)):  # A の各品物について
        if has_bit(n, i):  # n の選び方において i 番目の品物を選んでいるか？
            s += A[i]  # 選んだ品物の重さを加算
    # 残りの重さ (X - s) を B の選び方で作れるか確認
    ans += dic[X - s]  # B の選び方の数を加算

print(ans)
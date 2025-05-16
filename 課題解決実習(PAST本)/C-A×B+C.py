#入力
N = int(input())

ans = 0

#Aを固定してBとCを求める
for A in range(1,N):
    #固定したAに対して可能なBの個数
    b_cnt = (N - 1) // A
    ans += b_cnt

print(ans)
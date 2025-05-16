#https://atcoder.jp/contests/abc404/tasks/abc404_e

N = int(input())
C = [0] + list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

#p=操作回数
p = 0
q = 0

for i in range(1, N):
    if A[i] > 0:
        l = r = i
        while q < l:
            p += 1
            nl = l
            for j in range(l, r + 1):
                nl = min(nl, j - C[j])
            l = nl
        q = i

print(p)

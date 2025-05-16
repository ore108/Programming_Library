#https://atcoder.jp/contests/abc405/tasks/abc405_b

N, M = map(int, input().split())
A = list(map(int, input().split()))
li = [int(i) for i in range(1, M+1)]

cnt = 0

s = set(A)
Flag = True
for i in li:
    if i not in s:
        Flag = False
if not Flag:
    print(0)
    exit()

for i in range(N-1, -1, -1):
    A.pop()
    cnt += 1
    s = set(A)
    Flag = True
    for j in li:
        if j not in s:
            Flag = False
    if not Flag:
        print(cnt)
        exit()

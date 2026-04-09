N,M = map(int,input().split())

L = []
R = []

imos = [0] * (N + 2)

for i in range(M):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
    imos[l] += 1
    imos[r + 1] -= 1

for i in range(1,N + 2):
    imos[i] += imos[i - 1]

ans = M
for i in range(M):
    Flag = False
    for j in range(L[i],R[i] + 1):
        if imos[j] == 1:
            Flag = True
            break
    if Flag:
        ans = 1
        break

print(ans)
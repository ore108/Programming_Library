H,W = map(int,input().split())

MAP = [["." for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0 or i == H - 1:
            MAP[i][j] = "#"
        if j == 0 or j == W - 1:
            MAP[i][j] = "#"

for i in range(H):
    print(*MAP[i],sep = "")


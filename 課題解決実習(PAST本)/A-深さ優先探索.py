#再帰上限を増やす(Pythonは上限1000までになっているため)
import sys
sys.setrecursionlimit(10 ** 6)

h, w = map(int, input().split())
c = [list(input().strip()) for _ in range(h)]

#訪問済みリストの作成
visited = [[False] * w for _ in range(h)]
#4方向への移動
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#スタート地点とゴール地点の座標を探す
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            si, sj = i, j
        if c[i][j] == "g":
            gi, gj = i, j

#深さ優先探索を定義
def dfs(i, j):
    visited[i][j] = True
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if not (0 <= ni < h and 0 <= nj < w):
            continue
        if c[ni][nj] == "#":
            continue
        if not visited[ni][nj]:
            dfs(ni, nj)
#スタート地点から探索する
dfs(si, sj)

#ゴール地点まで探索できているか
if visited[gi][gj]:
    print("Yes")
else:
    print("No")

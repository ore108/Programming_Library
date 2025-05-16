#Dequeを追加
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

#グラフの辺を追加
for _ in range(m):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    graph[ai].append(bi)
    graph[bi].append(ai)

#未探索にしておく
dist = [-1] * n
queue = deque()
#始点となる頂点0をキューに追加
queue.append(0)
#0への最短距離を0にする
dist[0] = 0

#幅優先探索
while queue:
    i = queue.popleft()
    for j in graph[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            queue.append(j)

if dist[n - 1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
n,m,q = map(int,input().split())

#グラフの初期化
graph = []
for i in range(n):
    a = []
    graph.append(a)

#隣接リストを作成
for i in range(m):
    u,v = map(int,input().split())

    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)

print(graph)

#頂点iの色c_iを代入
c = list(map(int,input().split()))

for i in range(q):
    query = list(map(int,input().split()))

    num = query[0] 

    if num == 1:
        x = query[1]
        
        x -= 1

        print(c[x])
        #頂点xの隣接している頂点の色をc_x色に変更する
        for i in graph[x]:
            c[i] = c[x]

    if num == 2:
        x = query[1]
        y = query[2]

        x -= 1

        print(c[x])
        #頂点xを色yに変更する
        c[x] = y

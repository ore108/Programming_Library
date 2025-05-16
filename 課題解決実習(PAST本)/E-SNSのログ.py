n,q = map(int,input().split())

graph = []

for i in range(n):
    a = []
    for j in range(n):
        a.append(False)
    
    
    graph.append(a)


for i in range(q):
    query = list(map(int,input().split()))

    num = query[0]

    a = query[1] - 1

    if num == 1:

        b = query[2] - 1

        graph[a][b] = True

    if num == 2:

        for i in range(n):
            if graph[i][a]:
                graph[a][i] = True
    
    if num == 3:

        follow = []

        for i in range(n):
            if graph[a][i]:
                for j in range(n):
                    if graph[i][j] and j != a:

                        follow.append(j)

        for j in follow:
            graph[a][j] = True


for i in range(n):
    for j in range(n):
        if graph[i][j]:
            print("Y",end = "")
        else:
            print("N",end = "")
    print()
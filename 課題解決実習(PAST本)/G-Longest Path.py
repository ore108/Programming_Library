import sys
sys.setrecursionlimit(10 ** 6)  # 再帰の深さ制限を緩める

# 頂点数 n と 辺の数 m を入力
n, m = map(int, input().split())

# グラフの隣接リストを初期化（各頂点から出る辺を格納）
edge = [[] for _ in range(n)]

# 各頂点の入次数を記録するリストを初期化
ind = [0] * n

# 辺の情報を入力し、隣接リストと入次数リストを更新
for i in range(m):
    # 頂点の入力は1-indexedなので0-indexedに変換
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    # 頂点 x から頂点 y へ辺を追加
    edge[x].append(y)
    
    # 頂点 y の入次数を増やす（y に入る辺が増えるため）
    ind[y] += 1

# 各頂点からの最長経路の長さを格納するリスト
length = [0] * n

# 各頂点の訪問済み状態を記録するリスト（再帰計算済みかどうかを判定）
visited = [False] * n

# 再帰関数 rec(i): 頂点 i から出発したときの最長経路の長さを計算
def rec(i):
    # 頂点 i がすでに訪問済みなら、計算済みの長さを返す
    if visited[i]:
        return length[i]
    
    # 頂点 i を訪問済みとしてマーク
    visited[i] = True
    #print(str(i)+"を訪問しました。")
    
    # 頂点 i から出発する辺をたどる
    for j in edge[i]:
        # 隣接する頂点 j の最長経路 + 1 と、現在の最長経路を比較し、長い方を保持
        length[i] = max(length[i], rec(j) + 1)
    
    # 頂点 i からの最長経路の長さを返す
    return length[i]

# 入次数が 0 の頂点から順に最長経路を計算
for i in range(n):
    # 入次数が 0 の頂点は他の頂点からの依存がなく、スタート地点として扱える
    if ind[i] == 0:
        rec(i)  # 頂点 i からの最長経路を計算

# 全ての頂点から出発する場合の最長経路を出力
print(max(length))

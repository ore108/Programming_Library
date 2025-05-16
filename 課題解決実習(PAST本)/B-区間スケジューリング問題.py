N = int(input())
task = [tuple(map(int, input().split())) for _ in range(N)]

# タスクを終了時間でソートする
#タプルxの二番目の要素（終了時間）を取り出して、ソートしている
task.sort(key=lambda x: x[1])


ans = 0  #採用したタスクの個数
last = 0  #最後に採用したタスクの終了時間

for a, b in task:
    #現在のタスクの開始時間が、前回のタスクの終了時間より後であれば、そのタスクを採用する
    if last < a:
        ans += 1
        last = b


print(ans)

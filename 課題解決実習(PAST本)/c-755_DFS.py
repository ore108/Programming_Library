N = int(input())  

ans = 0  

# 深さ優先探索を定義
def dfs(n, used_three, used_five, used_seven):
    global ans  # グローバル変数ansを使う

    # 現在の数がNを超えたら終了
    if n > N:
        return

    # 数字に3, 5, 7がすべて含まれていたらカウントを増やす
    if used_three and used_five and used_seven:
        ans += 1

    # 末尾に3を追加し、3を使ったことを記録
    dfs(10 * n + 3, True, used_five, used_seven)

    # 末尾に5を追加し、5を使ったことを記録
    dfs(10 * n + 5, used_three, True, used_seven)

    # 末尾に7を追加し、7を使ったことを記録
    dfs(10 * n + 7, used_three, used_five, True)

# 初期状態で0から探索開始。（3, 5, 7は使われていない）
dfs(0, False, False, False)


print(ans)

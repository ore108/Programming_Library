import tkinter
import tkinter.messagebox
import random

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 80)
BLACK = 1
WHITE = 2
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
space = 0
color = [0]*2
player = -1
cpu = -1
who = ["あなた", "コンピュータ"]
who2 = ["プレイヤー1", "プレイヤー2"]
board = []
back = []
for y in range(8):
    board.append([0] * 8)
    back.append([0] * 8)

point = [
    [6, 2, 5, 4, 4, 5, 2, 6],
    [2, 1, 3, 3, 3, 3, 1, 2],
    [5, 3, 3, 3, 3, 3, 3, 5],
    [4, 3, 3, 0, 0, 3, 3, 4],
    [4, 3, 3, 0, 0, 3, 3, 4],
    [5, 3, 3, 3, 3, 3, 3, 5],
    [2, 1, 3, 3, 3, 3, 1, 2],
    [6, 2, 5, 4, 4, 5, 2, 6]
]

def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x/80)
    my = int(e.y/80)
    if mx>7: mx = 7
    if my>7: my = 7

def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x*80
            Y = y*80
            cvs.create_rectangle(X, Y, X+80, Y+80, outline="black")
            if board[y][x]==BLACK:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="black", width=0)
            if board[y][x]==WHITE:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="white", width=0)

            if player == 0:
                if kaeseru(x, y, color[turn]) > 0:
                    cvs.create_oval(X + 5, Y + 5, X + 75, Y + 75, outline = "cyan", width = 2)
            else:
                if turn == 0 and kaeseru(x, y, color[turn]) > 0:
                    cvs.create_oval(X + 5, Y + 5, X + 75, Y + 75, outline = "cyan", width = 2)

    if proc != 0: cvs.update()

def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE

# 石を打ち、相手の石をひっくり返す
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break

# そこに打つといくつ返せるか数える
def kaeseru(x, y, iro):
    if board[y][x]>0:
        return -1 # 置けないマス
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    total += k
                    break
    return total

# 打てるマスがあるか調べる
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0:
                return True
    return False

# 黒い石、白い石、いくつかあるか数える
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x]==BLACK: b += 1
            if board[y][x]==WHITE: w += 1
    return b, w

def save():
    for y in range(8):
        for x in range(8):
            back[y][x] = board[y][x]

def load():
    for y in range(8):
        for x in range(8):
            board[y][x] = back[y][x]

def uchiau(iro):
    while True:
        if not uteru_masu(BLACK) and not uteru_masu(WHITE):
            break

        iro = 3 - iro
        if uteru_masu(iro):
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if kaeseru(x, y, iro) > 0:
                    ishi_utsu(x, y, iro)
                    break

def computer_1(iro):
    sx, sy = 0, 0
    p = 0
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0 and point[y][x] > p:
                p = point[y][x]
                sx, sy = x, y
    return sx, sy

def computer_2(iro, loops):
    global msg
    win = [0] * 64
    save()

    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                msg += "."
                banmen()
                win[x + y * 8] = 1
                for i in range(loops):
                    ishi_utsu(x, y, iro)
                    uchiau(iro)
                    b, w = ishino_kazu()
                    if iro == BLACK and b > w:
                        win[x + y * 8] += 1
                    if iro == WHITE and w > b:
                        win[x + y * 8] += 1
                    load()
    
    m = 0
    n = 0
    for i in range(64):
        if win[i] > m:
            m = win[i]
            n = i
    x = n % 8
    y = int(n / 8)
    return x, y

#コンピュータの思考ルーチン
def computer_0(iro): # ランダムに打つ
    while True:
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        if kaeseru(rx, ry, iro)>0:
            return rx, ry

# 盤面をランダムに1マスずらす
def shift_board():
    direction = random.choice(["up", "down", "left", "right"])
    new_board = [[0]*8 for _ in range(8)]
    if direction == "up":
        for y in range(1, 8):
            for x in range(8):
                new_board[y-1][x] = board[y][x]
    elif direction == "down":
        for y in range(7):
            for x in range(8):
                new_board[y+1][x] = board[y][x]
    elif direction == "left":
        for y in range(8):
            for x in range(1, 8):
                new_board[y][x-1] = board[y][x]
    elif direction == "right":
        for y in range(8):
            for x in range(7):
                new_board[y][x+1] = board[y][x]

    # Fill the empty spaces
    for y in range(8):
        for x in range(8):
            if new_board[y][x] == 0:
                new_board[y][x] = 0

    # Update the board
    for y in range(8):
        for x in range(8):
            board[y][x] = new_board[y][x]

# ゲームのメイン処理
def main():
    global mc, proc, turn, msg, space, player
    if proc == 0:
        ban_syokika()
        banmen()
        tkinter.messagebox.showinfo("リバーシ", "ゲームスタート")
        player = random.randint(0, 1)  # 先手プレイヤーをランダムに決定
        proc = 1
        turn = 0
        mc = 0

    if proc == 1:
        if space == 0:
            b, w = ishino_kazu()
            s = "黒 = "+str(b)+"  白 = "+str(w)+" で終了"
            if b == w: s = "引き分け！"
            if b > w: s = who[color[0]-1]+"(黒)の勝ち！"
            if b < w: s = who[color[1]-1]+"(白)の勝ち！"
            msg = s
            banmen()
            tkinter.messagebox.showinfo("リバーシ", s)
            proc = 0
        else:
            iro = color[turn]
            if not uteru_masu(iro):
                turn = 1 - turn
                iro = color[turn]
                if not uteru_masu(iro):
                    b, w = ishino_kazu()
                    s = "黒 = "+str(b)+"  白 = "+str(w)+" で終了"
                    if b == w: s = "引き分け！"
                    if b > w: s = who[color[0]-1]+"(黒)の勝ち！"
                    if b < w: s = who[color[1]-1]+"(白)の勝ち！"
                    msg = s
                    banmen()
                    tkinter.messagebox.showinfo("リバーシ", s)
                    proc = 0

            else:
                msg = who[color[turn]-1]+"("+("黒" if iro == BLACK else "白")+")の番です"
                if player == turn:
                    if mc == 1:
                        if kaeseru(mx, my, iro) > 0:
                            ishi_utsu(mx, my, iro)
                            space -= 1
                            turn = 1 - turn
                            shift_board()  # 盤面をランダムに1マスずらす
                        mc = 0
                else:
                    if turn == 1:
                        cx, cy = computer_2(iro, 100)
                    else:
                        cx, cy = computer_0(iro)  # ランダムに打つ
                    ishi_utsu(cx, cy, iro)
                    space -= 1
                    turn = 1 - turn
                    shift_board()  # 盤面をランダムに1マスずらす
        banmen()
    root.after(100, main)

root = tkinter.Tk()
root.title("リバーシ")
root.resizable(False, False)
root.bind("<Button-1>", click)
cvs = tkinter.Canvas(root, width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()

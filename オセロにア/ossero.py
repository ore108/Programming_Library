import tkinter
import tkinter.messagebox
import random

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 80)
BLACK = 1
WHITE = 2
ITEM = 3
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
space = 0
color = [0] * 2
player = -1
cpu = -1
who = ["あなた", "コンピュータ"]
who2 = ["プレイヤー1", "プレイヤー2"]
board = []
back = []
items = []

for y in range(8):
    board.append([0] * 8)
    back.append([0] * 8)
    items.append([0] * 8)

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

def place_items():
    global items
    item_positions = random.sample([(x, y) for x in range(8) for y in range(8) if board[y][x] == 0], 10)
    for pos in item_positions:
        items[pos[1]][pos[0]] = ITEM

def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7: mx = 7
    if my > 7: my = 7

def select_piece_to_remove():
    global mx, my, mc
    msg = "消すマスを選んでください"
    banmen()
    mc = 0
    while mc == 0:
        cvs.update()
        if mc == 1 and items[my][mx] == ITEM:  # アイテムマスに置いた場合
            remove_piece(mx, my)
            banmen()
            mc = 0  # mcをリセットして再度クリック待ちにする

def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            elif board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
            if items[y][x] == ITEM:
                cvs.create_rectangle(X + 20, Y + 20, X + 60, Y + 60, outline="red", width=2)
            if player == 0:
                if kaeseru(x, y, color[turn]) > 0:
                    cvs.create_oval(X + 5, Y + 5, X + 75, Y + 75, outline="cyan", width=2)
            else:
                if turn == 0 and kaeseru(x, y, color[turn]) > 0:
                    cvs.create_oval(X + 5, Y + 5, X + 75, Y + 75, outline="cyan", width=2)
    if proc != 0: cvs.update()

def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
            items[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE
    place_items()

def remove_piece(x, y):
    board[y][x] = 0

def ishi_utsu(x, y, iro):
    board[y][x] = iro
    if items[y][x] == ITEM:
        items[y][x] = 0
        select_piece_to_remove()
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break

def kaeseru(x, y, iro):
    if board[y][x] > 0:
        return -1
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    total += k
                    break
    return total

def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                return True
    return False

def ishino_kazu():
    b = 0
    c = 0
    d = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == BLACK:
                c += 1
            elif board[y][x] == WHITE:
                d += 1
    return (c, d)

def hantei():
    global msg, player, turn
    (a, b) = ishino_kazu()
    if a + b == 64:
        if a > b:
            msg = "プレイヤー1の勝ち"
        elif a < b:
            msg = "プレイヤー2の勝ち"
        else:
            msg = "引き分け"
        return True
    if uteru_masu(color[0]) == False and uteru_masu(color[1]) == False:
        if turn == 0:
            msg = "プレイヤー1はパスです。"
        else:
            msg = "プレイヤー2はパスです。"
        turn = 1 - turn
        return True
    return False

def ai():
    mx = -1
    my = -1
    m = -1
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, color[1]) > m:
                mx = x
                my = y
                m = kaeseru(x, y, color[1])
    if mx >= 0:
        ishi_utsu(mx, my, color[1])

def main():
    global msg, player, turn, mc
    ban_syokika()
    banmen()
    while True:
        mc = 0
        if hantei() == True:
            banmen()
            tkinter.messagebox.showinfo("", msg)
            break
        if turn == 0:
            player = 0
        else:
            player = 1
            ai()
        banmen()
        turn = 1 - turn

root = tkinter.Tk()
root.title("オセロ")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(root, width=640, height=720)
cvs.pack()
main()
root.mainloop()


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
color = [0] * 2
who = ["Player1", "Player2"]
board = []
for y in range(8):
    board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7: mx = 7
    if my > 7: my = 7

def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_rectangle(X + 10, Y + 10, X + 70, Y + 70, fill="cyan", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="yellow", width=0)
            if kaeseru(x,y,color[turn]) > 0:
                cvs.create_oval(X + 5,Y + 5,X + 75,Y + 75,outline="fuchsia",width=2)
    cvs.update()

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

def ishi_utsu(x, y, iro):
    board[y][x] = iro
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dy, dx in directions:
        k = 0
        sx, sy = x, y
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
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dy, dx in directions:
        k = 0
        sx, sy = x, y
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
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == BLACK: b += 1
            if board[y][x] == WHITE: w += 1
    return b, w

def main():
    global mc, proc, turn, msg, space
    banmen()
    if proc == 0:
        msg = "黒から始まる"
        cvs.create_text(320, 200, text="Reversi", fill="gold", font=FL)
        cvs.create_text(200, 440, text="START", fill="magenta", font=FS)
        #cvs.create_text(480, 440, text="後手(白)", fill="lime", font=FS)
        if mc == 1:
            mc = 0
            if (mx == 1 or mx == 2) and my == 5:
                ban_syokika()
                color[0] = BLACK
                color[1] = WHITE
                turn = 0
                proc = 1
            if (mx == 5 or mx == 6) and my == 5:
                ban_syokika()
                color[0] = WHITE
                color[1] = BLACK
                turn = 1
                proc = 1
    elif proc == 1:
        if turn == 0:
            msg = "Player1の番です"
        else:
            msg = "Player2の番です"
        proc = 2
    elif proc == 2:
        if mc == 1:
            mc = 0
            if kaeseru(mx, my, color[turn]) > 0:
                ishi_utsu(mx, my, color[turn])
                turn = 1 - turn
                proc = 3
    elif proc == 3:
        msg = ""
        proc = 4
    elif proc == 4:
        if space == 0:
            proc = 5
        elif not uteru_masu(BLACK) and not uteru_masu(WHITE):
            tkinter.messagebox.showinfo("", "どちらも打てないので終了です")
            proc = 5
        elif not uteru_masu(color[turn]):
            tkinter.messagebox.showinfo("", who[turn] + "は打てないのでパスです")
            turn = 1 - turn
            proc = 1
        else:
            proc = 1
    elif proc == 5:
        b, w = ishino_kazu()
        tkinter.messagebox.showinfo("終了", "黒 = {}、白={}".format(b, w))
        if (color[0] == BLACK and b > w) or (color[0] == WHITE and w > b):
            tkinter.messagebox.showinfo("", "Player1(黒)の勝ち！")
        elif (color[1] == BLACK and b > w) or (color[1] == WHITE and w > b):
            tkinter.messagebox.showinfo("", "Player2(白)の勝ち！")
        else:
            tkinter.messagebox.showinfo("", "引き分け")
        proc = 0
    root.after(100, main)

root = tkinter.Tk()
root.title("リバーシ")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=640, height=700, bg="deep pink")
cvs.pack()
root.after(100, main)
root.mainloop()
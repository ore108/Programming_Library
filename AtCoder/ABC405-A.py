#https://atcoder.jp/contests/abc405/tasks/abc405_a


R,X = map(int,input().split())

if X == 1:
    if R >= 1600 and R <= 2999:
        print("Yes")
        exit()
elif X == 2:
    if R >= 1200 and R <= 2399:
        print("Yes")
        exit()
print("No")

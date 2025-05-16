MOD = 10007

N = int(input())
sekinin = input()

dp_past = [0] * 8

dp_past[1] = 1

for i in range(N):
    dp_now = [0] * 8
    for S in range(8):
        if sekinin[i] == "J" and (S & 1) == 0:
            continue
        if sekinin[i] == "O" and (S & 2) == 0:
            continue
        if sekinin[i] == "I" and (S & 4) == 0:
            continue
    
    for T in range(8):
        if S & T != 0:
            dp_now[S] = (dp_now[S] + dp_past[T]) % MOD
    
    dp_past = dp_now

print(sum(dp_past) % MOD)
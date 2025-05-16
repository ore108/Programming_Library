R,B = map(int,input().split())
x,y = map(int,input().split())

ok = 0
ng = 10 ** 18

def check(k):
    if R - k < 0 or B - k < 0:
        return False
    return (R - k) // (x - 1) + (B - k) // (y - 1) >= k

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
    
print(ok)
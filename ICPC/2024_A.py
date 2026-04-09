while True:
    N = int(input())

    if N == 0:
        exit()
    else:
        A = list(map(int,input().split()))

    sA = sorted(A)
    ans = 0

    for i in range(len(A)):
        if ans + A[i] <= 300:
            ans += A[i]
    
    print(ans)
import bisect

N,K = map(int,input().split())
A = list(map(int,input().split()))

#二分探索
ans = bisect.bisect_left(A,K)

#bisectは条件に当てはまらない場合、len(A)を返すため
if ans == N:
    print(-1)
else:
    print(ans)

'''
left = 0
right = N

while left < right:
    mid = (left + right) // 2
    if A[mid] >= K:
        right = mid  # 条件を満たす可能性があるので右端を縮める
    else:
        left = mid + 1  # 条件を満たさないので左端を右に移動

# 探索結果を確認
if left < N and A[left] >= K:
    print(left)
else:
    print(-1)
'''
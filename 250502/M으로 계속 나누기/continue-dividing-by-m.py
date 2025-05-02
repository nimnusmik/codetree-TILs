N, M = map(int, input().split())

# Please write your code here.
while N > 0:
    print(int(N))
    N /= M
    if N == 0: N = 0

N, M = map(int, input().split())

# Please write your code here.
while N > 0 and N>M:
    print(int(N))
    N /= M

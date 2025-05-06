N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    sum = 0  # 이 줄을 for문 안으로 옮겨주세요!
    for i in range(a, b + 1):
        if i % 2 == 0:
            sum += i
    print(sum)
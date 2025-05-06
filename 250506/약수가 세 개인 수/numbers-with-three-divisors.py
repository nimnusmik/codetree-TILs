start, end = map(int, input().split())

count = 0  # 전체 소수 개수 세기용
for i in range(start, end + 1):
    Divisor = []
    for j in range(1, i + 1):  # 여기! j는 1부터 i까지 가야 모든 약수 확인 가능해요
        if i % j == 0:
            Divisor.append(j)

    if len(Divisor) == 3:  # 소수는 약수가 1과 자기자신 딱 2개
        count += 1

print(count)
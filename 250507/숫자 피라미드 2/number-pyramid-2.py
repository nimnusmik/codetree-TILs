N = int(input())

num = 1  # 출력할 숫자
for i in range(1, N + 1):       # 줄 수만큼 반복 (1줄, 2줄, ..., N줄)
    for j in range(i):          # 줄마다 숫자를 i개 출력
        print(num, end=' ')     # 숫자 출력 후 줄바꿈 안 하고 한 칸 띄기
        num += 1                # 숫자 1 증가
     print()                     # 줄 바꾸기
f, s = map(int, input().split())
new_list = [f, s, f + s]  # ← 여기 'f + s'는 그냥 더한 값 그대로 넣기!

for i in range(3, 10):  # 10개 채울 때까지 반복
    new_num = (new_list[i - 1] + new_list[i - 2]) % 10  # 그다음부터는 %10
    new_list.append(new_num)

for i in range(10):  # 10개까지만 출력
    print(new_list[i], end=' ')
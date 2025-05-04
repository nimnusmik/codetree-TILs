f, s = map(int, input().split())
new_list = [f, s]  # 처음 두 개

# 세 번째부터는 % 10을 적용
for i in range(2, 10):
    new_num = (new_list[i - 1] + new_list[i - 2]) % 10
    new_list.append(new_num)

# 결과 출력
print(f, s, f + s, end=' ')
for i in range(3, 10):
    print(new_list[i], end=' ')
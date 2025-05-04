f, s = map(int, input().split())
new_list = [f, s, f + s]  # ✅ 처음 3개는 그대로 더함

for i in range(3, 10):
    new_num = (new_list[i-1] + new_list[i-2]) % 10  # 이후부터는 % 10
    new_list.append(new_num)

for i in range(10):
    print(new_list[i], end=' ')
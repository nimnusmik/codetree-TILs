f, s = map(int, input().split())
new_list = [f, s, f + s]  # 세 번째 항은 mod 없이 그대로!

for i in range(3, 10):
    new_num = (new_list[i - 1] + new_list[i - 2]) % 10
    new_list.append(new_num)

for num in new_list:
    print(num, end=' ')
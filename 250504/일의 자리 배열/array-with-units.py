f, s = map(int, input().split())
new_list = [f, s, f + s]   

for i in range(3, 10):
    new_num = (new_list[i - 1] + new_list[i - 2]) % 10
    new_list.append(new_num)

print(*new_list)
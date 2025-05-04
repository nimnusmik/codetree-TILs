f, s = map(int, input().split())
new_list = [f, s, f+s]
#0,  1,  2,  3,  4,  5, 6, 7, 8, 9, 10, 11 
#f, s, f+s
for i in range(3, 10):
    new_num = (new_list[i-1] + new_list[i-2]) % 10 
    new_list.append(new_num)

for i in range(len(new_list)):
    print(new_list[i], end = ' ')
    


num = int(input())
sum = 0
count = 0

for i in range(1, num + 1):
    sum += i
    count += 1
    if sum > num:
        break

print(count)
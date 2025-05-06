a, b = map(int, input().split())
list = []
list.append(a)

while True:
    if a % 2 == 0:
        next_a = a + 3
    else:
        next_a = a * 2

    if next_a > b:
        break

    a = next_a
    list.append(a)

print(*list, sep=' ')
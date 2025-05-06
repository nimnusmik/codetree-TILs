start, end = map(int, input().split())

# Please write your code here.
for i in range(start, end+1):
    Divisor = 0
    for j in range(i):
        if j % i == 0: 
            Divisor += 1
print(Divisor)
mul_3 = 0
mul_5 = 0

for i in range(10):
    num = int(input())
    if num % 3 ==0:
        mul_3 += 1
    if num % 5 ==0:
        mul_5 += 1
print(mul_3, mul_5)
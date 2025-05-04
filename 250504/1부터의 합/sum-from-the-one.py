num = int(input())
sum = 0
count = 0

for i in range(0,num):
    if sum < i: 
        sum += i
        count += 1
print(count)
    

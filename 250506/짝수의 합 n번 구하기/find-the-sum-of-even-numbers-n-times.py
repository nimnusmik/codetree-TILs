N = int(input())
sum = 0
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a,b):
        if i % 2 == 0:
            #print('i:',i)
            sum += i
            #print(sum) 
    print(sum)

#print(6+8+10+12+14+16+18+20+22+24+26+28)
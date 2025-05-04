n = int(input())
nums = list(map(int,input().split()))
even_list = []

#print(nums)
for num in nums:
    if num % 2 == 0: 
        even_list.append(num)
    #print( even_list)

for i in range(len(even_list)-1,-1,-1):
        print(even_list[i], end = ' ')

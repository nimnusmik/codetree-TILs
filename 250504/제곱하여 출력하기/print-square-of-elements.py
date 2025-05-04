N = int(input())
numbers = list(map(int, input().split()))

squares = [num**2 for num in numbers]
for sq in squares:
    print(sq, end=' ')
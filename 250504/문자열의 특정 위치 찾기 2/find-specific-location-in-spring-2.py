fruits = ["apple", "banana", "grape", "blueberry", "orange"]
char = input()  # str() 안 해도 이미 문자열이야!
count = 0

for fr in fruits:
    if char in fr[2:5]:
        print(fr)
        count += 1

print(count)
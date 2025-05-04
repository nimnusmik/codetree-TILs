A, B = map(str, input().split())

if len(A) > len(B): print(A, len(A), end = ' ')
elif len(A) < len(B): print(B, len(B), end = ' ')
else: print('same')

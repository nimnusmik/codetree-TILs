text = input()
text = list(text)

text[1] = 'a'       # 두 번째 글자
text[-2] = 'a'      # 끝에서 두 번째 글자

print(''.join(text))
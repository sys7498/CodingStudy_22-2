sample = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()

# 문자열에서 sample에 포함된 문자들을 찾아서 모두 제거
for pattern in sample:
    text = text.replace(pattern, '*')

# 제거한 후의 문자열에서 알파벳의 개수 세기
alphabet_count = sum(c.isalpha() for c in text) + sum(c=='*' for c in text)

print(alphabet_count)
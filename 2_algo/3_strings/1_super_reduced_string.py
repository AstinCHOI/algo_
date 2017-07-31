s = input()

size = len(s)
i = 1
while i < size:
    if s[i] == s[i-1]:
        s = s[:i-1] + s[i+1:]
        i = 0
        size = len(s)
    i = i + 1

# aaabccddd
# abccddd
# ab <-> ddd
# ab <-> d

if s:
    print(s)
else:
    print('Empty String')
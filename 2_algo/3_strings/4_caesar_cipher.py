N = input()
S = input()
K = int(input())

for s in S:
    if s.isalpha():
        a = ord('A') if s.isupper() else ord('a')
        s = chr(a + ((ord(s)-a+K)%26))
    print(s, end='')
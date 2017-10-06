n = int(input())

for _ in range(n):
    s = input()
    ls = len(s)
    funny = True
    for i in range(1, ls):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[(i*-1)]) - ord(s[(i*-1)-1])):
            funny = False
            break
    if funny:
        print("Funny")
    else:
        print("Not Funny")
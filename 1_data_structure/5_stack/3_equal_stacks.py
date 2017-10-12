n1, n2, n3 = map(int, input().split(' '))

s1 = list(map(int, input().split(' ')))
s2 = list(map(int, input().split(' ')))
s3 = list(map(int, input().split(' ')))

s1.reverse();s2.reverse();s3.reverse();

s1s = sum(s1)
s2s = sum(s2)
s3s = sum(s3)

while not (s1s == s2s and s2s == s3s):
    m = max(s1s, s2s, s3s)
    if m == s1s:
        s1s -= s1.pop()
    elif m == s2s:
        s2s -= s2.pop()
    else:
        s3s -= s3.pop()

print(s1s)
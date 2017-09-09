alphabet = list(map(int, input().split(' ')))
arr = input()

m = -1
for ap in arr:
    num = alphabet[ord(ap)-97]
    if num > m:
        m = num

print(m*len(arr))
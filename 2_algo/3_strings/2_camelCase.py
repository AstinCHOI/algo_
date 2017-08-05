str = input()

num = 1
for s in str:
    if s.isupper():
        num = num + 1
print(num)
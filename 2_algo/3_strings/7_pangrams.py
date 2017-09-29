sen = input()
alpha = [0] * 26

for one in sen:
    if one == ' ':
        continue
    else:
        alpha[ord(one.upper())-65] = 1

if sum(alpha) == 26:
    print("pangram")
else:
    print("not pangram")

# from discussions
# print("pangram") if len(set([i.lower() for i in input().strip()]) & set("abcdefghijklmnopqrstuvwxyz")) == 26  else print("not pangram")
    
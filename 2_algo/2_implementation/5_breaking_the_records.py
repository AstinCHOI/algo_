n = int(input())
scores = list(map(int, input().split()))

ma = mi = scores[0]
ma_, mi_ = 0, 0

for i in range(1, n):
    if scores[i] > ma:
        ma = scores[i]
        ma_ = ma_ + 1
    
    if scores[i] < mi:
        mi = scores[i]
        mi_ = mi_ + 1

print(ma_, mi_)
N, K = map(int, input().split(' '))

imp = []
nimp = []
for _ in range(N):
    L, T = map(int, input().split(' '))
    if T:
        imp.append(L)
    else:
        nimp.append(L)

imp.sort(reverse=True)
impl = len(imp)
print(sum(imp[:K]) - sum(imp[K:]) + sum(nimp))
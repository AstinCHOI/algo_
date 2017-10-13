T = int(input())
for _ in range(T):
    N, M, S = map(int, input().split(' '))
    print(((M+S-2)%N)+1)
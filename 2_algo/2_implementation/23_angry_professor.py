T = int(input())
for _ in range(T):
    N, K = map(int, input().split(' '))
    students = list(map(int, input().split(' ')))

    early = 0
    for student in students:
        if student < 0:
            early += 1

    if early >= K:
        print("YES")
    else:
        print("NO")
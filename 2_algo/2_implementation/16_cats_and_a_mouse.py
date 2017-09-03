q = int(input())

for _ in range(q):
    arr = list(map(int, input().split()))
    A = abs(arr[2] - arr[0])
    B = abs(arr[2] - arr[1])
    if A < B:
        print("Cat A")
    elif A > B:
        print("Cat B")
    else:
        print("Mouse C")
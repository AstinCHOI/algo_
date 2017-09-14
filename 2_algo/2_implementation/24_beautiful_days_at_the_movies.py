i, j, k = map(int, input().split(' '))

cnt = 0
for day in range(i, j+1):
    if abs(day - int(str(day)[::-1])) % k == 0:
        cnt += 1
print(cnt)

# In my opinion - not good to read..
# i, j, k = [int(x) for x in input().split()]
# beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
# print(sum(beautifulDays))
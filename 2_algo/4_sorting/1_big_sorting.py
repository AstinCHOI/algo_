# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# arr = []

# 1: fail
# def binarySearch(num, st, ed):
#     mid = int((ed + st) / 2)
    
#     if st == ed:
#         return mid
    
#     if num < arr[mid]:
#         return binarySearch(num, st, mid)
#     else:
#         return binarySearch(num, mid+1, ed)

# for i in range(n):
#     num = int(input())

#     idx = binarySearch(num, 0, i)
#     arr.insert(idx, num)

# for j in range(n):
#     print(arr[j])

# 2: fail
# for i in range(n):
#     num = int(input())
#     arr.append(num)

# arr.sort()
# for j in range(n):
#     print(arr[j])

n = int(input().strip())
bucket = {}

for _ in range(n):
    number = input().strip()
    length = len(number)
    
    if not length in bucket:
        bucket[length] = []
    
    bucket[length].append(number)

for key in sorted(bucket):
    for value in sorted(bucket[key]):
        print(value)
N = int(input())
steps = input()

below = False
level = 0
valley = 0
for step in steps:
    if step == 'U':
        level += 1
    else:
        level -= 1
    
    if not below and level < 0:
        valley += 1
        below = True
    
    if level >= 0:
        below = False
    
print(valley)
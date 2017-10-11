n = int(input())

for _ in range(n):
    case = input()
    stack = []
    flag = True
    for one in case:
        if one == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            stack.pop()
        elif one == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            stack.pop()
        elif one == '}':
            if not stack or stack[-1] != '{':
                flag = False
                break
            stack.pop()
        else:
            stack.append(one)

    if flag and not stack:
        print("YES")
    else:
        print("NO")
    
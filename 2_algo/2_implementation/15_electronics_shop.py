s, n, m = map(int, input().split(' '))
keyboards = list(map(int, input().split(' ')))
usbs = list(map(int, input().split(' ')))

nice = -1
for keyboard in keyboards:
    for usb in usbs:
        combo = keyboard + usb
        if s >= combo and nice < combo:
            nice = combo
print(nice)
        
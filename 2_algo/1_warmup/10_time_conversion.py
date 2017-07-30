import sys

time = input().strip()

h = int(time[:2])
r = time[2:-2]
ap = time[-2].lower()
if ap == 'a':
    print("{:02d}{}".format(h%12, r))
elif ap == 'p':
    print("{:02d}{}".format(((h%12)+12), r))
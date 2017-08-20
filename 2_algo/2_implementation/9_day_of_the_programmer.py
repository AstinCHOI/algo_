import calendar
year = int(input())

if (year == 1918):
    print('26.09.1918') # 256 - (31 + (28 - 13) + 31 + 30 + 31 + 30 + 31 + 31)
elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & calendar.isleap(year)):
    print('12.09.%s' % year)
else:
    print('13.09.%s' % year)

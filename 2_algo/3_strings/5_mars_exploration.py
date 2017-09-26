sos = input()
sosLen = len(sos)
typo = 0

# 1
# for i in range(0, sosLen-2, 3):
#    if sos[i] != 'S': typo += 1
#    if sos[i+1] != 'O': typo += 1
#    if sos[i+2] != 'S': typo += 1

# 2 from discussion
s = 'SOS'
for i in range(sosLen):
    if sos[i] != s[i%3]:
        typo += 1

print(typo)


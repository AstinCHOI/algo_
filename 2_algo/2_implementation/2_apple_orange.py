s, t = map(int, input().split(' ')) # house
a, b = map(int, input().split(' ')) # apple <-> org 
m, n = map(int, input().split(' ')) # apples, orgs
m_ = list(map(int, input().split(' ')))
n_ = list(map(int, input().split(' ')))

apps = list(map(lambda x: a + x, m_))
orgs = list(map(lambda x: b + x, n_))

A = 0
for app in apps:
    if app >= s and app <= t:
        A = A + 1
print(A)

B = 0
for org in orgs:
    if org >= s and org <= t:
        B = B + 1
print(B)

# O(n^n)
def combination(prefix, st, l):
    n = len(prefix)
    if n == l:
        print(prefix)
    else:
        for i in range(l):
            lst = len(st)
            if lst != l:
                st = st[i:] + st[i-1:i]
            combination(prefix + st[i], st, l)


if __name__ == '__main__':
    s = 'abc'
    combination('', s, len(s))
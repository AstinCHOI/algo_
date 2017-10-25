# O(n!)
def permutation(prefix, st):
    n = len(st)
    if n == 0:
        print(prefix)
    else:
        for i in range(n):
            permutation(prefix + st[i], st[:i] + st[i+1:])


if __name__ == '__main__':
    s = 'abcd'
    permutation('', s)
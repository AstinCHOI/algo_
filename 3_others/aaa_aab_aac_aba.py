def print_simple():
    data = ['a', 'b', 'c']
    data_len = len(data)

    for i in range(data_len):
      for j in range(data_len):
        for k in range(data_len):
          print(data[i] + data[j] + data[k], end=' ')
    print()

def baseto(num, base):
    st = ''
    tmp = num
    while tmp >= base:
        st = str(tmp % base) + st
        tmp = int(tmp / base)
    st += str(tmp)
    return st.zfill(base)

def print_string(s):
    le = len(s)
    for i in range(le**le):
        ba = baseto(i, le)
        for j in ba:
            print(s[int(j)], end='')
        print('', end=' ')
    print()

if __name__ == '__main__':
    # print(baseto(3, 3))
    print_string('abc')
    # print_simple()


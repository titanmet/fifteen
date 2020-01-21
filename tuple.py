def tuple1():
    t = (2.33, 6.7, 9.11, 23.65, 1.77, 7.3, 98.43, 34.21, 1.2, 5.67)
    print(max(t))
    print(min(t))


tuple1()


def thr_word():
    l = ['Earth', 'Russia', 'Moscow']
    print('{} -> {} -> {}'.format(l[0], l[1], l[2]))


thr_word()


def razb():
    list1 = []
    st = '/bin:/usr/bin:/usr/local/bin'
    for i in st.split(':'):
        list1.append(i)
    print(list1)


razb()


def delitel():
    for i in list(range(1, 101)):
        if i % 7 == 0:
            print(i)

delitel()


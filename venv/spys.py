def spys():
    spys = [1, 'slon', 56, True, 'serenada', 98]
    for i in spys:
        print(i, spys.index(i))


spys()


def spys_del():
    s = ['jaba', 'to-delete', 'slon', 'serenada', 'to-delete', 'sssr', 'to-delete']
    print(s)
    for i in s:
        if i == 'to-delete':
            s.remove(i)
    print(s)

spys_del()

def rev():
    s = list(range(1,11))
    print(s)
    s.reverse()
    print(s)

rev()
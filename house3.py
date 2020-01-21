def num():
    vvod = input("Number :")
    x = int(vvod)
    try:
        if x < 0:
            raise TypeError("Number < Zero")
        if x > 10:
            raise IndexError("Number > 10")
        if x % 2 == 0:
            raise ValueError("Even number")
    except ValueError:
        print("Even Number")
    except TypeError:
        print("Number < Zero")
    except IndexError:
        print("Number > 10")


# num()

def slist():
    list1 = [1, 3, 5, 7, 9, 12, 34, 56, 78, 89]
    vvod = input("Index list:")
    n = int(vvod)
    try:
        if n < len(list1) and n >= 0:
            print("Index, {}".format(n))
        elif n >= len(list1) or n < 0:
            raise IndexError("Not Index")
    except IndexError:
        print("Not Index")


# slist()

def two_number(n1, n2):
    if n1 > 0 and n2 > 0 and n1 != n2:
        print(n1 + n2)
    if n1 < 0 and n2 < 0:
        print(n1 - n2)
    if n1 == n2:
        print(0)


# two_number(5,5)

def two_number1(n1, n2):
    if n1 > 0 and n2 > 0 and n1 != n2:
        return n1 + n2
    if n1 < 0 and n2 < 0:
        return n1 - n2
    if n1 == n2:
        return 0


# print(two_number1(8,3))

def three_max(n1, n2, n3):
    list1 = [n1, n2, n3]
    list1.sort()
    print(list1[1], list1[2])


# three_max(3,1,7)

def func(*number, flag):
    list1 = []
    if flag == True:
        for n in number:
            if n % 2 == 0:
                list1.append(n)
    print(list1)

    list2 = []
    if flag == False:
        for m in number:
            if m % 2 > 0:
                list2.append(m)
    print(list2)

# func(12, 23, 5, 48, 10, 11, 46, flag=True)
# func(12, 23, 5, 7, 10, 11, 46, flag=False)

def fun_min_max(*number):
    list1=[]
    for i in number:
        list1.append(i)
    print('Max = {}'.format(max(list1)))
    print('Min = {}'.format(min(list1)))

# fun_min_max(2,4,1,34,87,11,55)

def str_case(strin,case=True):
    if case==True:
       print(strin.upper())
    else:
        print(strin.lower())

# str_case('sdsdffgdfgdsfg',True)
# str_case('sdsdffgdfgdsfg',False)

def fun_glue(*string,glue=':'):
    list1=[]
    for i in string:
        if len(i)>3:
            list1.append(i+glue)
    return glue.join(list1)

print(fun_glue('a', 'elefant', 'ass', 'almost','a','only'))
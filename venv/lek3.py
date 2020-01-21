# try:
#     print(1/0)
# except Exception:
#     print('0!!')
#
# try:
#     int('q')
# except ValueError:
#     print("Wrong value!")
#
# try:
#     1/0
# except ZeroDivisionError:
#     print('/0')
# def err():
#     try:
#         1 / int(input('x: '))
#     except ZeroDivisionError:
#         print('/0')
#     except TypeError:
#         print('Wrong type')
#     except ValueError:
#         print('Bad input')
#
# err()

# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print('Exeption ! Stop it!')
#     print(e)
#     print(e.with_traceback())
#

# try:
#     d = {'key': 23}
#     print(d['does not exist'])
# except KeyError as e:
#     print("Go it", e)
#
# try:
#     l = [1, 9]
#     l[3]
# except IndexError as e:
#     print('Out !',e)

# raise IndexError('Out !!!')
# raise ValueError('F1')

# try:
#     raise TypeError('Some message')
# except TypeError as e:
#     print(e)

try:
    print('Fine')
except KeyError:
    print('Nope.')
else:
    print('Else clause')

try:
    print(1/0)
except ZeroDivisionError:
    print('0!')
finally:
    print('I will be called')

try:
    raise ValueError()
finally:
    print('Finnaly!')
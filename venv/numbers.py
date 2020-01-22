
NUMBERS = [1, 4, 7, 9, 12, 15, 19]

def quest_true():
    while True:
        num = int(input("You number: ?"))
        if num in NUMBERS:
            print('You win, number: {}'.format(num))
            break
        print("Error")

def main():
    quest_true()


main()
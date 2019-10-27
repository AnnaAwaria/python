d = input("Podaj wysokośc choinki ")


def choinka(h):
    for x in range(h):
        print(' ' * (h - x - 1) + '*' * (2 * x + 1))


choinka(int(d))
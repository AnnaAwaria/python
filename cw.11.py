def dodaj(a, b, **kwargs):
    if 'verbosity' in kwargs:
        print('dodajemy')
    return a + b


a = dodaj(2, 3, verbosity=True)

print("hej")

print(a)

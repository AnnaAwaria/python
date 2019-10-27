z = []

for x in range(2000, 3001):
    if x % 7 == 0 and (x % 5 != 0):
        z.append(str(x))

print(','.join(z))

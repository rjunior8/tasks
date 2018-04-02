l = [1, 1.2, 2, 2.8, 3, 3.4, 4, 4.8, 5, 5.7, 6, 6.1]
c = 0

for n in l:
    if type(n) is int and c < 5:
        print(n)
        c += 1
n = int(input())

if n > 0:
    for i in range(2, n):
        c = 2
        primo = True
        while primo and c < i:
            if i % c == 0:
                primo = False
            else:
                c += 1
        if primo:
            print("{} é primo!".format(i))
else:
    print("Número errado!")
x = 2
y = 5.3

while True:
    e = int(input("Menu:\n1-adição\n2-subtração\n3-divisão\n4-multiplicação\n5-sair\nOpção: "))

    if e == 1:
        print("A soma de {} + {} = {}\n".format(x, y, x + y))
        continue
    elif e == 2:
        print("A subtração de {} + {} = {}\n".format(x, y, x - y))
        continue
    elif e == 3:
        print("A divisão de {} + {} = {}\n".format(x, y, x / y))
        continue
    elif e == 4:
        print("A multiplicação de {} + {} = {}\n".format(x, y, x * y))
        continue
    elif e == 5:
        print("Finalizado!")
        break
    else:
        print("Opção não disponível!\n")
        continue
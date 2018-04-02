while True:
    n = float(input("Digite uma nota entre 0 e 5: "))

    if n >= 0 and n <= 5:
        break
    else:
        print("Nota inválida!\n")
        continue
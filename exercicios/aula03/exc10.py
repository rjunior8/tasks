from calendar import month_name

d = {}
c = 0

for m in month_name:
    c += 1
    d.update({m : c})

data = input("Digite a data de seu nascimento: ")

data = data.split('/')
mes = int(data[1])

for key in d:
    if mes == d[key]:
        print(data[0], key, data[2])
        break
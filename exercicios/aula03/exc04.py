import calendar

l1 = []
l2 = []

for m in calendar.month_abbr:
    l1.append(m)

l1.remove(l1[0])

for t in l1:
    temp = float(input("Digite a temperatura do mês de {}: ".format(t)))
    l2.append(temp)

for i in range(len(l1)):
        print("{}: T° = {}°".format(l1[i], l2[i]))
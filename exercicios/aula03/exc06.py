from random import randint, uniform

c = 0
d = {}

for i in range(1, 30):
    idade = str(randint(4, 50))
    s = format(uniform(1, 2), ".2f")
    altura = float(s)
    d.update({idade : altura})

for age in d:
    if int(age) > 13 and d[age] < 1.60:
        c += 1

print("Total de alunos com mais de 13 anos com altura inferior à média: {}".format(c))
from math import pow

# дни за которые может с ними произойти событие
C = 6
# дни за которые может произойти событие с Полиной
D = 206

students = {
    "Polyna": 0,
    "Lesha": 0,
    "Sveta": 0
}

ans_chance = 1
for name, chance in students.items():
    n = input(f"Вероятность для {name}: ")
    chance = pow(1 - float(n), (1 / C))

    if name == "Polyna":
        ans_chance *= pow((1 - chance), D)
    else:
        ans_chance *= pow(chance, D)

print(ans_chance)

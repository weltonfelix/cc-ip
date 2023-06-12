name = input()
people_amount = int(input())
coeficient = float(input())

if people_amount % 2 == 0:  # even
    smokers = coeficient * (people_amount - 1) + 1
else:
    smokers = coeficient * (people_amount - 1) / 2

smokers_first_decimal_place = int((smokers % 1) * 10)

if smokers_first_decimal_place >= 1 and smokers_first_decimal_place <= 5:
    smokers = int(smokers // 1)
elif smokers_first_decimal_place > 5 and smokers_first_decimal_place <= 9:
    smokers = int(smokers // 1) + 1
else:
    smokers = int(smokers)

smokers_percentage = int(smokers * 100 / people_amount)

print(f"Vamos verificar se {name} vai fumar singaro!")
print(f"{smokers_percentage}% dos seus amigos fumam singaro")

if smokers_percentage < 25:
    print("Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde")
elif smokers_percentage > 25 and smokers_percentage < 50:
    print("Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde")
elif smokers_percentage > 50:
    print("TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!")

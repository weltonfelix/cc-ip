real_days = int(input())
houses = int(input())

# gasta 3 horas por dia
hours_spent = real_days * 3

# 24000 ticks = 20 min, mas na verdade 12000 ticks são gastos em 20 min, já que ele só trabalha de dia
# 12000   = 20 min
# x ticks = 60 min
ticks_in_hour = (12000 * 60) / 20
ticks_spent = ticks_in_hour * hours_spent

ticks_per_house = ticks_spent / houses

print(int(ticks_per_house))

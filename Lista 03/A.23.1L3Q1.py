creatures = []

n = int(input())

for i in range(n):
    name = input()
    if not (name in creatures):
        creatures.append(name)
    else:
        print("Criatura repetida")

print("Registradas:")
for creature in creatures:
    print(creature)

FAKE = "fake"
NATURAL = "natural"

people_amount = int(input())

people = {}

for _ in range(people_amount):
    person = {}

    data = input().split(" - ")
    name = data[0]

    data = data[1].split()
    person["profession"] = data[0]
    person["rating"] = data[1]
    person["month"] = int(data[2])

    people[name] = person

analysed_month = int(input())

fakes = {}

for name, person in people.items():
    if person["rating"] == FAKE and person["month"] == analysed_month:
        fakes[name] = person

fakes_names = fakes.keys()
fakes_names = sorted(fakes_names)

if len(fakes) > 0:
    print("Os fake nattys do mês são:")
    for name in fakes_names:
        print(f"{name} - {fakes[name]['profession']}")
else:
    print("Até agora não temos ninguém pra expor na internet neste mês :(")

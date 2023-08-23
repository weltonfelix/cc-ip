NATTY = "natty"
FAKE_NATTY = "FAKE NATTY"

people_amount = int(input())

people = []

for _ in range(people_amount):
    person_data = input().split(" - ")

    people.append(
        {
            "name": person_data[0],
            "rating": int(person_data[1]),
            "category": person_data[2],
        }
    )

natties = []
fake_natties = []

for person in people:
    if person["category"] == NATTY:
        natties.append(person)
    else:
        fake_natties.append(person)

natties = sorted(natties, key=lambda person: person["rating"], reverse=True)
fake_natties = sorted(fake_natties, key=lambda person: person["rating"], reverse=True)

for person in natties:
    print(f"{person['name']} - {person['rating']} - {person['category']}")

for person in fake_natties:
    print(f"{person['name']} - {person['rating']} - {person['category']}")

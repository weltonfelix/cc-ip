DIALECT_0 = "Oooh look at him"
DIALECT_1 = "Baseball bat"
DIALECT_2 = "Aesthetic"
DIALECT_3 = "Fake Natty"
DIALECT_4 = "Chris Bumbstead, o CBUM"
DIALECT_5 = "Pope Francis"
DIALECT_6 = "O suco vicia"
DIALECT_7 = "I don't know you tell me"
DIALECT_8 = "Não é mesmo?"
DIALECT_9 = "Rodrigo Goes out"

DIALECT_VALUES = {
    DIALECT_0: 0,
    DIALECT_1: 1,
    DIALECT_2: 2,
    DIALECT_3: 3,
    DIALECT_4: 4,
    DIALECT_5: 5,
    DIALECT_6: 6,
    DIALECT_7: 7,
    DIALECT_8: 8,
    DIALECT_9: 9,
}

people_amount = int(input())

people_people_ahead = []

for _ in range(people_amount):
    phrases = input().split("+")

    person_people_ahead = ""
    for phrase in phrases:
        person_people_ahead += str(DIALECT_VALUES[phrase])

    people_people_ahead.append(int(person_people_ahead))

people_people_ahead = sorted(people_people_ahead)

lines = []

is_possible = True

for person_people_ahead in people_people_ahead:
    if person_people_ahead == 0:
        lines.append(1)
    else:
        person_added = False
        for line in range(len(lines)):
            if lines[line] == person_people_ahead:
                lines[line] += 1
                person_added = True
                break

        if person_added == False:
            is_possible = False


print("YES" if is_possible else "NO")

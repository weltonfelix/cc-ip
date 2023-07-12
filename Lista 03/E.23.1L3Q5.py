n = int(input())

house = []

for _ in range(n):
    floor = []
    for _ in range(n):
        floor.append(input())

    house.append(floor)

for floor in house:
    print(" ".join(floor))

LOVED = "Amei!!"
TRY_AGAIN = "Acho que não combinou muito :/"
BAD = "Melhor escolher eu mesma"

hairs = input().split(" - ")
tops = input().split(" - ")
bottoms = input().split(" - ")
shoes = input().split(" - ")

# If the number of items is odd, the middle item is the integer division
# of the number of items by 2 + 1.
# If the number of items is even, the selected item is the number of items
# divided by 2 + 1 (first position after middle)
# Since the index starts at 0, subtract 1 in both cases.
current_hair_index = (
    (len(hairs) // 2 + 1) - 1 if len(hairs) % 2 == 1 else int((len(hairs) / 2) + 1) - 1
)

current_top_index = (
    (len(tops) // 2 + 1) - 1 if len(tops) % 2 == 1 else int((len(tops) / 2) + 1) - 1
)

current_bottom_index = (
    (len(bottoms) // 2 + 1) - 1
    if len(bottoms) % 2 == 1
    else int((len(bottoms) / 2) + 1) - 1
)

current_shoe_index = (
    (len(shoes) // 2 + 1) - 1 if len(shoes) % 2 == 1 else int((len(shoes) / 2) + 1) - 1
)

print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")

current_opinion = None

while current_opinion != LOVED and current_opinion != BAD:
    actions = input().split()

    print("Iniciando mesclagem...")

    for piece in range(len(actions)):
        if ">" in actions[piece]:
            delta = int(actions[piece].split(">")[0])
        else:
            delta = -int(actions[piece].split("<")[0])

        if piece == 0:
            current_hair_index = (current_hair_index + delta) % len(hairs)

        elif piece == 1:
            current_top_index = (current_top_index + delta) % len(tops)

        elif piece == 2:
            current_bottom_index = (current_bottom_index + delta) % len(bottoms)

        elif piece == 3:
            current_shoe_index = (current_shoe_index + delta) % len(shoes)

    print("O look gerado foi:")
    print(
        f"cabelo {hairs[current_hair_index]}, {tops[current_top_index]} com {bottoms[current_bottom_index]} e {shoes[current_shoe_index]} nos pés."
    )

    current_opinion = input()

if current_opinion == LOVED:
    if tops[current_top_index] == "camisa da seleção":
        print("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
    else:
        print("Essa Barbie vai arrasar com o look perfeito!")
else:
    print("Acho que estou precisando de ajustes, Ken :(")

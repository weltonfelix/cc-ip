desired_items = input().split(", ")
owned_items = input().split(", ")


owned_desired_items_counter = 0
for item in desired_items:
    if item in owned_items:
        owned_desired_items_counter += 1
        if owned_desired_items_counter == 1:
            print("Esses são os itens que já tenho em casa:")

        print(f"{owned_desired_items_counter}º item: {item}")

if owned_desired_items_counter == 0:
    print(
        f"Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {len(desired_items)} itens em casa."
    )
elif owned_desired_items_counter < len(desired_items):
    print(
        f"Irei precisar comprar {len(desired_items) - owned_desired_items_counter} itens antes do meu encontro!"
    )
elif owned_desired_items_counter == len(desired_items):
    print(
        f"Que ótimo, consegui encontrar cada um dos {owned_desired_items_counter} itens!"
    )

print("Isso é tudo! Hora de me preparar!")

arthur_offer = 10
luiz_offer = 30
pedro_offer = 100

diamonds = int(input())

if arthur_offer >= diamonds:
    print("Arthur")
elif luiz_offer >= diamonds:
    print("Luiz")
elif pedro_offer >= diamonds:
    print("Pedro")
else:
    print("Nenhum")

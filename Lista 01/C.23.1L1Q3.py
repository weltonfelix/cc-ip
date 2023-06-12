risk = int(input())

if risk <= 50:
    print("Ufa, finalmente posso tirar minhas férias!")
    destination = input()

    if destination == "Maceió":
        print("Bem que eu tava com saudade de uma boa praia!")
    elif destination == "Pipa":
        print("As noites em Pipa parecem muito animadas, to dentro!")
    elif destination == "Caruaru":
        print("Parece um local muito divertido para aproveitar as festas juninas!")
    elif destination == "Bonito":
        print("Praticar rapel nas cachoeiras vai ser demais!")
    else:
        print(f"Nunca ouvi falar sobre {destination}, mas me parece uma boa ideia!")
else:
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    hero = input()

    if hero == "Homem-Aranha":
        print("O amigo da vizinhança nunca me deixa em paz! Será derrotado!")
    elif hero == "Capitão América":
        print("Derrotar o carinha do escudo vai ser moleza!")
    elif hero == "Spider Gwen":
        print("A namoradinha do spidey nunca será capaz de me derrotar!")
    elif hero == "Hulk":
        print("Esse aí só sabe gritar e quebrar tudo, não será páreo para mim!")
    else:
        print(f"Não conheço esse herói {hero}. Preciso me preparar para essa batalha!")

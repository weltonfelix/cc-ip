personality1 = input()
personality2 = input()

person = input()

skill = input()

n1 = int(input())
n2 = int(input())
n3 = int(input())

passou = True
reason = ""

if passou and (personality1 != "Humildade" or personality2 != "Bondade"):
    passou = False
    reason = "personality"

if passou and (person != "Mary" and person != "Ninguem"):
    passou = False
    reason = "person"

if passou and (skill != "Dancar" and skill != "Lancar"):
    passou = False
    reason = "skill"

grade = (n1 + n2 + n3) / 3

if passou and grade < 7:
    passou = False
    reason = "grade"


if passou:
    print(
        "Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!"
    )
else:
    print(
        "Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!"
    )

    if reason == "personality":
        print("Infelizmente você não possui as característica necessárias!")
    elif reason == "person":
        print("Infelizmente você não está apaixonado pela pessoa certa!")
    elif reason == "skill":
        print("Infelizmente você não possui as habilidades necessárias!")
    elif reason == "grade":
        print("Infelizmente você não obteve um bom desempenho escolar!")

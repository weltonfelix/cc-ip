DOCTOR_TOOLS = ["Estetoscopio", "Esfigmomanometro", "Jaleco", "Caneta", "Celular"]
PROGRAMMER_TOOLS = ["Calculadora", "Oculos", "Notebook", "Camisa Social", "Caderno"]
BAKER_TOOLS = ["Rolo", "Caneta", "Avental", "Colher de Pau", "Caderno"]
ECONOMIST_TOOLS = ["Calculadora", "Caneta", "Camisa Social", "Agenda", "Celular"]
PERSONAL_TRAINER_TOOLS = ["Halter", "Agenda", "Celular", "Legging", "Corda"]

ALL_TOOLS = (
    DOCTOR_TOOLS
    + PROGRAMMER_TOOLS
    + BAKER_TOOLS
    + ECONOMIST_TOOLS
    + PERSONAL_TRAINER_TOOLS
)


ADD_ACTION = "Adicionar"
REMOVE_ACTION = "Retirar"
EXIT_ACTION = "Sair"

bag = []

expected_profession = input()
if expected_profession == "Medica":
    bag = DOCTOR_TOOLS.copy()
elif expected_profession == "Assistente de Informatica":
    bag = PROGRAMMER_TOOLS.copy()
elif expected_profession == "Padeira":
    bag = BAKER_TOOLS.copy()
elif expected_profession == "Economista":
    bag = ECONOMIST_TOOLS.copy()
elif expected_profession == "Personal Trainer":
    bag = PERSONAL_TRAINER_TOOLS.copy()

day_profession = input()
necessary_tools = []
if day_profession == "Medica":
    necessary_tools = DOCTOR_TOOLS.copy()
elif day_profession == "Assistente de Informatica":
    necessary_tools = PROGRAMMER_TOOLS.copy()
elif day_profession == "Padeira":
    necessary_tools = BAKER_TOOLS.copy()
elif day_profession == "Economista":
    necessary_tools = ECONOMIST_TOOLS.copy()
elif day_profession == "Personal Trainer":
    necessary_tools = PERSONAL_TRAINER_TOOLS.copy()

current_action = None

while current_action != EXIT_ACTION:
    current_action = input()
    if current_action == ADD_ACTION:
        item = input()
        if item in bag:
            print(f"Barbie, você já colocou {item} na bolsa")
        elif item in necessary_tools:
            bag.append(item)
            print(f"{item} adicionado à bolsa")
        elif item in ALL_TOOLS:
            print(f"Barbie, {item} não esta na lista de itens de {day_profession}")
    elif current_action == REMOVE_ACTION:
        item = input()

        if item in bag:
            if item not in necessary_tools:
                bag.remove(item)
                print(f"{item} retirado da bolsa")
            else:
                print(
                    f"Não faca isso Barbie, você precisa de {item} para trabalhar de {day_profession}"
                )
        else:
            print("Barbie, como você vai retirar algo que já não esta ai?")

sorted_bag = sorted(bag)

print(f"Itens na bolsa: {', '.join(sorted_bag)}")

delta_itens = 0
for item in bag:
    if item not in necessary_tools:
        delta_itens += 1
        print(
            f"Barbie, você esqueceu de tirar {item}, você não usa ele trabalhando de {day_profession}"
        )

for item in necessary_tools:
    if item not in bag:
        delta_itens -= 1
        print(f"Oh não!! Barbie, você esqueceu de pegar {item}!!")

if delta_itens == 0:
    print("Boa Barbie, foi na correria mas tudo deu certo!")

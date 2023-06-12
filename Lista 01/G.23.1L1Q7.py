feature1 = input()
cost_1 = int(input())

feature2 = input()
cost_2 = int(input())

feature3 = input()
cost_3 = int(input())

feature4 = input()
cost_4 = int(input())

feature5 = input()
cost_5 = int(input())

if feature1 == "novo lançador de teias":
    if feature2 != "NADA":
        print("Com calma, aranha")

    if feature2 == "lentes de visão avançada":
        print(
            "Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro"
        )

        if feature3 == "traje à prova de balas":
            print("UOU, só tente sair dessa vivo, vou otimizar a energia aqui")

ai_feature = "ativação de inteligência artificial"

if (
    feature1 == ai_feature
    or feature2 == ai_feature
    or feature3 == ai_feature
    or feature4 == ai_feature
    or feature5 == ai_feature
):
    print("Espero que não esteja ativando isso para usar nas provas")

total_cost = cost_1 + cost_2 + cost_3 + cost_4 + cost_5

if total_cost >= 80:
    print("Vou descarregar em questão de minutos, pare AGORA")

if (
    (
        feature1 == "membranas planadoras"
        or feature2 == "membranas planadoras"
        or feature3 == "membranas planadoras"
        or feature4 == "membranas planadoras"
        or feature5 == "membranas planadoras"
    )
    and (
        feature1 == "novo lançador de teias"
        or feature2 == "novo lançador de teias"
        or feature3 == "novo lançador de teias"
        or feature4 == "novo lançador de teias"
        or feature5 == "novo lançador de teias"
    )
    and (
        feature1 == "ativação de inteligência artificial"
        or feature2 == "ativação de inteligência artificial"
        or feature3 == "ativação de inteligência artificial"
        or feature4 == "ativação de inteligência artificial"
        or feature5 == "ativação de inteligência artificial"
    )
):
    print("Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa")

print(f"Aranha, nessa sequência você usou {total_cost} de energia!")

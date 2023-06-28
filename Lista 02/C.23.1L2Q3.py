EVENT_END = "O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas"
MATCH_END = "Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores"
MATCH_START = "Encham o cooler! O jogo vai começar!!!!"
MATCH_TIMEOUT = (
    "Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários"
)

bottles = 20

status = ""

while status != EVENT_END and bottles >= 0:
    status = input()

    if status == MATCH_END:
        players = int(input())

        if bottles >= players:
            bottles -= players
        else:
            print(
                f"Não teremos água para todos os jogadores... Temos que garantir {players-bottles} garrafas!!"
            )
            bottles *= 2
            bottles -= players
    elif status == MATCH_START:
        bottles += 15
        print("Geladeira cheia!")
    elif status == MATCH_TIMEOUT:
        for volunteer in range(1, 6):
            bottles -= int(input())

        if bottles < 0:
            print(
                f"Faltaram {-bottles} garrafas para atender o pedido feito aos voluntários"
            )

    if bottles < 0:
        print("Por questões logísticas, teremos que acabar com os jogos...")

if bottles > 0:
    print(f"Sobraram {bottles} garrafas, vamos guardar na geladeira :D")
elif bottles == 0:
    print("Vendemos todas as garrafas! Nosso planejamento foi perfeito!")

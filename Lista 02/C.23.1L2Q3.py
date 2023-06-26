EVENT_END = "O InterCIn acabou!!! Vamos ver nosso estoque de bebidas"
MATCH_END = "Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores"
MATCH_START = "Encham o cooler, vai começar um jogo!!!!"
MATCH_TIMEOUT = (
    "Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário"
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
            print(f"Prometemos distribuir {-bottles} garrafas e zeramos")

    if bottles < 0:
        print("Por questões logísticas, teremos que acabar com os jogos...")

if bottles > 0:
    print(f"Notícia boa: sobraram {bottles} garrafas, vamos guardar na geladeira :D")
elif bottles == 0:
    print("Vendemos todas as águas, fizemos uma contagem certeira!!")
else:
    print(f"Estamos devendo {-bottles} garrafas para os alunos...")

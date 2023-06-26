matches = int(input())

ip_won_matches = 0
opponent_won_matches = 0

current_match = 1
stopped = False
while current_match <= matches and not stopped:
    is_final = current_match == matches
    rounds = int(input())

    ip_won_rounds = 0
    opponent_won_rounds = 0

    if not is_final:
        print(
            f"Vai começar a {current_match}º partida. Esse jogo terá {rounds} rodada(s)."
        )
    else:
        print(f"Tá na hora da grande final! Esse jogo terá {rounds} rodada(s).")

    for round in range(1, rounds + 1):
        ip_player_power = int(input())
        opponent_player_power = int(input())

        if opponent_player_power > ip_player_power:
            opponent_won_rounds += 1
        else:
            ip_won_rounds += 1

    print(f"Fim de jogo! O placar foi {ip_won_rounds}x{opponent_won_rounds}")

    if not is_final:
        if ip_won_rounds == opponent_won_rounds or opponent_won_rounds > ip_won_rounds:
            print("Não foi dessa vez! Treinar pro ano que vem!")
            stopped = True
        elif ip_won_rounds >= (opponent_won_rounds + 5) and current_match != matches:
            print(
                "QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!"
            )
            stopped = True
        else:
            print("Vamos para próxima fase!")
    else:
        if ip_won_rounds == opponent_won_rounds or opponent_won_rounds > ip_won_rounds:
            print("Ah não!! Chegaram tão longe mas não foi dessa vez. :(")
        else:
            print("É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!")

    current_match += 1

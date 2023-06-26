team1_member1 = input()
team1_member2 = input()

team2_member1 = input()
team2_member2 = input()

matches = int(input())

print(f"VAMO VER QUEM VAI COMER GRAMA! TEREMOS {matches} PARTIDAS ENTRE:")
print(f"{team1_member1} e {team1_member2} X {team2_member1} e {team2_member2}")

team1_wins = 0
team1_total_score = 0

team2_wins = 0
team2_total_score = 0

current_match = 1
stopped = False
while current_match <= matches and not stopped:
    team1_match_score = int(input())
    team2_match_score = int(input())

    if team1_match_score == 0:
        stopped = True
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")

    if team2_match_score == 0:
        stopped = True
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")

    team1_total_score += team1_match_score
    team2_total_score += team2_match_score

    if team2_match_score > team1_match_score:
        team2_wins += 1
    else:
        team1_wins += 1

    current_match += 1

if not stopped:
    team1_final_coeficient = team1_total_score * (team1_wins / matches)
    team2_final_coeficient = team2_total_score * (team2_wins / matches)

    print(
        f"CARAMBA! Tivemos um total de {team1_total_score + team2_total_score} bolas ao chão ao longo dessa disputa."
    )

    if team2_final_coeficient > team1_final_coeficient:
        print(f"{team2_member1} e {team2_member2} são os grandes vencedores!")
        print(f"Mataram {team2_total_score} bolas, ganhando {team2_wins} partidas")
    else:
        print(f"{team1_member1} e {team1_member2} são os grandes vencedores!")
        print(f"Mataram {team1_total_score} bolas, ganhando {team1_wins} partidas")

team_1 = input()
team_2 = input()

game = 1
team_1_victories = 0
team_2_victories = 0
while(game <= 5 and (team_1_victories < 3 and team_2_victories < 3)):
    team_1_points = int(input())
    team_2_points = int(input())

    if team_1_points > team_2_points:
        team_1_victories += 1
        print(f"O vencedor da {game}ª rodada foi: {team_1}")
    else:
        team_2_victories += 1
        print(f"O vencedor da {game}ª rodada foi: {team_2}")

    if team_1_victories >= 3:
      print(f"O time {team_1} ganhou a partida final!")
    elif team_2_victories >= 3:
      print(f"O time {team_2} ganhou a partida final!")
    
    game += 1
  
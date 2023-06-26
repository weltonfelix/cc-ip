n = int(input())

current_winner_name = None
current_winner_points = -1

for i in range(0,n):
  name = input()
  points = int(input())
  penalties = int(input())

  final_points = points - penalties

  if final_points > current_winner_points:
    current_winner_points = final_points
    current_winner_name = name

print(f"O grande vencedor do torneio foi {current_winner_name} com um total de {current_winner_points} pontos!")
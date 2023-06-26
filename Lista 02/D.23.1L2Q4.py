n = int(input())

winners_name = None
winners_score = -1
losers_name = None
losers_score = -1

for i in range(0, n):
    name = input()
    semester = int(input())
    score = int(input())

    final_score = score / semester

    if final_score > winners_score:
        winners_name = name
        winners_score = final_score

    if losers_score < 0 or final_score < losers_score:
        losers_name = name
        losers_score = final_score

print(
    f"A dupla vencedora foi {winners_name} com a pontuação final de {winners_score:.2f} pontos."
)

print(
    f"A dupla perdedora foi {losers_name} com a pontuação final de {losers_score:.2f} pontos."
)

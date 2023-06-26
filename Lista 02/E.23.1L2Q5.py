MANCHESTER_CIN = "Manchester CIn"
SPICIN_GIRLS = "SpiCIn Girls"

n = int(input())

manchester_cin_total_score = 0
spicin_girls_total_score = 0

i = 0
while i < n and (manchester_cin_total_score >= 0 and spicin_girls_total_score >= 0):
    i += 1

    name = input()
    goals = int(input())
    shots = int(input())
    yellow_cards = int(input())
    red_cards = int(input())

    score = (goals * 10) + (shots * 3) + (yellow_cards * -2) + (red_cards * -4)

    if goals >= shots * 0.3:
        score += 3

    if red_cards >= yellow_cards:
        score -= 3

    if name == MANCHESTER_CIN:
        manchester_cin_total_score += score
        if manchester_cin_total_score < 0:
            print(
                f"O time {MANCHESTER_CIN} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro."
            )
    elif name == SPICIN_GIRLS:
        spicin_girls_total_score += score
        if spicin_girls_total_score < 0:
            print(
                f"O time {SPICIN_GIRLS} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro."
            )

if manchester_cin_total_score >= 0 and spicin_girls_total_score >= 0:
    total_score = manchester_cin_total_score + spicin_girls_total_score

    manchester_cin_final_score_percentage = (
        manchester_cin_total_score / total_score
    ) * 100
    spicin_girls_final_score_percentage = (spicin_girls_total_score / total_score) * 100

    if manchester_cin_final_score_percentage > spicin_girls_final_score_percentage:
        print(
            f"Com {manchester_cin_final_score_percentage:.2f}% dos pontos, o time {MANCHESTER_CIN} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn."
        )
    else:
        print(
            f"Com {spicin_girls_final_score_percentage:.2f}% dos pontos, o time {SPICIN_GIRLS} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn."
        )

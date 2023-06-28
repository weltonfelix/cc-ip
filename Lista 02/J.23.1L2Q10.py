student_name = input()
professor_name = input()

print("E agora, só pela resenha:")
print(f"Melhor de 3 entre: {student_name} e {professor_name}!")
print("COMEÇOU!")

student_wins = 0
professor_wins = 0

ended = False

match = 0
while match <= 3 and student_wins < 2 and professor_wins < 2:
    student_score = 0
    professor_score = 0

    student_won = False
    professor_won = False
    while not (student_won or professor_won):
        result = int(input())
        if result % 2 == 0:
            professor_score += 1
        else:
            student_score += 1

        print(f"{student_score} - {professor_score}")

        if student_score >= 11 and (student_score >= professor_score + 2):
            student_won = True
        elif professor_score >= 11 and (professor_score >= student_score + 2):
            professor_won = True

    if student_won:
        print(f"{student_name} ganhou esta partida!")
        student_wins += 1
    elif professor_won:
        print(f"{professor_name} ganhou esta partida!")
        professor_wins += 1

    print(f"Placar: {student_name} [{student_wins}-{professor_wins}] {professor_name}")

print("FIM DA SÉRIE!")

if student_wins > professor_wins:
    print(f"{student_name} ganhou a série! Puro talento!")
else:
    print(f"{professor_name} ganhou a série! A experiência ganhou!")

encrypted_clue = int(input())

if encrypted_clue % 2 == 0:  # even
    clue = (encrypted_clue / 2) ** (1 / 2) + 2
else:
    clue = encrypted_clue / 3 + 3

movie_1 = input()
movie_2 = input()
movie_3 = input()

fatigue = 0

found_stan = True

if (
    movie_1 != "Coringa"
    and movie_1 != "Batman vs Superman"
    and movie_1 != "O Cavaleiro das Trevas"
):
    if movie_1 == "Vingadores: Ultimato":
        fatigue += 2
    else:
        fatigue += 1

    if len(movie_1) != clue:
        print("Miles: Tou frio, melhor ir procurar nas fases mais antigas")
        if movie_2 == "Vingadores: Ultimato":
            fatigue += 2
        else:
            fatigue += 1

        if len(movie_2) != clue:
            print("Gwen: Cadê o velho??? Queria um autógrafo")
            if movie_3 == "Vingadores: Ultimato":
                fatigue += 2
            else:
                fatigue += 1

            if len(movie_3) != clue:
                found_stan = False

    if found_stan:
        print("Miles: Achei o easter egg!!!")
        spider_movie = input()
        spider_duration = int(input())

        if fatigue >= 2 and spider_duration >= 135:
            print("Miles: A mimir")
        elif fatigue >= 2 and spider_duration >= 120:
            print("Gwen: Nada que uma xícara de café não resolva!")
        else:
            print(f"Peter: {spider_movie} é o melhor filme do homem aranha, 10/10")
    else:
        print(
            "Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair..."
        )
else:
    print("Algo de errado não está certo!")

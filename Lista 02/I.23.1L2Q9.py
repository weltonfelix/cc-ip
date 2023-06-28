SCORE_GOAL = 10
CROWD_RATE = 0.8

playlist_duration = int(input())

d = 1
stopped = False

while d <= 3 and not stopped:
    print(f"Dia {d} do InterCIn")

    day_songs = int(input())

    best_daily_song_name = None
    best_daily_song_score = -1

    daily_crowd_score = 0

    song = 1
    while song <= day_songs:
        song_name = input()

        song_duration_s = int(input())
        song_score = int(input())

        playlist_duration -= song_duration_s

        if playlist_duration < 0:
            stopped = True
        elif playlist_duration == 0:
            if d != 3:
                stopped = True
            elif song != day_songs:
                stopped = True

        daily_crowd_score += int((song_score * CROWD_RATE) // 1)

        if song_score > best_daily_song_score:
            best_daily_song_name = song_name
            best_daily_song_score = song_score

        song += 1

    print(f"A música mais animada do dia foi {best_daily_song_name}")

    goal_achieved = daily_crowd_score >= SCORE_GOAL

    if d < 3:
        if not goal_achieved:
            SCORE_GOAL = 10 + (SCORE_GOAL - daily_crowd_score)
            print(
                f"Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {SCORE_GOAL} pontos de animação no outro dia"
            )
        else:
            SCORE_GOAL = 10
    elif not goal_achieved:
        print("Valeu a tentativa, na próxima vai dar bom")

    if stopped:
        print(
            "Estava animado, mas a playlist acabou antes do evento terminar e todo mundo ficou muito triste :("
        )
    elif d == 3:
        if not goal_achieved:
            print(
                "A playlist estava boa, mas não foi o suficiente para animar o evento"
            )
        else:
            print("A playlist estava incrível demais!")

    d += 1

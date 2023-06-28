OPPONENT_POINTS = 18

member_top = None
member_top_elo_points = -1

member_jungler = None
member_jungler_elo_points = -1

member_mid = None
member_mid_elo_points = -1

member_adc = None
member_adc_elo_points = -1

member_support = None
member_support_elo_points = -1

member_1_announcement = None
member_2_announcement = None
member_3_announcement = None
member_4_announcement = None
member_5_announcement = None
current_member = 0

artur_in_team = False
frej_in_team = False

stopped = False

while (
    not (member_top and member_jungler and member_mid and member_adc and member_support)
    and not stopped
):
    name = input()
    if name != "Bruna":
        lane = input()
        elo = input()

        elo_points = 0

        if elo == "Bronze":
            elo_points = 1
        elif elo == "Prata":
            elo_points = 2
        elif elo == "Ouro":
            elo_points = 4
        elif elo == "Platina":
            elo_points = 6
        elif elo == "Diamante":
            elo_points = 8
        elif elo == "Desafiante":
            elo_points = 10
        else:
            elo_points = 0
            print("Não conheço esse elo, então vou considerar que é um elo ruim.")

        accepted = False

        if lane == "Top":
            if not member_top:
                member_top = name
                member_top_elo_points = elo_points
                accepted = True
        elif lane == "Jungler":
            if not member_jungler:
                member_jungler = name
                member_jungler_elo_points = elo_points
                accepted = True
        elif lane == "Mid":
            if not member_mid:
                member_mid = name
                member_mid_elo_points = elo_points
                accepted = True
        elif lane == "Adc":
            if not member_adc:
                member_adc = name
                member_adc_elo_points = elo_points
                accepted = True
        elif lane == "Suporte":
            if not member_support:
                member_support = name
                member_support_elo_points = elo_points
                accepted = True

        if accepted:
            current_member += 1
            if current_member == 1:
                member_1_announcement = f"{name} - {lane} ({elo})"
            elif current_member == 2:
                member_2_announcement = f"{name} - {lane} ({elo})"
            elif current_member == 3:
                member_3_announcement = f"{name} - {lane} ({elo})"
            elif current_member == 4:
                member_4_announcement = f"{name} - {lane} ({elo})"
            elif current_member == 5:
                member_5_announcement = f"{name} - {lane} ({elo})"

            print(f"{name} entrou pro time.")
            if name == "Artur":
                artur_in_team = True
                print("Ele tá meio enferrujado...")
            elif name == "Frej":
                frej_in_team = True
                print("Joga muito!")
        else:
            print(f"{name} não foi aceito, que pena.")

    else:
        stopped = True
        print("LOL NÃO!!! TUDO MENOS LOL!!!")

if not stopped:
    print("O time está completo.")
    print(member_1_announcement)
    print(member_2_announcement)
    print(member_3_announcement)
    print(member_4_announcement)
    print(member_5_announcement)

    team_total_points = (
        member_adc_elo_points
        + member_mid_elo_points
        + member_jungler_elo_points
        + member_support_elo_points
        + member_top_elo_points
    )

    if (frej_in_team and artur_in_team) or (not frej_in_team and not artur_in_team):
        if team_total_points >= OPPONENT_POINTS:
            print("A GENTE VAI GANHAR!!!")
        else:
            print("Vai dar ruim...")
    elif artur_in_team:
        print("Vai dar ruim...")
    elif frej_in_team:
        print("A GENTE VAI GANHAR!!!")

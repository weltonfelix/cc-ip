# eventEnded, thursters, thurster_speed, droid
def handle_competitor_events(thrusters, thruster_speed):
    event = None
    while not (event == "Próximo" or event == "FIM"):
        event = input()

        if event == "Pit-Stop Espacial":
            thrusters += 1
        elif (
            event
            == "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra."
        ):
            thrusters -= 1
            if thrusters == 0:
                return False, 0, 0, False
        elif (
            event
            == "Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1..."
        ):
            return False, thrusters, thruster_speed, True
        elif event == "FIM":
            return True, thrusters, thruster_speed, False

    return False, thrusters, thruster_speed, False


def process_competitor(name, initial_thrusters, initial_thruster_speed):
    (
        eventEnd,
        final_thrusters,
        final_thruster_speed,
        is_droid,
    ) = handle_competitor_events(initial_thrusters, initial_thruster_speed)

    if is_droid:
        print(
            f"O {name} achou que não descobriríamos, tirem {name} imediatamente da pista."
        )
    elif final_thrusters == 0:
        print(f"BUUMM!! Infelizmente, {name} está fora da corrida.")
    else:
        initial_speed = initial_thruster_speed * initial_thrusters
        final_speed = final_thruster_speed * final_thrusters

        print(f"--- Participante: {name} ---")
        print(f"Qtd de propulsores Final: {final_thrusters}")
        print(f"Velocidade Inicial: {initial_speed} km/h")
        print(f"Velocidade Final: {final_speed} km/h")

    return eventEnd, is_droid or final_thrusters == 0


def main():
    eventEnd = False
    participants = 0
    disqualified_participants = 0

    while not eventEnd:
        user_input = input().split()
        if len(user_input) == 1:
            if user_input[0] == "FIM":
                eventEnd = True
        elif len(user_input) == 3:
            name, initial_thrusters, initial_thruster_speed = user_input
            initial_thrusters = int(initial_thrusters)
            initial_thruster_speed = int(initial_thruster_speed)

            eventEnd, disqualified = process_competitor(
                name, initial_thrusters, initial_thruster_speed
            )

            participants += 1
            if disqualified:
                disqualified_participants += 1

    if disqualified_participants == participants:
        print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")
    else:
        print(
            f"Relatório da CIn Pod Race: {participants - disqualified_participants} participantes terminaram a corrida e {disqualified_participants} foram desclassificados."
        )


main()

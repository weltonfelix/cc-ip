UP = "cima"
DOWN = "baixo"
LEFT = "esquerda"
RIGHT = "direita"

EMPTY = "-"
PLAYER = "V"
SCALPER = "C"
POPCORN = "P"
BARBIE_DOOR = "B"
OPPENHEIMER_DOOR = "O"

game_map = [[EMPTY for i in range(8)] for i in range(8)]

scalper_found = False
popcorn_found = False
popcorn_found_in_last_round = False
popcorn_destroyed = False
watching_oppenheimer = False
watching_barbie = False

player_coordinates = [0, 0]
scalper_coordinates = [0, 0]
popcorn_coordinates = [0, 0]
barbie_coordinates = [0, 0]
oppenheimer_coordinates = [0, 0]

player_coordinates[1] = int(input())
player_coordinates[0] = int(input())
scalper_coordinates[1] = int(input())
scalper_coordinates[0] = int(input())
popcorn_coordinates[1] = int(input())
popcorn_coordinates[0] = int(input())
barbie_coordinates[1] = int(input())
barbie_coordinates[0] = int(input())
oppenheimer_coordinates[1] = int(input())
oppenheimer_coordinates[0] = int(input())

game_map[barbie_coordinates[1]][barbie_coordinates[0]] = BARBIE_DOOR
game_map[oppenheimer_coordinates[1]][oppenheimer_coordinates[0]] = OPPENHEIMER_DOOR
game_map[popcorn_coordinates[1]][popcorn_coordinates[0]] = POPCORN
game_map[player_coordinates[1]][player_coordinates[0]] = PLAYER
game_map[scalper_coordinates[1]][scalper_coordinates[0]] = SCALPER

while not scalper_found and not watching_oppenheimer and not watching_barbie:
    if player_coordinates[0] > scalper_coordinates[0]:
        scalper_coordinates[0] += 1
    elif player_coordinates[0] < scalper_coordinates[0]:
        scalper_coordinates[0] -= 1
    elif player_coordinates[1] > scalper_coordinates[1]:
        scalper_coordinates[1] += 1
    elif player_coordinates[1] < scalper_coordinates[1]:
        scalper_coordinates[1] -= 1

    if scalper_coordinates == popcorn_coordinates:
        popcorn_destroyed = True

    if scalper_coordinates == player_coordinates:
        scalper_found = True
    else:
        move = input()
        if not popcorn_found_in_last_round:
            if move == UP and player_coordinates[1] > 0:
                player_coordinates[1] -= 1
            elif move == DOWN and player_coordinates[1] < 7:
                player_coordinates[1] += 1
            elif move == LEFT and player_coordinates[0] > 0:
                player_coordinates[0] -= 1
            elif move == RIGHT and player_coordinates[0] < 7:
                player_coordinates[0] += 1
        else:
            popcorn_found_in_last_round = False

    game_map = [[EMPTY for i in range(8)] for i in range(8)]

    game_map[barbie_coordinates[1]][barbie_coordinates[0]] = BARBIE_DOOR
    game_map[oppenheimer_coordinates[1]][oppenheimer_coordinates[0]] = OPPENHEIMER_DOOR
    if not popcorn_destroyed and not popcorn_found:
        game_map[popcorn_coordinates[1]][popcorn_coordinates[0]] = POPCORN
    game_map[player_coordinates[1]][player_coordinates[0]] = PLAYER
    game_map[scalper_coordinates[1]][scalper_coordinates[0]] = SCALPER

    for line in game_map:
        print(" ".join(line))

    if player_coordinates == barbie_coordinates:
        watching_barbie = True
    elif player_coordinates == oppenheimer_coordinates:
        watching_oppenheimer = True
    elif player_coordinates == scalper_coordinates:
        scalper_found = True
    else:
        if popcorn_found:
            print("Já peguei a pipoca")
        elif player_coordinates == popcorn_coordinates and not popcorn_destroyed:
            popcorn_found = True
            popcorn_found_in_last_round = True
            print("Finalmente! Peguei a pipoca")
        else:
            print("Ainda não achei a pipoca")

        scalper_distance = pow(
            pow(player_coordinates[0] - scalper_coordinates[0], 2)
            + pow(player_coordinates[1] - scalper_coordinates[1], 2),
            0.5,
        )

        if scalper_distance <= 3:
            print("Preciso acelerar, o cambista tá na minha cola!")
        elif scalper_distance <= 4:
            print("Consigo ver lá longe o cambista, mas é melhor acelerar!")
        else:
            print("O cambista está longe, mas não posso ficar parado")

        print("")

    if scalper_found:
        print("Droga! Agora volto pra casa sem filme e sem dinheiro.")
    elif not popcorn_found and (watching_barbie or watching_oppenheimer):
        print(
            "Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha."
        )
    elif watching_barbie:
        print(
            "A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?"
        )
    elif watching_oppenheimer:
        print("Aí sim, que filmaço! Christopher Nolan nunca erra!")

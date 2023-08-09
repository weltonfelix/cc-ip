COIN = "◇"
SWORD = "espada"
ZELDA = "Zelda"
AGAHNIM = "Agahnim"

rooms = int(input())

map = []


def load_map(current_map, rooms_left):
    if rooms_left == 0:
        return current_map
    else:
        current_map_copy = current_map.copy()
        room = input().split(" - ")
        current_map_copy.append(room)

        return load_map(current_map_copy, rooms_left - 1)


map = load_map([], rooms)

initial_room = int(input())


def explore_map(map, room, coins, initial_room, visited_rooms=[], has_sword=False):
    next_room, coins, has_sword = explore_room(
        map[room], 0, coins=coins, visited_rooms=visited_rooms, has_sword=has_sword
    )

    if room != initial_room:
        visited_rooms.append(room)

    if ZELDA in map[room]:
        if AGAHNIM in map[room]:
            if has_sword:
                return True, visited_rooms
            else:
                return False, visited_rooms
        else:
            return True, visited_rooms
    elif next_room == -1:
        return False, visited_rooms
    elif next_room == initial_room:
        return False, visited_rooms
    else:
        return explore_map(
            map, next_room, coins, initial_room, visited_rooms, has_sword=has_sword
        )


def explore_room(room, position, coins, visited_rooms=[], has_sword=False):
    if position > len(room) - 1:
        return -1, coins, has_sword
    if room[position] == COIN:
        return explore_room(
            room,
            position + 1,
            coins + 1,
            visited_rooms=visited_rooms,
            has_sword=has_sword,
        )
    elif room[position] == SWORD:
        return explore_room(
            room, position + 1, coins, visited_rooms=visited_rooms, has_sword=True
        )
    elif (
        room[position] == ZELDA
        or room[position] == AGAHNIM
        or int(room[position]) in visited_rooms
    ):
        return explore_room(
            room, position + 1, coins, visited_rooms=visited_rooms, has_sword=has_sword
        )
    else:
        return int(room[position]), coins, has_sword


rescued, visited_rooms = explore_map(map, initial_room, 0, initial_room, [], False)

visited_rooms.append(initial_room)


def count_coins(map, visited_rooms, current_coins=0, current_visited_room=0):
    if current_visited_room >= len(visited_rooms):
        return current_coins
    else:
        coins = map[visited_rooms[current_visited_room]].count(COIN)
        return count_coins(
            map,
            visited_rooms,
            current_coins=current_coins + coins,
            current_visited_room=current_visited_room + 1,
        )


collected_coins = count_coins(map, visited_rooms)

if rescued:
    print(
        f"A princesa Zelda está a salvo e ainda conseguimos coletar {collected_coins} rupees"
    )
else:
    print(
        f"Infelizmente a princesa ainda corre perigo, mas temos {collected_coins} rupees para nos ajudar nas buscas"
    )

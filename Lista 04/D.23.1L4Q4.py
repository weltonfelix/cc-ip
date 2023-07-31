def check_astrounaut_condition(astrounaut_coords, explosion_coords, explosion_radius):
    distance = (
        (explosion_coords[0] - astrounaut_coords[0]) ** 2
        + (explosion_coords[1] - astrounaut_coords[1]) ** 2
    ) ** (1 / 2)

    return True if distance > explosion_radius else False


def check_capsule(capsule, explosion_coords, explosion_radius):
    living_astronauts = []
    x_sum = 0
    y_sum = 0
    for astronaut in capsule:
        is_alive = check_astrounaut_condition(
            astronaut, explosion_coords, explosion_radius
        )
        living_astronauts.append(is_alive)
        if is_alive:
            x_sum += astronaut[0]
            y_sum += astronaut[1]

    return living_astronauts, [
        x_sum / sum(living_astronauts) if sum(living_astronauts) > 0 else 0,
        y_sum / sum(living_astronauts) if sum(living_astronauts) > 0 else 0,
    ]


def rescue_astronauts():
    capsules = eval(input())
    explosion_position = eval(input())
    explosion_radius = int(input())

    living_astrounauts = 0
    capsules_central_positions = []
    for capsule in capsules:
        astrounauts_condiditions, central_position = check_capsule(
            capsule, explosion_position, explosion_radius
        )
        living_astrounauts += sum(astrounauts_condiditions)
        if sum(astrounauts_condiditions) > 0:
            capsules_central_positions.append(central_position)

    print([living_astrounauts, capsules_central_positions])


rescue_astronauts()

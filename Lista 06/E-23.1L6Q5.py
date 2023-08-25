ADD_SUSPECT = "Adicionar suspeito"
UPDATE_SUSPECT = "Atualizar suspeito"
REMOVE_SUSPECT = "Remover suspeito"
JUDGE_SUSPECT = "Julgamento"
RESULT = "NattyMeter"
END = "FIM"

BICEPS = "Biceps"
TRAIN_TIME = "Treino"
FREQUENCY = "Frequencia"
BODY_FAT = "BF"
SWEAT = "Suor"

HOUR = "hora"
MINUTE = "minuto"

SWEAT_DRY = "Seco"

SUSPECT_NOT_FOUND = "Quem é esse crazy man? Não tá aqui na database"
NATURAL = "Natural"
FAKE_NATTY = "FAKE NATTY! USOU O SUCO!"

NATTYMETER_STARTED = "NattyMeter, ON!"

suspects_set = {}


def get_suspect(name):
    return suspects["suspects"].get(name)


def add_suspect(name):
    if get_suspect(name) is None:
        suspects["suspects"][name] = {}


def update_suspect(name, property, value):
    if get_suspect(name) is None:
        return False

    suspects["suspects"][name][property] = value
    return True


def remove_suspect(name):
    return suspects["suspects"].pop(name, None)


def judge_suspect(name):
    suspect = get_suspect(name)
    if suspect is None:
        return None

    biceps_size = suspect.get(BICEPS)
    train_time = suspect.get(TRAIN_TIME)
    frequency = suspect.get(FREQUENCY)
    body_fat = suspect.get(BODY_FAT)
    sweat = suspect.get(SWEAT)

    evidences = 0
    if biceps_size is not None and biceps_size > 45:
        evidences += 1
    if train_time is not None and train_time < 30 * 60:  # in seconds
        evidences += 1
    if frequency is not None and frequency < 4:
        evidences += 1
    if body_fat is not None and body_fat < 0.1:
        evidences += 1
    if not sweat:
        evidences += 1

    return evidences >= 3


def get_result():
    suspects_names = suspects["suspects"].keys()
    fake_natties = 0
    for name in suspects_names:
        if judge_suspect(name):
            fake_natties += 1

    if len(suspects_names) == 0:
        return 0

    return fake_natties / len(suspects_names)


suspects = {
    "suspects": suspects_set,
    "add": add_suspect,
    "get": get_suspect,
    "remove": remove_suspect,
    "update": update_suspect,
    "judge": judge_suspect,
    "result": get_result,
}


def handle_add_suspect():
    name = input()
    suspects["add"](name)
    print(f"Novo suspeito: {name}")


def handle_update_suspect():
    name, data = input().split("-> ")
    if suspects["get"](name) is None:
        print(SUSPECT_NOT_FOUND)
    else:
        props = data.split(", ")

        for prop_data in props:
            prop, value = prop_data.split(": ")
            if prop == BICEPS:
                value = int(value[:-2])
            elif prop == TRAIN_TIME:
                value, unit = value.split(" ")
                value = int(value)
                if MINUTE in unit:
                    value = value * 60  # in seconds
                elif HOUR in unit:
                    value = value * 60 * 60  # in seconds
            elif prop == FREQUENCY:
                value = int(value.split(" ")[0])
            elif prop == BODY_FAT:
                value = int(value[:-1]) / 100
            elif prop == SWEAT:
                if value == SWEAT_DRY:
                    value = False
                else:
                    value = True

            if not suspects["update"](name, prop, value):
                print(SUSPECT_NOT_FOUND)


def handle_remove_suspect():
    name = input()
    if suspects["remove"](name) is not None:
        print(f"{name} removido da lista de suspeitos, está limpo")
    else:
        print(SUSPECT_NOT_FOUND)


def handle_judge_suspect():
    name = input()
    is_fake_natty = suspects["judge"](name)
    if is_fake_natty is None:
        print(SUSPECT_NOT_FOUND)
    else:
        print(f"Eu já tenho o meu veredito, e o meu veredito, {name}:")
        print(FAKE_NATTY if is_fake_natty else NATURAL)


def handle_result():
    print(NATTYMETER_STARTED)
    result = suspects["result"]()

    if result == 0:
        print("Oh yeah, vivemos em uma sociedade sem suco, um great day")
    else:
        print(f"NOOO! {int(result * 100)}% USARAM O SUCO")


command = input()
while command != END:
    if command == ADD_SUSPECT:
        handle_add_suspect()
    elif command == UPDATE_SUSPECT:
        handle_update_suspect()
    elif command == REMOVE_SUSPECT:
        handle_remove_suspect()
    elif command == JUDGE_SUSPECT:
        handle_judge_suspect()
    elif command == RESULT:
        handle_result()

    command = input()

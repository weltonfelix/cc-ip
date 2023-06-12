hiding_place = input()

place = input()

if place.lower() == hiding_place.lower():
    print("Ahá, te encontrei e é o fim das suas férias!")
else:
    print("Carambolas, ele não está aqui. Ele continua se divertindo!")

    place = input()

    if place.lower() == hiding_place.lower():
        print("Ahá, te encontrei e é o fim das suas férias!")
    else:
        print("Carambolas, ele não está aqui. Ele continua se divertindo!")

        place = input()

        if place.lower() == hiding_place.lower():
            print("Ahá, te encontrei e é o fim das suas férias!")
        else:
            print("Carambolas, ele não está aqui. Ele continua se divertindo!")
            print("AAAAAAAH, ele escapou de vez!")

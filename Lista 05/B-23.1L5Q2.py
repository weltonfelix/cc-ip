life, houses = input().split()
life = int(life)
houses = int(houses)

fibonacci_list = []


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def check_in_fibonnaci(number):
    if number in fibonacci_list:
        return True
    else:
        n = 0
        fib = 0
        while fib <= number:
            fib = fibonacci(n)
            if len(fibonacci_list) > n:
                fibonacci_list[n] = fib
            else:
                fibonacci_list.append(fib)

            if fib == number:
                return True
            elif fib > number:
                return False

            n += 1

        return False


initial_houses = houses

while houses > 0 and life > 0:
    house_number = int(input())

    if check_in_fibonnaci(house_number):
        houses -= 1
    else:
        life -= 1
        houses = initial_houses

        print(
            "Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!"
        )

if life == 0:
    print(
        "A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf"
    )
else:
    print("Voce Adicionou A Master Sword ao seu inventario")
    print("Link Salve Hyrule!!!")

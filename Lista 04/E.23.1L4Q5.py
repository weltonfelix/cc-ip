VOWELS = ["a", "e", "i", "o", "u"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def count_letters(text):
    vowels = 0
    consonants = 0

    for i in range(len(text)):
        if text[i] not in NUMBERS:
            if text[i] in VOWELS:
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


def detect_numbers(text):
    numbers = []
    last_number = ""
    for i in range(len(text)):
        if text[i] in NUMBERS:
            last_number += text[i]
        else:
            if last_number != "":
                numbers.append(int(last_number))
                last_number = ""

    if last_number != "":
        numbers.append(int(last_number))
        last_number = ""

    return numbers


def floor(number):
    return int(number - (number % 1))


def build_matrix(x, y):
    matrix = []
    for row in range(7):
        row_content = []
        for column in range(7):
            if [column, row] == [y, x]:
                row_content.append("☆")
            else:
                row_content.append(".")

        matrix.append(row_content)

    return matrix


def detect_multiples(numbers):
    if len(numbers) > 1:
        is_multiple = True
        for number in numbers:
            if number % numbers[0] != 0:
                is_multiple = False

        return is_multiple
    else:
        return False


x_axis_code = input().lower()
y_axis_code = input().lower()

x_vowels, x_consonants = count_letters(x_axis_code)
x_position = floor(x_vowels / x_consonants) % 7 if x_consonants != 0 else 0

if detect_multiples(detect_numbers(x_axis_code)):
    x_position = 3

y_vowels, y_consonants = count_letters(y_axis_code)
y_position = floor(y_vowels / y_consonants) % 7 if y_consonants != 0 else 0

if detect_multiples(detect_numbers(y_axis_code)):
    y_position = 3

for row in build_matrix(x_position, y_position):
    print(" ".join(row))

if [x_position, y_position] == [3, 3]:
    print(
        "Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!"
    )
elif x_position in [0, 6] or y_position in [0, 6]:
    print(
        "Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código..."
    )
else:
    print("Ok, agora é só enviar a matriz!")

if x_position in [0, 6] or y_position in [0, 6]:
    print(
        "Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo."
    )
else:
    print("Obrigado pela ajuda! A foto ficou ótima!")

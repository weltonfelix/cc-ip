NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def check_is_palindrome(text):
    is_palindrome = True
    i = 0
    while is_palindrome and i < (len(text) / 2) + 1:
        if text[i] != text[-i - 1]:
            is_palindrome = False

        i += 1

    return is_palindrome


def count_distinct_characters(text):
    distinct_characters = []
    for i in range(len(text)):
        if text[i] not in distinct_characters:
            distinct_characters.append(text[i])

    return len(distinct_characters)


phrases = int(input())

for i in range(phrases):
    text = input()
    normalized_text = text.replace(" ", "").upper()

    is_palindrome = check_is_palindrome(normalized_text)
    distinct_characters = count_distinct_characters(normalized_text)

    is_number = True
    j = 0
    while is_number and j < len(normalized_text):
        if text[j] not in NUMBERS:
            is_number = False

        j += 1

    if is_palindrome:
        if is_number:
            print(f'O número "{text}" é um palíndromo!')
            print(
                f"Há {distinct_characters} número(s) distinto(s) na sequência de números."
            )
        else:
            print(f'A frase "{text}" é um palíndromo!')
            print(f"Há {distinct_characters} letra(s) distinta(s) na frase.")
    else:
        print("A frase ou o número não é um palíndromo.")

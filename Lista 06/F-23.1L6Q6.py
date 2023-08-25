EOF = "END_OF_FILE"

file = []

row = input()
while row != EOF:
    file.append(row.lower())
    row = input()


def generate_trigrams(file):
    trigrams = {}

    for row_number in range(len(file)):
        row = file[row_number]

        row_trigrams = []
        row_trigrams += [
            row[initial_char : initial_char + 3]
            for initial_char in range(0, len(row), 3)
        ]  # generate trigrams, starting from the first character
        row_trigrams += [
            row[initial_char : initial_char + 3]
            for initial_char in range(1, len(row), 3)
        ]  # generate trigrams, starting from the second character
        row_trigrams += [
            row[initial_char : initial_char + 3]
            for initial_char in range(2, len(row), 3)
        ]  # generate trigrams, starting from the third character
        # E.g.: "abcde" -> ["abc", "bcd", "cde"]

        for trigram in row_trigrams:
            if trigrams.get(trigram):
                trigrams[trigram].append(row_number)
            else:
                trigrams[trigram] = [row_number]

    return trigrams


file_trigrams = generate_trigrams(file)
search_substrings = []

for _ in range(int(input())):
    search_substrings.append(input().lower())


for search in search_substrings:
    matched_row = -1
    search_first_trigram = search[0:3]
    rows_search_first_trigram = file_trigrams.get(search_first_trigram)

    if rows_search_first_trigram is not None:
        current_row_index = 0
        while matched_row == -1 and current_row_index < len(rows_search_first_trigram):
            current_row = rows_search_first_trigram[current_row_index]
            if search in file[current_row]:
                matched_row = current_row

            current_row_index += 1

    print(matched_row)

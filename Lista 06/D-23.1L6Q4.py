alphabet = list(chr(code) for code in range(97, 123))

rows = int(input())

words = {}

for _ in range(rows):
    word = input()
    for letter in alphabet:
        new_word = f"{word.replace('_', letter)}"
        words[new_word] = words[new_word] + 1 if words.get(new_word) else 1

_, most_repeated_ocurrences = max(words.items(), key=lambda word: word[1])

most_repeated_words = []

for word in words.items():
    if word[1] == most_repeated_ocurrences:
        most_repeated_words.append(word)

word, ocurrences = min(most_repeated_words, key=lambda item: item[0])

print(word, ocurrences)

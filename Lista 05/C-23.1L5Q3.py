suspect_name = input()
names = input()


def find_substring(substring, original_substring, string):
    if len(substring) == 1:
        if string[0] == substring[0]:
            return True
        else:
            return False
    elif len(string) == 1:
        return False
    if string[0] == substring[0]:
        return find_substring(substring[1:], original_substring, string[1:])
    else:
        return find_substring(original_substring, original_substring, string[1:])


if find_substring(suspect_name.lower(), suspect_name.lower(), names.lower()):
    print(f"Encontrei, o culpado é o {suspect_name}!")
else:
    print(f"Não era o {suspect_name}, tenho que continuar procurando.")

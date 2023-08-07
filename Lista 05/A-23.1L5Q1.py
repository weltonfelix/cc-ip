def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def check_string_casing(string: str):
    upper_string = string.upper()

    uppercase = 0
    lowercase = 0

    for char_index in range(len(string)):
        if string[char_index] == upper_string[char_index]:
            uppercase += 1
        else:
            lowercase += 1

    return [uppercase, lowercase]


grunt = input()
[uppercase, lowercase] = check_string_casing(grunt)

price = 0
if uppercase == lowercase:
    price = len(grunt) ** 2
else:
    price = factorial(max(lowercase, uppercase)) * len(grunt)

if price >= 100:
    print(f"Hum... {price}? Acho que na volta eu compro")
else:
    print(f"{price}! Vou comprar todos!")

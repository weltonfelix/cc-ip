ADDITION_INPUT = "Quero somar esses dois números:"
SUBTRACTION_INPUT = "Preciso subtrair um pelo outro"
MULTIPLICATION_INPUT = "Quanto dá o produto disso?"
DIVISION_INPUT = "Vou dividir aqui rapidinho"
EXPONENTIATION_INPUT = "E se eu elevar um pelo outro?"


def addition(term1, term2):
    return term1 + term2


def subtraction(minuend, subtrahend):
    return minuend - subtrahend


def multiplication(factor1, factor2):
    return factor1 * factor2


def division(dividend, divisor):
    return dividend / divisor


def exponentiation(base, power):
    return base**power


def calculate():
    operation = input()
    number1 = float(input())
    number2 = float(input())

    if operation == ADDITION_INPUT:
        return addition(number1, number2)
    elif operation == SUBTRACTION_INPUT:
        return subtraction(number1, number2)
    elif operation == MULTIPLICATION_INPUT:
        return multiplication(number1, number2)
    elif operation == DIVISION_INPUT:
        return division(number1, number2)
    elif operation == EXPONENTIATION_INPUT:
        return exponentiation(number1, number2)


operations = int(input())
if operations == 0:
    print("Vou relaxar aqui na minha nave")
else:
    for i in range(1, operations + 1):
        print(f"O resultado da {i}ª operação foi {calculate():.1f}")

    print("Ufa, já deu de cálculos por hoje!")

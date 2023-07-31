END = "Todas as expressoes foram enviadas!"
OPERANDS = ["+", "-", "*", "/"]


def handle_operation(term1, term2, operand):
    if operand == "+":
        return term1 + term2
    elif operand == "-":
        return term1 - term2
    elif operand == "*":
        return term1 * term2
    elif operand == "/":
        return term1 / term2


def solve_expression(expression):
    stack = []
    terms = expression.split()
    for term in terms:
        if term not in OPERANDS:
            stack.append(int(term))
        else:
            term1 = stack[-2]
            term2 = stack[-1]
            stack = stack[: len(stack) - 2]
            stack.append(handle_operation(term1, term2, term))

    return stack[0]


def check_perfect_number(value):
    if value == 0:
        return 0

    divisors = []
    for number in range(1, value):
        if value % number == 0:
            divisors.append(number)

    return 1 if sum(divisors) == value else 0


def binary_to_ascii(number):
    return chr(int(number, base=2))


def main():
    message = ""
    expression = input()
    expressions_counter = 0

    while expression != END:
        expressions_counter += 1
        binary = ""

        while expression != "":
            result = int(solve_expression(expression))
            binary += str(check_perfect_number(result))

            expression = input()

        if len(binary) > 0:
            character = binary_to_ascii(binary)
            message += character

            print(
                f"O {expressions_counter}º conjunto de expressoes resultou no binario {binary} que em ASCII eh: {character}\n"
            )

        expression = input()

    print(f"A decodificacao final resultou em:\n{message}")


main()

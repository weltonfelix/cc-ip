polynomial_degree = int(input())
derivative_order = int(input())
not_null_coeficients = int(input())

coeficients = [0] * (polynomial_degree + 1)
for c in range(not_null_coeficients):
    # Coeficiente do 0 : 10
    coeficient_input = input()
    index = coeficient_input[15:]
    values = index.replace(":", "").split(" ")

    coeficients[int(values[0])] = int(values[2])


def differentiate(polynomial_coeficients, derivative_order):
    if derivative_order == 0:
        return polynomial_coeficients

    result = [0] * len(polynomial_coeficients)

    for term_index in range(len(polynomial_coeficients)):
        result[term_index] = polynomial_coeficients[term_index] * term_index

    if all(c == 0 for c in result):
        return [0]
    else:
        return differentiate(result[1:], derivative_order - 1)


def print_polinomyal(coeficients):
    polinomyal = ""
    if all(c == 0 for c in coeficients):
        return "0"

    for term in range(len(coeficients)):
        if coeficients[term] != 0:
            if coeficients[term] == -1:
                if term == 0:
                    polinomyal += str(coeficients[term])
                elif term == 1:
                    polinomyal += "-x"
                else:
                    polinomyal += f"-x^{term}"
            elif coeficients[term] == 1:
                if term == 0:
                    polinomyal += str(coeficients[term])
                elif term == 1:
                    if len(polinomyal) == 0:
                        polinomyal += f"x"
                    else:
                        polinomyal += f"+x"
                else:
                    if len(polinomyal) == 0:
                        polinomyal += f"x^{term}"
                    else:
                        polinomyal += f"+x^{term}"
            else:
                if term == 0:
                    polinomyal += f"{coeficients[term]}"
                elif term == 1:
                    if coeficients[term] < 0 or len(polinomyal) == 0:
                        polinomyal += f"{coeficients[term]}x"
                    else:
                        polinomyal += f"+{coeficients[term]}x"
                else:
                    if coeficients[term] < 0 or len(polinomyal) == 0:
                        polinomyal += f"{coeficients[term]}x^{term}"
                    else:
                        polinomyal += f"+{coeficients[term]}x^{term}"

    return polinomyal


derivative = differentiate(coeficients, derivative_order)

print(f"A derivada {derivative_order} do polinômio {print_polinomyal(coeficients)} é")
print(print_polinomyal(derivative))

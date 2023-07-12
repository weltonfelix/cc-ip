undesired_items = ["colete preto", "coturno", "vestido com babados", "blusa bufante"]

n = int(input())

for _ in range(n):
    collection = input().split(", ")
    raw_grades = input().split(", ")
    grades = []
    for raw_grade in raw_grades:
        grades.append(int(raw_grade))

    i = 0
    eliminated = False
    total_collection_grade = 0
    while (i < len(collection)) and not eliminated:
        if collection[i] in undesired_items:
            eliminated = True
        else:
            total_collection_grade += grades[i]
            i += 1

    collection_mean = total_collection_grade / len(collection)

    if eliminated:
        if collection[i] in ["colete preto", "coturno"]:
            print(
                f"{collection[i]} é uma peça muito gótica, não faz o estilo da Glimmer."
            )
        elif collection[i] in ["vestido com babados", "blusa bufante"]:
            print(
                f"{collection[i]} é uma peça muito antiquada, infelizmente essa coleção não vai servir..."
            )

    elif collection_mean < 6:
        print(
            "Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir."
        )
    else:
        print("Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.")

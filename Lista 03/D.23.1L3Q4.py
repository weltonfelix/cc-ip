EXPLORE_RACK = "Explorar arara"
FINISH = "Meninas, acho que já falei demais. Vamos para o shopping?"

current_option = ""
rack_number = -1
while current_option != FINISH:
    current_option = input()
    if current_option != FINISH:
        rack_number += 1
        professions_in_rack = input().split(", ")
        professions_to_present = input().split(", ")

        print(f"Arara {rack_number}:")

        missing_professions = []
        for profession in professions_in_rack:
            if profession not in professions_to_present:
                missing_professions.append(profession)

        if len(professions_in_rack) != len(professions_to_present):
            print(
                "Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!"
            )
        elif len(missing_professions) > 0:
            print(
                f"Poxa, Barbie! Você acabou desorganizando essa arara, e {len(missing_professions)} profissões vão ficar de fora da conversa. São elas: {', '.join(missing_professions)}."
            )
        elif len(missing_professions) == 0:
            print(
                "Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!"
            )

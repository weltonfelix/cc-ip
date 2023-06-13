venom_max_hp = int(input())
venom_attack = int(input())
venom_potion_hp = int(input())

creeper_hp = int(input())
creeper_attack = venom_attack

druid_hp = int(input())
druid_attack = int(input())

venom_life = venom_max_hp
creeper_life = creeper_hp

# Round 1
print(f"SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O CREEPER!")

venom_life -= creeper_attack
creeper_life -= venom_attack

did_venom_lose = False

if venom_life <= 0:
    did_venom_lose = True
elif creeper_life <= 0:
    did_venom_lose = False
else:
    if venom_attack < creeper_attack:
        did_venom_lose = True
    elif venom_attack > creeper_attack:
        did_venom_lose = False
    else:
        if venom_life < creeper_life:
            did_venom_lose = True
        elif creeper_life < venom_life:
            did_venom_lose = False
        else:
            did_venom_lose = True

if venom_life <= 0:
    print("O venom não tankou e foi de base...")

if creeper_life <= 0:
    print("O creeper não tankou e foi de base...")

if venom_life > 0 and creeper_life > 0:
    print(f"Vida atual do Venom: {venom_life}")
    print(f"Dano sofrido pelo Venom: {creeper_attack}")
    print(f"Vida atual do creeper: {creeper_life}")
    print(f"Dano sofrido pelo creeper: {venom_attack}")

if not did_venom_lose:
    print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")

    if (venom_potion_hp + venom_life) <= venom_max_hp:
        venom_life += venom_potion_hp
        print("Ah! Essa poção é da boa!")

    # Round 2
    print(f"SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O DRUIDA!")

    poison = 0

    if (venom_potion_hp + venom_life) <= venom_max_hp:
        venom_life += venom_potion_hp
    else:
        poison = (venom_life + venom_potion_hp) - venom_max_hp
        venom_life = venom_max_hp

    druid_life = druid_hp

    venom_life -= druid_attack + poison
    druid_life -= venom_attack

    did_venom_lose = False

    if venom_life <= 0:
        did_venom_lose = True
    elif druid_life <= 0:
        did_venom_lose = False
    else:
        if venom_attack < (druid_attack + poison):
            did_venom_lose = True
        elif venom_attack > (druid_attack + poison):
            did_venom_lose = False
        else:
            if venom_life < druid_life:
                did_venom_lose = True
            elif druid_life < venom_life:
                did_venom_lose = False
            else:
                did_venom_lose = True

    if venom_life <= 0:
        print("O venom não tankou e foi de base...")

    if druid_life <= 0:
        print("O druida não tankou e foi de base...")

    if venom_life > 0 and druid_life > 0:
        print(f"Vida atual do Venom: {venom_life}")
        print(f"Dano sofrido pelo Venom: {druid_attack + poison}")
        print(f"Vida atual do druida: {druid_life}")
        print(f"Dano sofrido pelo druida: {venom_attack}")

    if not did_venom_lose:
        print("Quase me dei mal, nunca mais aceito nada de estranho...")
        print(
            "Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *"
        )
    else:
        print("Pelo visto a poção tava fora do prazo de validade :(")
        print("Pelo visto as aventuras do Miles terminaram por aqui...")
else:
    print("AH NÃO! O VENOM PEGOU EM BOMBA!")
    print("Pelo visto as aventuras do Miles terminaram por aqui...")

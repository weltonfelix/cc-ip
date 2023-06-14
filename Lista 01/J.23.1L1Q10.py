spider_name = input()
spider_attack = int(input())
spider_defense = int(input())

ally_name = input()
ally_attack = int(input())
ally_defense = int(input())

villan_name = input()
villan_attack = int(input())
villan_defense = int(input())

henchman_name = input()
henchman_attack = int(input())
henchman_defense = int(input())

luck_round_1 = int(input())
luck_round_2 = int(input())
luck_round_3 = int(input())

spider_wins = 0

# Round 1
# Spider attacks
current_round = 1
print(f"{current_round}° confronto:")

did_spider_won = False

spider_has_ally = False
villan_has_henchman = False

if luck_round_1 == 0:
    spider_has_ally = False
    villan_has_henchman = False
elif luck_round_1 == 1:
    spider_has_ally = True
    villan_has_henchman = False
elif luck_round_1 == 2:
    spider_has_ally = False
    villan_has_henchman = True
elif luck_round_1 == 3:
    spider_has_ally = True
    villan_has_henchman = True

spider_power = spider_attack
villan_power = villan_defense

if spider_has_ally:
    spider_power += ally_attack

if villan_has_henchman:
    villan_power += henchman_defense

if spider_power > villan_power:
    did_spider_won = True
elif spider_power < villan_power:
    did_spider_won = False
else:
    if spider_has_ally == villan_has_henchman:
        did_spider_won = True
    elif spider_has_ally:
        did_spider_won = True
    else:
        did_spider_won = False

if did_spider_won:
    spider_wins += 1
    print(f"O {spider_name} acertou vários golpes no {villan_name}")
else:
    print(f"O {villan_name} está dificultando a vida do {spider_name}")

# Round 2
# Spider defends
current_round = 2
print(f"{current_round}° confronto:")

did_spider_won = False

spider_has_ally = False
villan_has_henchman = False

if luck_round_2 == 0:
    spider_has_ally = False
    villan_has_henchman = False
elif luck_round_2 == 1:
    spider_has_ally = False
    villan_has_henchman = True
elif luck_round_2 == 2:
    spider_has_ally = True
    villan_has_henchman = False
elif luck_round_2 == 3:
    spider_has_ally = True
    villan_has_henchman = True

spider_power = spider_defense
villan_power = villan_attack

if spider_has_ally:
    spider_power += ally_defense

if villan_has_henchman:
    villan_power += henchman_attack

if spider_power > villan_power:
    did_spider_won = True
elif spider_power < villan_power:
    did_spider_won = False
else:
    if spider_has_ally == villan_has_henchman:
        did_spider_won = True
    elif spider_has_ally:
        did_spider_won = True
    else:
        did_spider_won = False

if did_spider_won:
    spider_wins += 1
    print(f"O {spider_name} contra-atacou o {villan_name}")
else:
    print(f"O {spider_name} não consegue se defender contra o {villan_name}")

# Round 3
# Spider attacks
current_round = 3
print(f"{current_round}° confronto:")

did_spider_won = False

spider_has_ally = False
villan_has_henchman = False

if luck_round_3 == 0:
    spider_has_ally = False
    villan_has_henchman = False
elif luck_round_3 == 1:
    spider_has_ally = True
    villan_has_henchman = False
elif luck_round_3 == 2:
    spider_has_ally = False
    villan_has_henchman = True
elif luck_round_3 == 3:
    spider_has_ally = True
    villan_has_henchman = True

spider_power = spider_attack
villan_power = villan_defense

if spider_has_ally:
    spider_power += ally_attack

if villan_has_henchman:
    villan_power += henchman_defense

if spider_power > villan_power:
    did_spider_won = True
elif spider_power < villan_power:
    did_spider_won = False
else:
    if spider_has_ally == villan_has_henchman:
        did_spider_won = True
    elif spider_has_ally:
        did_spider_won = True
    else:
        did_spider_won = False

if did_spider_won:
    spider_wins += 1
    print(f"O {spider_name} acertou vários golpes no {villan_name}")
else:
    print(f"O {villan_name} está dificultando a vida do {spider_name}")

if spider_wins >= 2:
    print(
        f"O {spider_name} e {ally_name} conseguiram derrotar o {villan_name} e recuperar o multiverso!"
    )
else:
    print(
        f"O {villan_name} e {henchman_name} invadiram Nova York, onde estão os outros aranhas??"
    )

import random

win1 = 0
for i in range(1,10001):
    car = random.randint(1,3)
    goat1 = random.randint(1,3)
    goat2 = random.randint(1,3)

    while goat1 == car:
        goat1 = random.randint(1,3)
    while goat2 == car or goat2 == goat1:
        goat2 = random.randint(1,3)

    choicep1 = random.randint(1,3)

    if choicep1 == car:
        win1 = win1 + 1

print("Out of 10,000 games, you win %d times if you dont swap doors" % win1)


win2 = 0
for i in range(1,10001):
    car = random.randint(1,3)
    goat1 = random.randint(1,3)
    goat2 = random.randint(1,3)

    while goat1 == car:
        goat1 = random.randint(1,3)
    while goat2 == car or goat2 == goat1:
        goat2 = random.randint(1,3)

    choicep2 = random.randint(1,3)

    optioning = random.randint(1,3)

    while optioning == car:
        optioning = random.randint(1,3)

    choicep2_1 = 0

    if choicep2 == goat1 or choicep2 == goat2:
        choicep2_1 = car + choicep2_1

    if choicep2 == car:
        choicep2_1 = optioning + choicep2_1

    if choicep2_1 == car:
        win2 += 1

print("Out of 10,000 games, you win %d times if you do swap" % win2)

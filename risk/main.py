import random as rd

defender_troops = int(input("defender Troups: "))
attacker_troops = int(input("attacker Troups: "))


def roll_dice():
    return rd.randrange(0, 6)


def roll_more_dice(defender_troups, attacker_troups):

    defender_dice_rolls = [roll_dice()]

    if defender_troups >= 2:
        defender_dice_rolls.append(roll_dice())

    defender_dice_rolls.sort(reverse=True)

    attacker_dice_rolls = [roll_dice()]

    if attacker_troups > 1:
        attacker_dice_rolls.append(roll_dice())

    if attacker_troups > 2:
        attacker_dice_rolls.append(roll_dice())

    attacker_dice_rolls.sort(reverse=True)
    #print(attacker_dice_rolls, defender_dice_rolls)
    return attacker_dice_rolls, defender_dice_rolls


def compare_dice_rolls(attacker_dice_rolls, defender_dice_rolls):
    attacker_troops_lost = 0
    defender_troops_lost = 0

    if attacker_dice_rolls[0] > defender_dice_rolls[0]:
        defender_troops_lost += 1
    else:
        attacker_troops_lost += 1

    if len(attacker_dice_rolls) and len(defender_dice_rolls) >= 2:
        if attacker_dice_rolls[1] > defender_dice_rolls[1]:
            defender_troops_lost += 1
        else:
            attacker_troops_lost += 1

    return attacker_troops_lost, defender_troops_lost


while (defender_troops > 0) and (attacker_troops > 0):
    adr, cdr = roll_more_dice(defender_troops, attacker_troops)
    atl, dtl = compare_dice_rolls(adr, cdr)

    attacker_troops -= atl
    defender_troops -= dtl

    #print(attacker_troops, defender_troops)

print(f"Result:\n Attacker troops: {attacker_troops}\n Defender troops: {defender_troops}")


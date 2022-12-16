import math
import random
import time

def RollFunction():
    Roll = random.randint(1,6)
    return Roll

StringNumberList = [str(x) for x in range(1000 + 1)]

def CheckAnswerInt(IntAnswer):
    while IntAnswer not in StringNumberList:
        IntAnswer = input("*!Error!* Please enter an integer: ")
    
    return int(IntAnswer)

def CheckYesNo(Answer):
    ExeceptedAnswer = ["YES", "yES", "yeS", "YEs", "YeS", "yes", "Y", "y", "Yes", "NO", "no", "N", "n", "No", "nO"]
    YesList = ["YES", "yES", "yeS", "YEs", "YeS", "yes", "Y", "y", "Yes",]
    NoList = ["NO", "no", "N", "n", "No", "nO"]
    YesAnswer = "YES"
    NoAnswer = "NO"

    while Answer not in ExeceptedAnswer:
        Answer = str(input("*!ERROR!* Answer must be either YES or NO: "))
        continue
    
    if Answer in YesList:
        return YesAnswer
    elif Answer in NoList:
        return NoAnswer


INTRODUCTION = '''
_____________________________________________
*********************************************
        Welcome to Digital Terracatta

        Made for Quick Games of Risk

    Here you are able to simulate battles
    so that you do not have to deal with
        time consuming dice rolling.

    Enter the number of units attacking
    Enter the number of units defending

    Then choose if you want to simulate
    Full Battle    or   Individual Rolls
_____________________________________________
*********************************************
'''
print(INTRODUCTION)

AttackUnits = CheckAnswerInt(str(input("Enter number of units attacking:  ")))
DefenseUnits = CheckAnswerInt(str(input("Enter number of units defending:  ")))

Choice = CheckYesNo(str(input("Would you like to see each individual roll? YES/NO: ")))

BeginingUnitsAttack = AttackUnits
BeginingUnitsDefense = DefenseUnits

while True:

    AttackRolls3 = (RollFunction(), RollFunction(), RollFunction())
    AttackRolls2 = (RollFunction(), RollFunction())
    AttackRolls1 = (RollFunction())

    DefenseRolls2 = (RollFunction(), RollFunction())
    DefenseRolls1 = (RollFunction())

    if AttackUnits > 2 and DefenseUnits > 1:
        Attack = sorted(AttackRolls3, reverse = True)
        print('\nAttack Roll: ' + str(Attack))

        Defense = sorted(DefenseRolls2, reverse = True)
        print('Defense Roll: ' + str(Defense))

        if Attack[0] > Defense[0]:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits))
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))
                
        if Attack[1] > Defense[1]:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits)) 
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))

    elif AttackUnits == 2 and DefenseUnits > 1:
        Attack = sorted(AttackRolls2, reverse = True)
        print('\nAttack Roll: ' + str(Attack))

        Defense = sorted(DefenseRolls2, reverse = True)
        print('Defense Roll: ' + str(Defense))

        if Attack[0] > Defense[0]:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits)) 
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))
            
        if Attack[1] > Defense[1]:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits))
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))

    elif AttackUnits == 1 and DefenseUnits > 1:
        Attack = AttackRolls1
        print('\nAttack Roll: ' + str(Attack))

        Defense = sorted(DefenseRolls2, reverse = True)
        print('Defense Roll: ' + str(Defense))

        if Attack > Defense[0]:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits))
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))

    elif AttackUnits > 2 and DefenseUnits == 1:
        Attack = sorted(AttackRolls3, reverse = True)
        print('\nAttack Roll: ' + str(Attack))

        Defense = DefenseRolls1
        print('Defense Roll: ' + str(Defense))

        if Attack[0] > Defense:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits))
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))

    elif AttackUnits == 2 and DefenseUnits == 1:
        Attack = sorted(AttackRolls2, reverse = True)
        print('\nAttack Roll: ' + str(Attack))

        Defense = DefenseRolls1
        print('Defense Roll: ' + str(Defense))

        if Attack[0] > Defense:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits))
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))

    elif AttackUnits == 1 and DefenseUnits == 1:
        Attack = AttackRolls1
        print('\nAttack Roll: ' + str(Attack))

        Defense = DefenseRolls1
        print('Defense Roll: ' + str(Defense))

        if Attack > Defense:
            DefenseUnits = DefenseUnits - 1
            print("\nThe Defense lost one unit.\nDefense Units Remaining: " + str(DefenseUnits)) 
        else:
            AttackUnits = AttackUnits - 1
            print("\nThe Attack lost one unit.\nAttack Units Remaining: " + str(AttackUnits))
    
    if AttackUnits > 0 and DefenseUnits > 0 and Choice == "YES":
        EveryRoll = CheckYesNo(str(input("\nWould you like to roll again? YES/NO: ")))
        if EveryRoll == "YES":
            continue
        elif EveryRoll == "NO":
            print("\n\nEnding Battle...")
            time.sleep(1)
            print("\n\n***!Battle Ended!***")
            print("\nThe Attack lost a total of " + str(BeginingUnitsAttack - AttackUnits) + " units.")
            print("The Defense lost a total of " + str(BeginingUnitsDefense - DefenseUnits) + " units.")
            print("\nAttack Units Remaining: " + str(AttackUnits))
            print("Defense Units Remaining: " + str(DefenseUnits))
            print("")
            break

    if AttackUnits == 0:
        print("\n\n\nThe Attack Has Lost All Units.")
        time.sleep(1)
        print("\n\nBattle Over...\nCalculating Results...")
        time.sleep(2)
        print("\n\n*The Defense has won!")
        print("\n*The Defense lost a total of " + str(BeginingUnitsDefense - DefenseUnits) + " units.")
        print("*Defense Units Remaining: " + str(DefenseUnits))
        print("")
        break

    elif DefenseUnits == 0:
        print("\n\n\nThe Defense Has Lost All Units.")
        time.sleep(1)
        print("\n\nBattle Over...\nCalculating Results...")
        time.sleep(2)
        print("\n\n*The Attack has won!\n")
        print("\n*The Attack lost a total of " + str(BeginingUnitsAttack - AttackUnits) + " units.")
        print("*Attack Units Remaining: " + str(AttackUnits))
        print("")
        break
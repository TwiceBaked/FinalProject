import math
import random

def RollFunction():
    Roll = random.randint(1,6)
    return Roll

#def AttackUnitsLoss():
    #AttackUnitsLost = AttackUnits - 1
    #print("Attack Units: ")
    #print(AttackUnitsLost)
    #return AttackUnitsLost

#def DefenseUnitsLoss():
    #DefenseUnitsLost = DefenseUnits - 1
    #print("Defense Units: ") 
    #print(DefenseUnitsLost)
    #return DefenseUnitsLost

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


while AttackUnits > 0 and DefenseUnits > 0:

    AttackRolls3 = (RollFunction(), RollFunction(), RollFunction())
    AttackRolls2 = (RollFunction(), RollFunction())
    AttackRolls1 = (RollFunction())

    DefenseRolls2 = (RollFunction(), RollFunction())
    DefenseRolls1 = (RollFunction())

    if AttackUnits > 2 and DefenseUnits > 1:
        Attack = sorted(AttackRolls3, reverse = True)
        print('\nAttack Roll')
        print(Attack)

        Defense = sorted(DefenseRolls2, reverse = True)
        print('\nDefense Roll')
        print(Defense)

        if Attack[0] > Defense[0]:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)
            
        if Attack[1] > Defense[1]:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)        
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)

    elif AttackUnits == 2 and DefenseUnits > 1:
        Attack = sorted(AttackRolls2, reverse = True)
        print('\nAttack Roll')
        print(Attack)

        Defense = sorted(DefenseRolls2, reverse = True)
        print('\nDefense Roll')
        print(Defense)

        if Attack[0] > Defense[0]:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)
            
        if Attack[1] > Defense[1]:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)        
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)

    elif AttackUnits == 1 and DefenseUnits > 1:
        Attack = AttackRolls1
        print('\nAttack Roll')
        print(AttackRolls1)

        Defense = sorted(DefenseRolls2, reverse = True)
        print('\nDefense Roll')
        print(Defense)

        if Attack > Defense[0]:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)
            

    elif AttackUnits > 2 and DefenseUnits == 1:
        Attack = sorted(AttackRolls3, reverse = True)
        print('\nAttack Roll')
        print(Attack)

        Defense = DefenseRolls1
        print('\nDefense Roll')
        print(DefenseRolls1)

        if Attack[0] > Defense:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)

    elif AttackUnits == 2 and DefenseUnits == 1:
        Attack = sorted(AttackRolls2, reverse = True)
        print('\nAttack Roll')
        print(Attack)

        Defense = DefenseRolls1
        print('\nDefense Roll')
        print(DefenseRolls1)

        if Attack[0] > Defense:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)

    elif AttackUnits == 1 and DefenseUnits == 1:
        Attack = AttackRolls1
        print('\nAttack Roll')
        print(AttackRolls1)

        Defense = DefenseRolls1
        print('\nDefense Roll')
        print(DefenseRolls1)

        if Attack > Defense:
            #DefenseUnitsLoss()
            DefenseUnits = DefenseUnits - 1
            print("\nDefense Units: ") 
            print(DefenseUnits)
        else:
            #AttackUnitsLoss()
            AttackUnits = AttackUnits - 1
            print("\nAttack Units: ")
            print(AttackUnits)

    if Choice == "Yes":
        EveryRoll = CheckYesNo(str(input("Would you like to roll again? YES/NO: ")))
        if EveryRoll == "Yes":
            continue
        elif EveryRoll == "No":
            break
    elif Choice == "No":
            break

if AttackUnits == 0:
    print("\nThe Defense has won!\n")
elif DefenseUnits == 0:
    print("\nThe Attack has won!\n")

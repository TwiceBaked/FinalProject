import math
import random

def RollFunction():
    Roll = random.randint(1,6)
    return Roll

AttackRolls3 = (RollFunction(), RollFunction(), RollFunction())
AttackRolls2 = (RollFunction(), RollFunction())
AttackRolls1 = (RollFunction())

DefenseRolls2 = (RollFunction(), RollFunction())
DefenseRolls1 = (RollFunction())

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

AttackUnits = int(input("Enter number of units attacking:  "))
DefenseUnits = int(input("Enter number of units defending:  "))

#while (AttackUnits - 1) > 0 or DefenseUnits > 0:


if AttackUnits > 2 and DefenseUnits > 1:
    Attack = sorted(AttackRolls3, reverse = True)
    print('\nAttack Roll')
    print(Attack)

    Defense = sorted(DefenseRolls2, reverse = True)
    print('\nDefense Roll')
    print(Defense)

    if Attack[0] > Defense[0]:
        print('True')
    else:
        print('False')
    
    if Attack[1] > Defense[1]:
        print('True')
    else:
        print('False')

    #Paired = zip(Attack, Defense)
    #print(tuple(Paired))
    #if Paired[0] > Paired[1]:
    
elif AttackUnits == 2 and DefenseUnits > 1:
    Attack = sorted(AttackRolls2, reverse = True)
    print('\nAttack Roll')
    print(Attack)

    Defense = sorted(DefenseRolls2, reverse = True)
    print('\nDefense Roll')
    print(Defense)

elif AttackUnits == 1 and DefenseUnits > 1:
    print('\nAttack Roll')
    print(AttackRolls1)

    Defense = sorted(DefenseRolls2, reverse = True)
    print('\nDefense Roll')
    print(Defense)

elif AttackUnits > 2 and DefenseUnits == 1:
    Attack = sorted(AttackRolls3, reverse = True)
    print('\nAttack Roll')
    print(Attack)

    print('\nDefense Roll')
    print(DefenseRolls1)

elif AttackUnits == 2 and DefenseUnits == 1:
    Attack = sorted(AttackRolls2, reverse = True)
    print('\nAttack Roll')
    print(Attack)

    print('\nDefense Roll')
    print(DefenseRolls1)

elif AttackUnits == 1 and DefenseUnits == 1:
    print('\nAttack Roll')
    print(AttackRolls1)

    print('\nDefense Roll')
    print(DefenseRolls1)
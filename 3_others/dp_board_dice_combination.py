#!/usr/bin/python3


dice = [1,2,3,4,5,6]
DICE_SIDE = len(dice)

def dice_combination(n):
    combination = [ [0]*(DICE_SIDE+1) for _ in range(n+1) ]

    for i in range(DICE_SIDE+1):
        combination[0][i] = 1

    for step in range(1, n+1):
        for dice in range(1, DICE_SIDE+1):
            inself = 0
            if step - dice >= 0:
                inself = combination[step-dice][dice]

            outself = combination[step][dice-1]
            combination[step][dice] = inself + outself

    return combination[step][dice]


if __name__ == '__main__':
    print('input n: ', end='', flush=True)
    n = int(input())
    print('output: {0}'.format(dice_combination(n)))
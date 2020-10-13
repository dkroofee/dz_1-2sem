def tic_tac_toe(field):
    for i in range(len(field)):
        if field[i][0] == field[i][1] == field[i][2]:
            print(field[i][0], 'win')
            break
        elif field[0][i] == field[1][i] == field[2][i]:
            print(field[0][i], 'win')
            break
        elif field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
            print(field[1][1], 'win')
            break
    else:
        print('draw')

data = """0 - x
          - x -
          0 - 0"""

field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)
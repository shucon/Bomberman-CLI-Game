import sys


def controls(move, hero, board, bomb):

    if(move == 'w' and (board._board[hero._position_x][hero._position_y - 2] == board._freesymbol)):
        hero.clr(board)
        hero._position_y -= 2

    if(move == 's' and (board._board[hero._position_x][hero._position_y + 2] == board._freesymbol)):
        hero.clr(board)
        hero._position_y += 2

    if(move == 'a' and (board._board[hero._position_x - 4][hero._position_y] == board._freesymbol)):
        hero.clr(board)
        hero._position_x -= 4

    if(move == 'd' and (board._board[hero._position_x + 4][hero._position_y] == board._freesymbol)):
        hero.clr(board)
        hero._position_x += 4

    if(move == 'x'):
        bomb.plant(hero, board)

    if (move == 'q'):
        sys.exit(0)

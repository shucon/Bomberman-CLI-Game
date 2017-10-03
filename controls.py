import sys


def controls(move, hero, board, bomb):

    if(move == 'w' and (board.board[hero.position_x][hero.position_y - 2] == board.freesymbol)):
        hero.clr(board)
        hero.position_y -= 2

    if(move == 's' and (board.board[hero.position_x][hero.position_y + 2] == board.freesymbol)):
        hero.clr(board)
        hero.position_y += 2

    if(move == 'a' and (board.board[hero.position_x - 4][hero.position_y] == board.freesymbol)):
        hero.clr(board)
        hero.position_x -= 4

    if(move == 'd' and (board.board[hero.position_x + 4][hero.position_y] == board.freesymbol)):
        hero.clr(board)
        hero.position_x += 4

    if(move == 'x'):
        bomb.plant(hero, board)

    if (move == 'q'):
        sys.exit(0)

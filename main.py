def askgame():
    play = input('Do you want to play the game (yes/no) ?: ')
    startgame(play)


def startgame(bool):
    if bool.lower() == 'yes':

        print('\nSince you are playing in the console, you cannot click the board, a number is needed. ')
        print('As you can see in the board bellow, each cell has a number asign to it, you need to type the cell number your move takes')
        show_Board(example=wining_combinations[0:3])
        game()

    else:
        print('your loss, come another time, bye :) ')
        return

def show_Board(matrix=None, example=None):

    if example is not None:
        matrix = example

    split = '______________'
    print(split)
    print(' ')
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            print(f'| {matrix[a][b]} ', end='|')

        print(' ')
        print(split)
        print(' ')

def update_matrix(matrix1, matrix2, move, tag):
    
    matrix1[cells[move][0]][cells[move][1]] = tag
    matrix2[cells[move][0]][cells[move][1]] = move
    return matrix1, matrix2


def checkvictory(matrix2, moves):
    if moves < 3:
        return False
    else:
        current_matrix_combination = []
        for a in range(len(wining_combinations)):
            m = []
            for b in range(len(wining_combinations[0])):
                m.append(matrix2[cells[wining_combinations[a][b]]
                         [0]][cells[wining_combinations[a][b]][1]])
            current_matrix_combination.append(m)  
        for a in current_matrix_combination:
            if a in wining_combinations:
                return True      
    return False


def game():
    gameOn = True
    m_numbers_1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    m_numbers_2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    m_show = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    show_Board(matrix=m_show)
    moves1 = 0
    moves2 = 0
    while gameOn:

        ############### Player 1 ############################
        moveP1 = int(input("Player1. choose your next cell: "))
        if m_show[cells[moveP1][0]][cells[moveP1][1]] != ' ':
             moveP1 = int(input("Player1. cell taken, please choose another cell: "))
        m_show, m_numbers_1 = update_matrix(
            m_show, m_numbers_1, int(moveP1), 'X')
        moves1 += 1
        show_Board(matrix=m_show)
        if checkvictory(m_numbers_1, moves1):
            print("¡Player 1 won!")
            gameOn = False
            askgame()

        ################ Boards ############################
        if moves1 + moves2 == 9:
            print("Boards, you may begin another game")
            gameOn = False
            askgame()
        
        ############### Player 2 ############################
        moveP2 = int(input("Player2. choose your next cell: "))
        if m_show[cells[moveP2][0]][cells[moveP2][1]] != ' ':
             moveP2 = int(input("Player2. cell taken, please choose another cell: "))
        m_show, m_numbers_2 = update_matrix(
            m_show, m_numbers_2, int(moveP2), 'O')
        moves2 += 1
        show_Board(matrix=m_show)
        if checkvictory(m_numbers_2, moves2):
            print("¡Player 2 won!")
            gameOn = False
            askgame()


if __name__ == "__main__":
    cells = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    wining_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    print('\nWELCOME TO TICTACTOE GAME\n')
    askgame()

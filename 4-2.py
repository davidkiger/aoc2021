file = open("4-1.in", "r")
rows = list(file)

def check_board(board):
    if (sum(board[0]) == -5 or
       sum(board[1]) == -5 or
       sum(board[2]) == -5 or
       sum(board[3]) == -5 or
       sum(board[4]) == -5 or
       (board[0][0] + board[1][0] + board[2][0] + board[3][0] + board[4][0]) == -5 or
       (board[0][1] + board[1][1] + board[2][1] + board[3][1] + board[4][1]) == -5 or
       (board[0][2] + board[1][2] + board[2][2] + board[3][2] + board[4][2]) == -5 or
       (board[0][3] + board[1][3] + board[2][3] + board[3][3] + board[4][3]) == -5 or
       (board[0][4] + board[1][4] + board[2][4] + board[3][4] + board[4][4]) == -5):
       #(board[0][4] + board[1][4] + board[2][4] + board[3][4] + board[4][4]) == -5 or

       #(board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4]) == -5 or
       #(board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0]) == -5):
        return True
    else:
        return False

numbers = list(map(int, rows[0].strip().split(',')))
boards = []
this_board = []
for i in range(2, len(rows)):
    rows[i] = rows[i].replace('  ', ' ')
    if rows[i].strip() == '':
        boards.append(this_board)
        this_board = []
        continue

    this_board.append(list(map(int,rows[i].strip().split(' '))))

for n in numbers:
    for b in boards:
        for r in range(5):
            for y in range(5):
                if b[r][y] == n:
                    b[r][y] = -1
    
    for b in boards:
        if check_board(b):
            if len(boards) > 1:
                boards.remove(b)
            else:
                for r in range(5):
                    for y in range(5):
                        if b[r][y] == -1:
                            b[r][y] = 0
            
                unmarked_sum = sum(sum(b,[]))
                print(unmarked_sum * n)
                exit()

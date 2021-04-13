import random
import copy

class Teeko2Player:
    """ An object representation for an AI game player for the game Teeko2.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a Teeko2Player object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.

        Args:
            state (list of lists): should be the current state of the game as saved in
                this Teeko2Player object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.

                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).

        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """

        state_copy = copy.deepcopy(state)
        num_elements = 0

        # deep copy the state and count the number of mom-space elements
        for i in state:
            for j in i:
                if j == ' ':
                    continue
                num_elements += 1

        # drop phase = true for having less than 8 non-space elements
        if num_elements < 8:
            drop_phase = True   # TODO: detect drop phase
        else:
            drop_phase = False

        move = []

        if drop_phase == False:
            # TODO: choose a piece to move and remove it from the board
            # (You may move this condition anywhere, just be sure to handle it)
            #
            # Until this part is implemented and the move list is updated
            # accordingly, the AI will not follow the rules after the drop phase!
            piece_location = []
            for i in range(5):
                for j in range(5):
                    if state_copy[i][j] == self.my_piece:
                        list1 = [i, j]
                        piece_location.append(list1)

            a = random.randint(0, len(piece_location) - 1)
            point_move = piece_location[a]

            row = point_move[0]
            col = point_move[1]
            list2 = []

            if col < 4 and state[row][col + 1] == ' ':
                list2.append([row, col+1])
            elif row < 4 and state[row + 1][col] == ' ':
                list2.append([row+1, col])
            elif col < 4 and row < 4 and state[row + 1][col + 1] == ' ':
                list2.append(([row+1, col+1]))
            elif col > 0 and state[row][col - 1] == ' ':
                list2.append([row, col-1])
            elif row > 0 and state[row - 1][col] == ' ':
                list2.append([row-1, col])
            elif col > 0 and row > 0 and state[row - 1][col - 1] == ' ':
                list2.append([row-1, col-1])
            elif col < 4 and row > 0 and state[row - 1][col + 1] == ' ':
                list2.append([row-1, col+1])
            elif col > 0 and row < 4 and state[row + 1][col - 1] == ' ':
                list2.append([row+1, col-1])

            xe = random.randint(0, len(list2)-1)

            b = tuple(list2[xe])

            # print(b)

            move.insert(0, (row, col))
            move.insert(0, b)

            # state[row][col] = ' '
            # state[b[0]][b[1]] = self.my_piece
            # print(move)

        #print(self.my_piece)
        # print(num_elements)
        # print(drop_phase)
        # self.succ( state, drop_phase, self.my_piece)
        # self.heuristic_game_value(state)


        # print(a)

        # select an unoccupied space randomly
        # TODO: implement a minimax algorithm to play better
        if drop_phase:
            #move = []
            (row, col) = (random.randint(0,4), random.randint(0,4))
            while not state[row][col] == ' ':
                (row, col) = (random.randint(0,4), random.randint(0,4))

            # ensure the destination (row,col) tuple is at the beginning of the move list
            move.insert(0, (row, col))
            # print(move)

            # a, b= self.max_value(state_copy, 0, 1, -1)
            # print(b)
            # print(a)

        return move

    def whose_turn(self, state):
        b = 0
        r = 0
        for i in state:
            for j in i:
                if j == 'b':
                    b += 1
                if j == 'r':
                    r += 1
        if b > r:
            return 'r'
        else:
            return 'b'


    def succ(self, state, drop_phase, ai_color):

        if self.whose_turn(state) == ai_color:
            color = ai_color
        else:
            color = self.whose_turn(state)

        state_copy = copy.deepcopy(state)
        board_list = []
        return_list = []
        if drop_phase:
            for row in range(5):
                for col in range(5):
                    if state[row][col] == ' ':
                        list1 = [row, col]
                        return_list.append(list1)

                        # get the possible state after the move
                        state_copy[row][col] = color
                        board_list.append(state_copy)
                        state_copy = copy.deepcopy(state)
        else:
            # check all the possible moves that are adjacent
            for row in range(5):
                for col in range(5):
                    if state[row][col] == color:

                        # state_copy[row][col] = ' '

                        if col < 4 and state[row][col+1] == ' ':
                            list1 = [row, col+1]
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row][col+1] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)

                        if row < 4 and state[row+1][col] == ' ':
                            list1 = [row+1, col]
                            return_list.append(list1)
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row+1][col] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)


                        if row < 4 and col < 4 and state[row+1][col+1] == ' ':
                            list1 = [row+1, col+1]
                            return_list.append(list1)
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row+1][col + 1] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)

                        if col > 0 and state[row][col-1] == ' ':
                            list1 = [row, col-1]
                            return_list.append(list1)
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row ][col -1] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)

                        if row > 0 and state[row-1][col] == ' ':
                            list1 = [row-1, col]
                            return_list.append(list1)
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row - 1][col] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)
                        if row > 0 and col > 0 and state[row-1][col-1] == ' ':
                            list1 = [row-1, col-1]
                            return_list.append(list1)
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row - 1][col-1] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)
                        if  row < 4 and col > 0 and state[row+1][col-1] == ' ':
                            list1 = [row+1, col-1]
                            return_list.append(list1)
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row + 1][col - 1] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)
                        if row > 0 and col < 4 and state[row-1][col+1] == ' ':
                            list1 = [row-1, col+1]
                            return_list.append(list1)
                            if list1 not in return_list:
                                return_list.append(list1)

                            # the possible board after this move
                            state_copy[row - 1][col + 1] = color
                            state_copy[row][col] = ' '
                            board_list.append(state_copy)
                            state_copy = copy.deepcopy(state)
        #print(return_list)
        # print(board_list)
        return board_list




    def heuristic_game_value(self, state):



        if self.game_value(state) == 1:
            return 1
        elif self.game_value(state) == -1:
            return -1
        else:
            w4 = [2,2]
            w3 = [[1,1],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2],[3,3]]
            w2 = [[1,0],[0,1],[0,3],[1,4],[3,0],[4,1],[3,4],[4,3]]
            w1 = [[0,0],[0,2],[0,4],[3,0],[3,4],[4,0],[4,2],[4,4]]

            a4 = 0
            a3 = 0
            a2 = 0
            a1 = 0

            p1 = 0
            p2 = 0
            p3 = 0
            p4 = 0

            for row in range(5):
                for col in range(5):
                    if state[row][col] == self.my_piece:
                        coord = [row, col]
                        if coord == w4:
                            a4 +=1
                        elif coord in w3:
                            a3 +=1
                        elif coord in w2:
                            a2 += 1
                        elif coord in w1:
                            a1 += 1

                    if state[row][col] != ' ' and state[row][col] != self.my_piece:
                        coord = [row, col]
                        if coord == w4:
                            p4 += 1
                        elif coord in w3:
                            p3 += 1
                        elif coord in w2:
                            p2 += 1
                        elif coord in w1:
                            p1 += 1
            return_val = 0.4*(a4 - p4) + 0.3*(a3 - p3) + 0.2*(a2 - p2)
        #print(return_val)
        return return_val


    def minmax(self, state_copy, depth):
        state = copy.deepcopy(state_copy)
        # print(state)
        if self.game_value(state) == 1 or self.game_value(state) == -1:
            print('a')
            return self.game_value(state)
        if depth == 1:
            return self.heuristic_game_value(state)

        if self.whose_turn(state_copy) == self.my_piece:
            for element in self.succ(state_copy, self.is_drop(state),self.my_piece):
                return max(self.minmax(element, depth+1), -1)
        else:
            if self.my_piece == 'r':
                a = 'b'
            else:
                a = 'r'
            for element in self.succ(state_copy, self.is_drop(state),a):
                return min(self.minmax(element, depth+1), 1)



    def is_drop(self, state):
        a = 0
        for i in state:
            for j in i:
                if j != ' ':
                    a += 1
        if a >= 8:
            return False
        else:
            return True

    def max_value(self, state_copy, depth, alpha, beta):
        state = copy.deepcopy(state_copy)

        if self.game_value(state) == 1 or self.game_value(state) == -1:
            return self.game_value(state), state

        if depth == 1:
            return self.heuristic_game_value(state), state

        for element in self.succ(state_copy, self.is_drop(state), self.my_piece):

            alpha = max(alpha, self.min_value(element, depth + 1, alpha, beta)[0])
            b = self.min_value(element, depth + 1, alpha, beta)[1]
            if (alpha >= beta):
                return beta, element

        return alpha, b

    def min_value(self, state_copy, depth, alpha, beta):
        state = copy.deepcopy(state_copy)
        # print(state)
        # print(1)

        if self.game_value(state) == 1 or self.game_value(state) == -1:
            print('b')
            # print(self.game_value(state))
            return self.game_value(state), state
        if depth == 5:
            return self.heuristic_game_value(state), state
        if self.my_piece == 'r':
            player_color = 'b'
        else:
            player_color = 'r'

        for element in self.succ(state_copy, self.is_drop(state), player_color):
            beta = min(beta, self.max_value(element, depth + 1, alpha, beta)[0])
            a = self.max_value(element, depth + 1, alpha, beta)[1]
            # print(beta)
            if (alpha >= beta):
                return alpha, element
        return beta, a


    """
        def max_value(self, state, depth, alpha, beta):
        value = self.game_value(state)
        
        if value != 0:
            return value
        
        if depth == 4:
            return self.heuristic_game_value(state)
        
        for s in self.succ(state, self.is_drop(), self.my_piece)
    
        

    
        def max_value(self, state, depth, alpha, beta):
        value = self.game_value(state)

        if value != 0:
            return value

        if depth == 4:
            return self.heuristic_game_value(state)

        for s in self.succ(state, self.is_drop(state), self.my_piece):
            next_state = get_next_state(state, self.my_piece, s[0], s[1])
            alpha = max(alpha, self.min_value(next_state, depth+1, alpha, beta))
            if alpha >= beta:
                return beta
        return alpha

    def min_value(self, state, depth, alpha, beta):
        value = self.game_value(state)

        if value != 0:
            return value

        if depth == 4:
            return self.heuristic_game_value(state)

        if self.my_piece == 'r':
            player_color = 'b'
        else:
            player_color = 'r'

        for s in self.succ(state, self.is_drop(state), player_color):
            next_state = get_next_state(state, player_color, s[0], s[1])
            beta = min(beta, self.max_value(s, depth +1, alpha, beta))
            if alpha >= beta:
                return alpha
        return beta
    
        
        

    
    
    """




    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this Teeko2Player object, or a generated successor state.

        Returns:
            int: 1 if this Teeko2Player wins, -1 if the opponent wins, 0 if no winner

        TODO: complete checks for diagonal and 3x3 square corners wins
        """
        #print(state)
        # check horizontal wins
        #print(state)
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    #print(state)
                    #print("989")
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    print("x")
                    return 1 if state[i][col]==self.my_piece else -1

        # TODO: check \ diagonal wins
        for row in range(2):
            for col in range(2):
                if state[row][col] != ' ' and state[row][col] == state[row+1][col+1] == state[row+2][col+2]== state[row+3][col+3]:

                    return 1 if state[row][col] == self.my_piece else -1


        # TODO: check / diagonal wins
        for i in range(2):
            for col in range(2):
                row = 4 - i
                #print(row)
                #print(state[row][col])

                if state[row][col] != ' ' and state[row][col] == state[row-1][col+1] == state[row-2][col+2]== state[row-3][col+3]:

                    return 1 if state[row][col] == self.my_piece else -1

        # TODO: check 3x3 square corners wins
        for row in range(3):
            for col in range(3):
                if state[row][col] != ' ' and state[row][col] == state[row][col+2] == state[row+2][col] == state[row+2][col+2]:

                    return 1 if state[row][col] == self.my_piece else -1

        return 0 # no winner yet

def get_next_state(state_copy_from, color, row, col):
    state = state_copy_from
    state[row][col] = color
    if col < 4 and state[row][col+1] == color:
        state[row][col + 1] = ' '
    elif row < 4 and state[row+1][col] == color:
        state[row+1][col] = ' '
    elif col < 4 and row < 4 and state[row+1][col+1] == color:
        state[row+1][col + 1] = ' '
    elif col > 0 and state[row][col-1] == color:
        state[row][col-1] = ' '
    elif row >0 and state[row-1][col] == color:
        state[row-1][col] = ' '
    elif col > 0 and row > 0 and state[row-1][col-1] == color:
        state[row-1][col - 1] = ' '
    elif col < 4 and row > 0 and state[row - 1][col+1] == color:
        state[row - 1][col + 1] = ' '
    elif col > 0  and row < 4 and state[row + 1][col - 1] == color:
        state[row+1][col-1] = ' '
    print(state)
    return  state

############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################
def main():
    print('Hello, this is Samaritan')
    ai = Teeko2Player()
    piece_count = 0
    turn = 0

    # drop phase
    #print(ai.board)
    while piece_count < 8 and ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved at "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved from "+chr(move[1][1]+ord("A"))+str(move[1][0]))
            print("  to "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0])-ord("A")),
                                    (int(move_from[1]), ord(move_from[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        print("AI wins! Game over.")
    else:
        print("You win! Game over.")


if __name__ == "__main__":
    main()

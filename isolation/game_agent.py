import random

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # score function with heuristic1
    return heuristic1(game, player)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # score function with heuristic2
    return heuristic2(game, player)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # score function with heuristic3
    return heuristic3(game, player)


def heuristic1(game, player):
    """heuristic 1: evaluate the difference between player's total number of moves 
    left and opponent's total number of moves left. The move the player's moves left, 
    the better.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # return inf if player has won the game, otherwise return -inf 
    if game.is_winner(player):
        return float('inf')
    elif game.is_loser(player):
        return float('-inf')

    # calculate player's moves left and opponent's moves left, and return the difference
    my_moves_left = len(game.get_legal_moves(player))
    opponent_moves_left = len(game.get_legal_moves(game.get_opponent(player)))

    return float(my_moves_left - opponent_moves_left)


def heuristic2(game, player):
    """heuristic 2: evaluate the difference between player's total number of moves 
    left and opponent's total number of moves left as in heuristic 1. If both have 
    the same number of moves left, then evaluate whose current position is closer 
    to the center of the board (the closer the better).

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # return inf if player has won the game, otherwise return -inf
    if game.is_winner(player):
        return float('inf')
    elif game.is_loser(player):
        return float('-inf')

    # calculate number of moves left
    my_moves_left = len(game.get_legal_moves(player))
    opponent_moves_left = len(game.get_legal_moves(game.get_opponent(player)))

    
    if my_moves_left != opponent_moves_left:
        # return difference in number of moves left if it is not zero
        return float(my_moves_left - opponent_moves_left)
    else:
        # calculate distance from current position to the center position for both
        # return the difference of the two distances
        center_y_pos, center_x_pos = int(game.height/2), int(game.width/2)
        my_y_pos, my_x_pos = game.get_player_location(player)
        opponent_y_pos, opponent_x_pos = game.get_player_location(game.get_opponent(player))
        my_distance = abs(my_y_pos - center_y_pos) + abs(my_x_pos - center_x_pos)
        opponent_distance = abs(opponent_y_pos - center_y_pos) + \
                            abs(opponent_x_pos - center_x_pos)
        return float(opponent_distance - my_distance)/10.


def heuristic3(game, player):
    """heuristic 2: evaluate the difference between player's total number of moves 
    left and opponent's total number of moves left. If both have the same number of
    moves left, then evaluate whose current position is closer to the center of the 
    ard (more likely to win)

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # return inf if player has won the game, otherwise return -inf
    if game.is_winner(player):
        return float('inf')
    elif game.is_loser(player):
        return float('-inf')

    # calculate number of moves left
    my_moves_left = len(game.get_legal_moves(player))
    opponent_moves_left = len(game.get_legal_moves(game.get_opponent(player)))

    
    if my_moves_left != opponent_moves_left:
        # return difference in number of moves left if it is not zero
        return float(my_moves_left - opponent_moves_left)
    else:
        # calculate distance from current position to the center position for both
        # return the difference of the two distances
        center_y_pos, center_x_pos = int(game.height/2), int(game.width/2)
        my_y_pos, my_x_pos = game.get_player_location(player)
        opponent_y_pos, opponent_x_pos = game.get_player_location(game.get_opponent(player))
        my_distance = abs(my_y_pos - center_y_pos) + abs(my_x_pos - center_x_pos)
        opponent_distance = abs(opponent_y_pos - center_y_pos) + \
                            abs(opponent_x_pos - center_x_pos)
        return float(opponent_distance - my_distance)/10.

class IsolationPlayer:
    """Base class for minimax and alphabeta agents.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Depth-limited minimax search algorithm.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        """


        def min_play(self, game, depth):
            """function used by minimax to return best score for minimizing layer"""

            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            moves = game.get_legal_moves()
            
            # if no moves left
            if not moves:
                return game.utility(self)
            # if end of depth
            if depth == 0:
                return self.score(game, self)
            
            # initialize best score
            best_score = float('inf')
            # update best score by iterating over all legal moves
            for move in moves:
                best_score = min(best_score, max_play(self, game.forecast_move(move), depth-1))
            return best_score

        def max_play(self, game, depth):
            """function used by minimax to return best score for maximizing layer"""

            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            moves = game.get_legal_moves()

            # if no moves left
            if not moves:
                return game.utility(self)
            # if end of depth
            if depth == 0:
                return self.score(game, self)           
            
            # initialize best score
            best_score = float('-inf')
            # update best score by iterating over all legal moves
            for move in moves:
                best_score = max(best_score, min_play(self, game.forecast_move(move), depth-1))
            return best_score

        ### BODY OF MINIMAX
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # get the list of all legal moves for the active player
        moves = game.get_legal_moves()
        # initialize best move
        best_move = (-1, -1)
        best_score = float('-inf')

        # if no available moves
        if not moves:
            return best_move
        # if max depth reached
        if depth == 0:
            return best_move

        f = lambda m: min_play(self, game.forecast_move(m), depth-1)
        return max(moves, key=f)



class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. 
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move and depth_limit
        best_move = (-1, -1)
        depth_limit = 100

        # if no legal moves
        moves = game.get_legal_moves()
        if not moves:
            return best_move

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            for depth in range(depth_limit):
                best_move = self.alphabeta(game, depth+1)
                
                if best_move == (-1, -1):
                    break

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Depth-limited minimax search with alpha-beta pruning.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers
 
        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        """

        def min_play(self, game, depth, alpha, beta):
            """function used by alphabeta to return best score for minimizing layer"""

            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            moves = game.get_legal_moves()
            
            # check if end of game or end of search tree
            if not moves:
                return game.utility(self)  
            if depth == 0:
                return self.score(game, self)      

            # initialize best score
            best_score = float('inf')

            for move in moves:
                best_score = min(best_score, max_play(self, game.forecast_move(move), 
                                                        depth-1, alpha, beta))
                # prune if branch best score smaller than alpha
                if best_score <= alpha:
                    return best_score
                # update beta
                beta = min(beta, best_score)
            return best_score

            
        def max_play(self, game, depth, alpha, beta):
            """function used by alphabeta to return best score for maximizing layer"""

            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            moves = game.get_legal_moves()
            
            # check if end of game or end of search tree
            if not moves:
                return game.utility(self)
            if depth == 0:
                return self.score(game, self) 

            # initialize best score
            best_score = float('-inf')
            
            for move in moves:
                best_score = max(best_score, min_play(self, game.forecast_move(move),
                                                        depth-1, alpha, beta))
                # prune if best score larger than beta
                if best_score >= beta:
                    return best_score
                # update alpha
                alpha = max(alpha, best_score)
            return best_score
 

        ### BODY OF ALPHABETA
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # get the list of all legal moves for the active player
        moves = game.get_legal_moves()
        # initialize the best move and best score 
        best_move = (-1, -1)
        best_score = float('-inf')

        # test if end of game
        if not moves:
            return best_move
        # test if end of search depth
        if depth == 0:
            return best_move

        for move in moves:
            score = min_play(self, game.forecast_move(move), depth-1, alpha, beta)
            # prune if branch yields score better than beta
            if score >= beta:
                return move
            # otherwise remember score and move
            if score > best_score:
                best_move = move
                best_score = score
            # update alpha
            alpha = max(alpha, best_score)

        return best_move 
   
        
    
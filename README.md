# Artificial Intelligence Projects 

This repo contains projects for Udacity AI Nanodegree 

## Environment Setup

The projects are run in an environment with Python 3 and all necessary packages installed. The environment can be created and configured by following the steps below:

1. ```conda env create -f aind-environment-osx.yml``` to create the environment (for OSX)  
2. ```source activate aind``` to enter environment  
3. ```pip install git+https://github.com/hmmlearn/hmmlearn.git``` to install the development version of `hmmlearn 0.2.1`


**Install Pygame**  
1. Install homebrew  
2. ```brew install sdl sdl_image sdl_mixer sdl_ttf portmidi mercurial``` 
3. ```source activate aind``` 
4. ```pip install pygame``` 

--- 

## Project 1: Sudoku Solver (`sudoku/`)
Used constraint propagation to 
- solve naked twins problem by enforcing the constraint that no squares outside the naked twins squares can contain the twin values
- implement solver for diagonal sudoku in which diagonals are added to the set of constraints. 

--- 

## Project 2: Game-playing Agent (`isolation/`)
Developed an adversarial search agent to play a deterministic, two-player game of perfect information called 'isolation', in which the players alternate turns moving a single piece from one cell to another on a board and the first player with no remaining legal moves loses.   
- Implemented depth-limited minimax search, minimax search with alpha-beta pruning, and iterative deepening search.   
- Implemented custom evaluation heuristics and evaluated the performance of the heuristics by competing against baseline agents with alpha-beta search and iterative deepening.  

--- 

## Project 3: Traveling Salseman (`travel/`)
- Implemented simulated annealing algorithm to solve the traveling saleseman problem between US state capitals, which is an optimization problem that seeks to find the shortest path passing through every city exactly once.   
- Compared different cooling schedule functions used for simulated annealing, including linear, exponential, quadratic, and logarithmical functions.  

---  

## Project 4: N-Queens Solver (`n-queens/`)  
Used symbolic math library to explicitly construct binary constraints and then use Backtracking to solve the N-queens problem, a game in which N queens are to be placed on a standard NxN chessboard such that none of the queens are in "check" (i.e., no two queens occupy the same row, column, or diagonal).  

---  

## Project 5: Implement a Planning Search (`planning/`)  
- Implemented progression search algorithms to solve deterministic logistics planning problems for an Air Cargo transport system using a planning search agent    
- Implemented two different domain-independent heuristics to aid A* search for the agent   
- Compared result metrics including optimality, search time, and node expansions between non-heuristic search algorithms (breadth-first, depth-first, etc.) and heuristic search algorithms (A* search with custom heuristic functions) 


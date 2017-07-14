
# Build a Game-playing Agent

![Example game of isolation](./images/viz.gif)

## Introduction

In this project, an adversarial search agent is developed to play the game "Isolation". Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board. Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner. These rules are implemented in the `isolation.Board` class in the repository. 

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard). The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess). Additionally, agents will have a fixed time limit each turn to search for the best move and respond. If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.

## Game Visualization

To visualize the game, run
1. ```python -m http.server 8000``` from project directory (if 8000 is unavailable, replace it with another port number),  
2. open browser ```http://localhost:8000/isoviz/display.html```  
3. Enter the move history of an isolation match (i.e., the array returned by the Board.play() method) into the text area and run the match.  
4. Refresh the page to run a different game.



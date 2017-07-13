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
Use constraint propagation to 
- solve naked twins problem by enforcing the constraint that no squares outside the naked twins squares can contain the twin values
- implement solver for diagonal sudoku in which diagonals are added to the set of constraints. 

# Artificial Intelligence Projects 

-- Projects of Udacity AI Nanodegree 

## Environment Setup

The projects are run in an environment with Python 3 and all necessary packages installed. The environment can be created and configured by following the steps below:

```conda env create -f aind-environment-osx.yml``` to create the environment (for OSX) 

```source activate aind``` to enter environment

```pip install git+https://github.com/hmmlearn/hmmlearn.git``` to install the development version of `hmmlearn 0.2.1`


**Install Pygame**  
(homebrew installed) 
```
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi mercurial
source activate aind
pip install pygame
```
--- 

## Project 1: Sudoku Solver (`sudoku/`)
Use constraint propagation to 
- solve naked twins problem by enforcing the constraint that no squares outside the naked twins squares can contain the twin values
- implement solver for diagonal sudoku in which diagonals are added to the set of constraints. 

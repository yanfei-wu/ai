# Diagonal Sudoku Solver

This project builds a solver with naked-twin strategy, i.e., enforcing the constraint that no squares outside the two naked twins squares can contain the twin values. The solver can also be extended to solve diagonal sudoku where the diagonals of the board are constraint to have all the numbers between 1 and 9.  

## Environment 
This project runs in **Python 3** with Pygame installed.


## Run 
To test the solution, run 

```
python solution_test.py
```

To view in Python game window, run 

```
python solution.py
```


## Questions
### Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: In the case of naked twins in sudoku, i.e., two boxes belonging to the same unit (row, column, square and/or diagonal) permit the same 2 values, we can thus enforce the constraint that only these two boxes can contain the twin values and we can eliminate the twin values from the possible value lists of all their peers. 

### Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: A diagonal sudoku problem is like a regular sudoku, except that the numbers 1 to 9 should all appear once among the two main diagonals. So in addition to the constraints set by regular units (rows, columns, and squares), we can also use the constraint set by the diagonal units to eliminate the possible values in each empty box. 



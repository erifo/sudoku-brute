# sudoku-solver
Attempts to solve sudoku through deductive reasoning by keeping track of candidates for each cell. 

Originally inteded to bruteforce sudoku without deduction.

Existing algorithms have not been studied, as the purpose of this exercise is to see if I can figure it out on my own.

### Future Improvements
* Strategy: If number X must be in certain region on certain row: Remove X as candidate from cells in different region on same row. Likewise for region-column.
* Thoroughly written comments for the code.
* Visual indicator for newly solved cells each iteration.
* More intelligent algorithm for solving more complex sudoku.
* Option to import and solve multiple sudoku from textfile source.
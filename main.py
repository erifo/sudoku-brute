from classes import Sudoku

def main():
    s = Sudoku()
    
    #First to be tested. 29 clues. Able to solve.
    #s.textToAbsolutes("8..93...2..9....4.7.21..96.2......9..6.....7..7...6..5.27..84.6.3....5..5...62..8")
    
    #Second to be tested. 25 clues. Unable to solve.
    s.textToAbsolutes("7...4...5...2.8.....1.3.2...8.....9.3.2.7.5.6.9.....2...3.6.4.....1.3...9...8...7")
    
    # Third to be tested. 27 clues. Unable to solve. 
    #s.textToAbsolutes("......68.....73..93.9....4549.......8.3.5.9.2.......3696....3.87..68.....28......")
    
    s.solve()


if __name__ == "__main__":
    main()
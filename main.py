from sudoku import Sudoku

def main():
    #29 clues. Able to solve.
    #question = "8..93...2..9....4.7.21..96.2......9..6.....7..7...6..5.27..84.6.3....5..5...62..8"
    
    #27 clues. Able to solve. 
    #question = "......68.....73..93.9....4549.......8.3.5.9.2.......3696....3.87..68.....28......"
    
    #25 clues. Able to solve.
    #question = ".7...52......3..95...2.9.....9.....4.5........8.34..1....9.617..27851...1........"

    #25 clues. Unable to solve.
    #question = "7...4...5...2.8.....1.3.2...8.....9.3.2.7.5.6.9.....2...3.6.4.....1.3...9...8...7"
    
    #26 clues. Unable to solve. Supposedly "Evil" difficulty.
    question = ".....8...64.5....75..79....49....2...83...17...5....69....75..67....2.48...1....."

    s = Sudoku(debug=True)
    s.textToAbsolutes(question)
    s.solve()
    answer = s.absolutesToText()
    print(answer)


if __name__ == "__main__":
    main()
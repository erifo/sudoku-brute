from classes import Sudoku

def main():
    s = Sudoku()
    s.textToAbsolutes("8..93...2..9....4.7.21..96.2......9..6.....7..7...6..5.27..84.6.3....5..5...62..8")
    s.solve()


if __name__ == "__main__":
    main()


# NOTE
# Adding correct numbers one by one does not work on all sudoku.
# Guesswork might be necessary.
# Time to look up strategies for solving sudoku as a regular human bean.
# I'd also prefer to have number validation happen in Sudoku rather than Cell in the future.
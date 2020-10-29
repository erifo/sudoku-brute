from classes import Sudoku

def main():
    s = Sudoku()
    s.textToAbsolutes("8..93...2..9....4.7.21..96.2......9..6.....7..7...6..5.27..84.6.3....5..5...62..8")
    s.solve()


if __name__ == "__main__":
    main()


# TODO
# Compare for horizontal and vertical. Not just inside the 3x3.
# Visual indicator in console for which numbers are new?
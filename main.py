import tictactoe

def main():
    game = tictactoe.Game()
    print(game)
    game.place_piece(0, 2, "X")
    print(game)
    game.place_piece(1, 1, "X")
    print(game)
    game.place_piece(2, 0, "X")
    print(game)
    print(game.is_won())


if __name__ == "__main__":
    main()

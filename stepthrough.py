from tabular_model import tabular_mcts
from tictactoe_module import tictactoe_methods

if __name__ == "__main__":
    tictactoe_functions = tictactoe_methods()
    board = tictactoe_functions.get_initial_board()
    board = [1,2,1,2,0,0,2,0,1]
    model = tabular_mcts()
    turn = 1

    # track that simulation hardcore
    while(input() == "n"):
        model.simulate_step(board,turn,debug=True)
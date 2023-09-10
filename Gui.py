import time
from typing import Union

from chess import Board
from chessboard import display


class Gui:

    def __init__(self) -> None:
        self.board: Union[display, None] = None
        self.board_ghost: Board = Board()

    def show(self) -> None:
        self.board = display.start()
        while True:
            display.check_for_quit()
            time.sleep(.3)

    def kill(self) -> None:
        self.board.terminate()

    def update(self, move: str) -> None:
        self.board_ghost.push_san(move)
        fen: str = self.board_ghost.fen()
        display.update(fen=fen, game_board=self.board)


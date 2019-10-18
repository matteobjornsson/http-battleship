
from typing import *

class Battleship:

    def __init__(self, board_path: str):
        self.opp_board = self.read_board(board_path)
        self.own_board = self.create_own_board()
        self.dim = self.get_game_dim()
    
    def get_game_dim(self):
        return (len(self.opp_board[0]), len(self.opp_board[1]))

    def create_own_board(self) -> List[List[str]]:
        return [["_" for i in range(10)] for i in range(10)]

    def read_board(self, board_path: str) -> List[List[str]]:

        with open(board_path) as board_file:
            board_text = board_file.readlines()

        return [self.process_board_line(line) for line in board_text]

    def process_board_line(self, board_line: str) -> List[str]:
        return list(board_line.strip("\n"))

    def validate_coordinates(self, x: int, y: int) -> int:

        if x < 0 or x >= self.dim[0] or y < 0 or y >= self.dim[1]:
            return 0
        else:
            return 1

    # Maybe do not return sink item unless actually sunk
    def receive_fire(self, x: int, y: int) -> str:


        if self.opp_board[y][x] == "_":
            self.own_board[y][x] = "M"
            return {"hit": 0}
        elif self.opp_board[y][x] == "M" or self.opp_board[y][x] == 'X':
            return {"hit": -1}
        else:
            # Ship sunk
            ship_code = self.opp_board[y][x]
            self.own_board[y][x] = "X"
            self.opp_board[y][x] = "X"

            if self.check_if_sunk(ship_code) == True:
                return {"hit": 1, "sink": ship_code}
            else:
                return {"hit": 1}
                
    # Checks if ship_code exists anywhere in board
    # Makes an assumption that only one ship per type is allowed
    def check_if_sunk(self, ship_code: str) -> bool:
        return not any([ship_code in row for row in self.opp_board])

    def format_board(self, board: List[List[str]]) -> str:
        return "\n".join("".join(row) for row in board)

    def print_own_board(self) -> None:
        print(self.format_board(self.own_board))

    def print_opp_board(self) -> None:
        print(self.format_board(self.opp_board))

    # write board to HTML
    # used as reference: https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python
    
    def format_html_board(self, board: List[List[str]]) -> str:
        return "<br>".join("".join(row) for row in board)

    def generate_board_html(self, board: List[List[str]]) -> str:
        html_board = """<html>
        <head>
        <style>
        * {font-family: monospace}
        </style>
        </head>
        <body><p>"""\
        + self.format_html_board(board) \
        + """</p></body>
        </html>"""
        return html_board

    def write_opp_board_to_html(self, file: str) -> None:
        f = open(file, 'w')
        html_board = self.generate_board_html(self.opp_board)
        f.write(html_board)
        f.close()

    def write_own_board_to_html(self, file: str) -> None:
        f = open(file, 'w')
        html_board = self.generate_board_html(self.own_board)
        f.write(html_board)
        f.close()

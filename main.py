import re #regex
p1_boats = []
p2_boats = []
ref = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

# 15x15 Tabuleiro
class Board:
    def __init__(self) -> None:
        # Campo da batalha naval
        self.board: dict = {
            "A": [0 for a in range(15)],
            "B": [0 for a in range(15)],
            "C": [0 for a in range(15)],
            "D": [0 for a in range(15)],
            "E": [0 for a in range(15)],
            "F": [0 for a in range(15)],
            "G": [0 for a in range(15)],
            "H": [0 for a in range(15)],
            "I": [0 for a in range(15)],
            "J": [0 for a in range(15)],
            "K": [0 for a in range(15)],
            "L": [0 for a in range(15)],
            "M": [0 for a in range(15)],
            "N": [0 for a in range(15)],
            "O": [0 for a in range(15)],
            "P": [0 for a in range(15)]
		}

        # Peças
        self.boats: dict = {
            "encouraçado": {
                "id": 1,
                "pos": 4,
                "qtd": 5
            },
            "porta-aviões": {
                "id": 2,
                "pos": 5,
                "qtd": 2
            },
            "submarino": {
                "id": 3,
                "pos": 1,
                "qtd": 10
            },
            "cruzador": {
                "id": 4,
                "pos": 2,
                "qtd": 5
            }
        }

class Player:
    def __init__(self, file: str) -> None:
        self.file = open(file, 'r')
        self.board = Board()
        self.peca_pos = {}
        self.readfile()

    def readfile(self):
        for line in self.file:
            # Usando REGEX
            # 1;A2V|C7H
            id_peca    = re.search('.(?=\;)', line).group()
            self.peca_pos.update({id_peca: {}})
            pos_peca   = line.split(";")[1].replace('\n', '').split('|')
            for i, n in enumerate(pos_peca):
                self.peca_pos[id_peca].update({i: {'places': [n[:-1]], 'orientation': [n[-1]]}})


            print(self.peca_pos)


class Game:
    def __init__(self, j1, j2) -> None:
        self.j1 = j1
        self.j2 = j2
        self.winner()

    def winner(self):
        with open('resultado.txt', 'w') as f:
            f.write("")

if __name__ == '__main__':
    p1 = Player('p1.txt')
    p2 = Player('p2.txt')
    game = Game(p1, p2)
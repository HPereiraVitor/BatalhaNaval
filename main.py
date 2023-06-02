import re #regex
p1_boats = []
p2_boats = []
ref = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

class Error_Handle:
    def __init__(self) -> None:
        pass

    def check_piece_qtty(self, qtty, max_qtty) -> None:
        if qtty >= max_qtty:
            raise Exception("ERROR_NR_PARTS_VALIDATION")
    
    def check_piece_ovw(self, pos_a, pos_b) -> None:
        if pos_a == pos_b:
            raise Exception("ERROR_OVERWRITE_PIECES_VALIDATION")
        
    def check_piece_pos(self, pos) -> None:
        if (pos[0] not in ref) or (int(pos[1:-1]) >= 15):
            raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")

class Helper:
    def __init__(self) -> None:
        pass

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
            "1": {
                "name": 'encouraçado',
                "pos": 4,
                "qtd": 5
            },
            "2": {
                "name": 'porta-aviões',
                "pos": 5,
                "qtd": 2
            },
            "3": {
                "name": 'submarino',
                "pos": 1,
                "qtd": 10
            },
            "4": {
                "name": 'cruzador',
                "pos": 2,
                "qtd": 5
            }
        }

class Player:
    def __init__(self, file: str) -> None:
        self.file = open(file, 'r')
        self.board = Board()
        self.peca_pos = {}
        self.error_handle = Error_Handle()
        self.readfile()

    def readfile(self):
        for line in self.file:
            if line[0] in ("1","2","3","4") and not line.startswith("#"):
                # Usando REGEX
                # 1;A2V|C7H
                id_peca    = re.search('.(?=\;)', line).group()
                self.peca_pos.update({id_peca: {}})
                pos_peca   = line.split(";")[1].replace('\n', '').split('|')
                self.error_handle.check_piece_qtty(len(pos_peca), self.board.boats[id_peca]['qtd'])
                
                for i, n in enumerate(pos_peca):
                    self.peca_pos[id_peca].update({i: []})
                    idx = 0
                    start_pos_l = n[0]
                    start_pos_l_idx = ref.index(start_pos_l)
                    start_pos_n = int(n[1:-1]) if n.endswith("V") or n.endswith("H") else int(n[1:])
                
                    # self.error_handle.check_piece_pos(n)
                    if id_peca == "1":
                        while idx < self.board.boats[id_peca]['pos']:
                            count = idx+1
                
                            if n[-1] == 'V':
                                if start_pos_l_idx+idx >= len(ref):
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                
                            elif n[-1] == 'H':
                                if start_pos_n+(idx) >= len(ref):
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{start_pos_l}{start_pos_n+(idx)}')

                            idx += 1

                    elif id_peca == "2":
                        while idx < self.board.boats[id_peca]['pos']:
                            count = idx+1

                            if n[-1] == 'V':
                                if start_pos_l_idx+count >= len(ref):
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                
                            elif n[-1] == 'H':
                                if start_pos_n+(idx+1) >= len(ref):
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{start_pos_l}{start_pos_n+(idx)}')

                            idx += 1

                    elif id_peca == "3":
                        while idx < self.board.boats[id_peca]['pos']:
                            count = idx+1

                            if (start_pos_l not in ref) or (start_pos_n >= 15):
                                raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                            else:
                                self.peca_pos[id_peca][i].append(n)

                            idx += 1

                    elif id_peca == "4":
                        while idx < self.board.boats[id_peca]['pos']:
                            count = idx+1

                            if n[-1] == 'V':
                                if start_pos_l_idx+count >= len(ref):
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                
                            elif n[-1] == 'H':
                                if start_pos_n+(idx+1) >= len(ref):
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{start_pos_l}{start_pos_n+(idx)}')

                            idx += 1



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
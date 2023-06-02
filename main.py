import re #regex
p1_boats = []
p1_plays = []
p2_boats = []
p2_plays = []
ref = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
game_result = {
    "jogador": "",
    "hits": 0,
    "erros": 0,
    "pontuacao": 0
}

class Error_Handle:
    def __init__(self) -> None:
        pass

    def check_piece_qtty(self, qtty, max_qtty) -> None:
        if qtty > max_qtty:
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
    def __init__(self, file: str, playerId: int) -> None:
        self.file = open(file, 'r')
        self.board = Board()
        self.pId = playerId
        self.peca_pos = {}
        self.error_handle = Error_Handle()
        self.readfile()

    def save_error(self, error):
        with open('resultado.txt', 'w') as f:
            f.write('jogador1' if self.pId == 1 else 'jogador2')
            f.write(error)

    def readfile(self):
        for line in self.file:
            if line[0] in ("1","2","3","4") and not line.startswith("#"):
                # Usando REGEX
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
                                    self.save_error("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    if self.pId == 1:
                                        p1_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    else:
                                        p2_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')

                            elif n[-1] == 'H':
                                if start_pos_n+(idx) >= len(ref):
                                    self.save_error("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{start_pos_l}{start_pos_n+(idx)}')
                                    if self.pId == 1:
                                        p1_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    else:
                                        p2_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')

                            idx += 1

                    elif id_peca == "2":
                        while idx < self.board.boats[id_peca]['pos']:
                            count = idx

                            if n[-1] == 'V':
                                if start_pos_l_idx+count >= len(ref):
                                    self.save_error("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    if self.pId == 1:
                                        p1_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    else:
                                        p2_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')

                            elif n[-1] == 'H':
                                if start_pos_n+(idx+1) >= len(ref):
                                    self.save_error("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{start_pos_l}{start_pos_n+(idx)}')
                                    if self.pId == 1:
                                        p1_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    else:
                                        p2_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')

                            idx += 1

                    elif id_peca == "3":
                        while idx < self.board.boats[id_peca]['pos']:
                            count = idx+1

                            if (start_pos_l not in ref) or (start_pos_n >= 15):
                                self.save_error("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                            else:
                                self.peca_pos[id_peca][i].append(n)
                                if self.pId == 1:
                                    p1_boats.append(n)
                                else:
                                    p2_boats.append(n)

                            idx += 1

                    elif id_peca == "4":
                        while idx < self.board.boats[id_peca]['pos']:
                            count = idx+1

                            if n[-1] == 'V':
                                if start_pos_l_idx+count >= len(ref):
                                    self.save_error("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    if self.pId == 1:
                                        p1_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')
                                    else:
                                        p2_boats.append(f'{ref[start_pos_l_idx+idx]}{start_pos_n}')

                            elif n[-1] == 'H':
                                if start_pos_n+(idx+1) >= len(ref):
                                    self.save_error("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                    raise Exception("ERROR_POSITION_NONEXISTENT_VALIDATION")
                                else:
                                    self.peca_pos[id_peca][i].append(f'{start_pos_l}{start_pos_n+(idx)}')
                                    if self.pId == 1:
                                        p1_boats.append(f'{start_pos_l}{start_pos_n+(idx)}')
                                    else:
                                        p2_boats.append(f'{start_pos_l}{start_pos_n+(idx)}')

                            idx += 1

            elif line[0] == 'T':
                _arr = line.split(';')[1].split('|')
                for _i in _arr:
                    if self.pId == 1:
                        p1_plays.append(_i)
                    else:
                        p2_plays.append(_i)



class Game:
    def __init__(self, j1, j2) -> None:
        self.j1 = j1
        self.j2 = j2
        self.winner()

    def winner(self):
        p1_hits = 0
        p1_erros = 0
        p1_points = 0
        p2_hits = 0
        p2_erros = 0
        p2_points = 0
        for play in p1_plays:
            if play in p2_boats:
                p1_hits += 1
                p1_points += 3
            else:
                p1_erros += 1

        for play in p2_plays:
            if play in p1_boats:
                p2_hits += 1
                p2_points += 3
            else:
                p2_erros += 1

        print(f'''
                jogador1
                {p1_hits}
                {p1_erros}
                {p1_points}
              
              ----------------------------------------------
                jogador2
                {p2_hits}
                {p2_erros}
                {p2_points}
              ''')

        if p1_points > p2_points:
            game_result['jogador'] = "jogador1"
            game_result["hits"] = p1_hits
            game_result['erros'] = p1_erros
            game_result["pontuacao"] = p1_points
        elif p1_points < p2_points:
            game_result['jogador'] = "jogador2"
            game_result["hits"] = p2_hits
            game_result['erros'] = p2_erros
            game_result["pontuacao"] = p2_points
        else:
            game_result = f"jogador1 {p1_hits} {p1_erros} {p1_points}\njogador2 {p2_hits} {p2_erros} {p2_points}"

        with open('resultado.txt', 'w') as f:
            if type(game_result) is dict:
                f.write(f"{game_result['jogador']} {game_result['hits']} {game_result['erros']} {game_result['pontuacao']}")
            else:
                f.write(game_result)

if __name__ == '__main__':
    p1 = Player('p1.txt', 1)
    p2 = Player('p2.txt', 2)
    game = Game(p1, p2)
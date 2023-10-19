class Game:
    """This class represents the chess game read from a pgn file."""

    def __init__(self, event, site, date, round, white_player, black_player, result, moves):
        self.event = event
        self.site = site
        self.date = date
        self.round = round
        self.white_player = white_player
        self.black_player = black_player
        self.result = result
        self.moves = moves


    def __iter__(self):
        self.idx = 0
        return self
    

    def __next__(self):
        if self.idx >= len(self.moves):
            raise StopIteration
        nxt = self.moves[self.idx]
        self.idx += 1
        return nxt


    def get_move(self, move_number):
        if move_number < 1 or move_number > len(self.moves) + 1:
            raise InvalidMoveNumberException()
        return self.moves[move_number - 1]
    

    def get_game_data(self):
        data_str = self.event + '\n' + self.site + '\n' + self.date + '\n' + self.white_player  + '\n' + self.black_player + '\n' + self.result
        return data_str
    
    
    def get_moves_count(self):
        return int(len(self.moves) / 2)
    

class InvalidMoveNumberException(Exception):
    pass
from game import Game

class InvalidPgnFormatException(Exception):
    pass


def read_pgn_file(file_path):
    """
    Files must follow the spec: https://www.chessclub.com/help/PGN-spec
    """
    moves = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            start_idx = line.find('"') + 1
            end_idx = len(line) - 2
            if "Event" in line:
                event = line[start_idx:end_idx]
            elif "Site" in line:
                site = line[start_idx:end_idx]
            elif "Date" in line:
                date = line[start_idx:end_idx]
            elif "Round" in line:
                round = line[start_idx:end_idx]
            elif "White" in line:
                white_player = line[start_idx:end_idx]
            elif "Black" in line:
                black_player = line[start_idx:end_idx]
            elif "Result" in line:
                result = line[start_idx:end_idx]
            else:
                if not line == "":
                    strings = line.split(' ')
                    for string in strings:
                        # todo: how to handle comments?
                        if not '.' in string and not '{' in string:
                            if len(string) > 5: # a rough little format check
                                print('ERROR: ' + string)
                                raise InvalidPgnFormatException()
                            moves.append(string)
        
        moves.pop() # remove result of game from moves
        return Game(event, site, date, round, white_player, black_player, result, moves)
    


if __name__ == "__main__":
    file_path = 'files/Bobby Fischer_vs_Boris V Spassky_1992.09.02.pgn'
    my_game = read_pgn_file(file_path)

    print(my_game.get_game_data())

    print(my_game.get_move(10))
    print(my_game.get_moves_count())
    print(my_game.moves)
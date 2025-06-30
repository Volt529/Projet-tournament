from models.player import Player
from utils.json_handler import load_data, save_data

PLAYERS_FILE = "data/players.json"

class PlayerController:
    def __init__(self):
        self.players = [Player.from_dict(d) for d in load_data(PLAYERS_FILE)]

    def add_player(self, first_name, last_name, birth_date, gender, ranking):
        new_player = Player(first_name, last_name, birth_date, gender, ranking)
        self.players.append(new_player)
        self.save_players()

    def save_players(self):
        data = [player.to_dict() for player in self.players]
        save_data(PLAYERS_FILE, data)

    
    def list_players(self):
        """Retourne la liste de tous les joueurs"""
        return self.players

    def get_player_by_id(self, player_id):
        """Trouve un joueur par son ID"""
        for player in self.players:
            if player.id == player_id:
                return player
        return None

    
    def get_sorted_players(self, sort_by="alpha"):
        """Retourne les joueurs triés"""
        if sort_by == "alpha":
            return sorted(self.players, key=lambda p: (p.last_name, p.first_name))
        else:  # par classement
            return sorted(self.players, key=lambda p: p.ranking, reverse=True)
import uuid
from datetime import datetime
from models.round import Round

class Tournament:
    def __init__(self, name, location, start_date, end_date, description="", number_of_rounds=4):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.players = []
        self.rounds = []
        self.current_round = 0

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "players": [player.id for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
            "current_round": self.current_round
        }

    @classmethod
    def from_dict(cls, data, player_controller):
        tournament = cls(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data["description"],
            data["number_of_rounds"]
        )
        tournament.id = data["id"]
        tournament.current_round = data["current_round"]
        
        # Reconstruire les joueurs à partir des IDs
        tournament.players = [
            player_controller.get_player_by_id(player_id) 
            for player_id in data["players"]
        ]
        
        # Reconstruire les rounds
        tournament.rounds = [
            Round.from_dict(round_data, player_controller)
            for round_data in data["rounds"]
        ]
        
        return tournament
from datetime import datetime
from models.match import Match
class Round:
    def __init__(self, name, start_time=None, end_time=None):
        self.name = name
        self.start_time = start_time or datetime.now().isoformat()
        self.end_time = end_time
        self.matches = []

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.to_dict() for match in self.matches]
        }

    @classmethod
    def from_dict(cls, data, player_controller):
        round_obj = cls(
            data["name"],
            data["start_time"],
            data["end_time"]
        )
        
        round_obj.matches = [
            Match.from_dict(match_data, player_controller)
            for match_data in data["matches"]
        ]
        
        return round_obj

    def end_round(self):
        self.end_time = datetime.now().isoformat()
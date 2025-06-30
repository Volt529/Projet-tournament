import uuid

class Player:
    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "ranking": self.ranking
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(
            data["first_name"],
            data["last_name"],
            data["birth_date"],
            data["gender"],
            data["ranking"]
        )
        player.id = data["id"]
        return player

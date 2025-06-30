from models.tournament import Tournament
from utils.json_handler import load_data, save_data

TOURNAMENTS_FILE = "data/tournaments.json"

class TournamentController:
    def __init__(self, player_controller):
        self.player_controller = player_controller
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        tournaments_data = load_data(TOURNAMENTS_FILE)
        return [
            Tournament.from_dict(t_data, self.player_controller)
            for t_data in tournaments_data
        ]

    def save_tournaments(self):
        data = [tournament.to_dict() for tournament in self.tournaments]
        save_data(TOURNAMENTS_FILE, data)

    def create_tournament(self, name, location, start_date, end_date, description=""):
        """Crée un nouveau tournoi et le sauvegarde"""
        new_tournament = Tournament(name, location, start_date, end_date, description)
        self.tournaments.append(new_tournament)
        self.save_tournaments()
        return new_tournament

    def update_tournament(self, tournament_id, name, location, start_date, end_date, description):
        """Modifie les informations d'un tournoi existant"""
        tournament = self.get_tournament_by_id(tournament_id)
        if tournament:
            tournament.name = name
            tournament.location = location
            tournament.start_date = start_date
            tournament.end_date = end_date
            tournament.description = description
            self.save_tournaments()
            return True
        return False

    def list_tournaments(self):
        """Retourne la liste complète des tournois"""
        return self.tournaments

    def get_tournament_by_id(self, tournament_id):
        """Récupère un tournoi spécifique par son ID"""
        for tournament in self.tournaments:
            if tournament.id == tournament_id:
                return tournament
        return None

    def add_player_to_tournament(self, tournament_id, player_id):
        """Ajoute un joueur à un tournoi"""
        tournament = self.get_tournament_by_id(tournament_id)
        player = self.player_controller.get_player_by_id(player_id)
        
        if tournament and player:
            if player not in tournament.players:
                tournament.players.append(player)
                self.save_tournaments()
                return True
        return False
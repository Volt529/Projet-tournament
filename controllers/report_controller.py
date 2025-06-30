class ReportController:
    def __init__(self, player_controller, tournament_controller):
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller

    def list_all_players_alphabetical(self):
        """Liste tous les joueurs par ordre alphabétique"""
        return sorted(self.player_controller.list_players(), 
                    key=lambda p: (p.last_name, p.first_name))

    def list_all_tournaments(self):
        """Liste tous les tournois"""
        return self.tournament_controller.list_tournaments()

    def list_tournament_rounds_and_matches(self, tournament_id):
        """Liste les rounds et matches d'un tournoi spécifique"""
        tournament = self.tournament_controller.get_tournament_by_id(tournament_id)
        return tournament.rounds if tournament else []
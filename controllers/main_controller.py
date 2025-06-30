from views.main_menu_view import MainMenuView
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.report_view import ReportView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController

class MainController:
    def __init__(self):
        # Initialisation des contrôleurs
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(self.player_controller)
        self.report_controller = ReportController(self.player_controller, self.tournament_controller)
        
        # Initialisation des vues
        self.main_view = MainMenuView()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.report_view = ReportView()

    def run(self):
        """Point d'entrée principal de l'application"""
        while True:
            choice = self.main_view.display_main_menu()
            
            if choice == "1":  # Menu Joueurs
                self.manage_players()
            elif choice == "2":  # Menu Tournois
                self.manage_tournaments()
            elif choice == "3":  # Rapports
                self.generate_reports()
            elif choice == "4":  # Quitter
                print("Au revoir !")
                break
            else:
                print("Option invalide, veuillez réessayer.")

    def manage_players(self):
        """Version simplifiée sans choix de tri"""
        while True:
            choice = self.player_view.display_player_menu()
        
            if choice == "1":  # Ajouter joueur
                player_data = self.player_view.get_player_info()
                try:
                    self.player_controller.add_player(*player_data)
                    self.player_view.display_success("Joueur ajouté avec succès")
                except Exception as e:
                    self.player_view.display_error(f"Erreur: {str(e)}")
                
            elif choice == "2":  # Modifier classement
                self.update_player_ranking()
            
            elif choice == "3":  # Lister joueurs (toujours par ordre alphabétique)
                players = self.player_controller.list_players()
                self.player_view.display_players(players)
            
            elif choice == "4":  # Retour
                break
            else:
                self.player_view.display_error("Option invalide")

    def update_player_ranking(self):
        """Gère la modification du classement d'un joueur"""
        players = self.player_controller.list_players()
        self.player_view.display_players(players)
        
        choice = self.player_view.select_player(players)
        try:
            if choice == "0":
                return
                
            index = int(choice) - 1
            if 0 <= index < len(players):
                player = players[index]
                new_ranking = self.player_view.get_new_ranking(player)
                player.ranking = int(new_ranking)
                self.player_controller.save_players()
                self.player_view.display_success("Classement mis à jour")
            else:
                self.player_view.display_error("Numéro invalide")
        except ValueError:
            self.player_view.display_error("Veuillez entrer un nombre valide")

    def manage_tournaments(self):
        """Gestion simplifiée des tournois"""
        while True:
            choice = self.tournament_view.display_tournament_menu()
        
            if choice == "1":  # Créer tournoi
                self.create_tournament()
                
            elif choice == "2":  # Modifier tournoi
                self.modify_tournament()
            
            elif choice == "3":  # Lister tournois
                tournaments = self.tournament_controller.list_tournaments()
                self.tournament_view.display_tournaments(tournaments)
            
            elif choice == "4":  # Retour
                break
            else:
                self.tournament_view.display_error("Option invalide")

    def create_tournament(self):
        """Crée un nouveau tournoi"""
        tournament_data = self.tournament_view.get_tournament_info()
        try:
            self.tournament_controller.create_tournament(*tournament_data)
            self.tournament_view.display_success("Tournoi créé avec succès")
        except Exception as e:
            self.tournament_view.display_error(f"Erreur: {str(e)}")

    def modify_tournament(self):
        """Modifie un tournoi existant"""
        tournaments = self.tournament_controller.list_tournaments()
        if not tournaments:
            self.tournament_view.display_error("Aucun tournoi à modifier")
            return
    
        self.tournament_view.display_tournaments(tournaments)
        choice = self.tournament_view.select_tournament(tournaments)
    
        if 0 <= choice < len(tournaments):
            tournament = tournaments[choice]
            new_data = self.tournament_view.get_tournament_info(tournament)
            try:
                self.tournament_controller.update_tournament(tournament.id, *new_data)
                self.tournament_view.display_success("Tournoi modifié avec succès")
            except Exception as e:
                self.tournament_view.display_error(f"Erreur: {str(e)}")
        else:
            self.tournament_view.display_error("Sélection invalide")
    
    def generate_reports(self):
        """Gère le menu des rapports simplifié"""
        while True:
            choice = self.report_view.display_report_menu()
        
            if choice == "1":  # Joueurs (alpha)
                players = self.report_controller.list_all_players_alphabetical()
                self.report_view.display_players(players)
            
            elif choice == "2":  # Liste tournois
                tournaments = self.report_controller.list_all_tournaments()
                self.report_view.display_tournaments(tournaments)
            
            elif choice == "3":  # Détails tournoi
                tournament_id = self.select_tournament()
                if tournament_id:
                    rounds = self.report_controller.list_tournament_rounds_and_matches(tournament_id)
                    self.report_view.display_rounds_and_matches(rounds)
                
            elif choice == "4":  # Retour
                break
            else:
                self.report_view.display_error("Option invalide")

    def create_tournament(self):
        """Crée un nouveau tournoi"""
        tournament_data = self.tournament_view.get_tournament_info()
        try:
            self.tournament_controller.create_tournament(*tournament_data)
            self.tournament_view.display_success("Tournoi créé avec succès")
        except Exception as e:
            self.tournament_view.display_error(f"Erreur: {str(e)}")

    def select_tournament(self):
        """Sélectionne un tournoi dans la liste"""
        tournaments = self.tournament_controller.list_tournaments()
        if not tournaments:
            self.report_view.display_error("Aucun tournoi disponible")
            return None
            
        self.report_view.display_tournaments(tournaments)
        choice = input("Sélectionnez le numéro du tournoi (0 pour annuler) : ")
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(tournaments):
                return tournaments[index].id
            return None
        except ValueError:
            return None

    def add_players_to_tournament(self):
        """Ajoute des joueurs à un tournoi"""
        # Implémentation à compléter
        pass

    def start_tournament(self):
        """Démarre un tournoi"""
        # Implémentation à compléter
        pass

    def manage_rounds(self):
        """Gère les rounds d'un tournoi"""
        # Implémentation à compléter
        pass
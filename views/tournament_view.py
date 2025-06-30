class TournamentView:
    @staticmethod
    def display_tournament_menu():
        """Menu simplifié de gestion des tournois"""
        print("\n=== MENU TOURNOIS ===")
        print("1. Créer un nouveau tournoi")
        print("2. Modifier un tournoi existant")
        print("3. Lister tous les tournois")
        print("4. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    def get_tournament_info(tournament=None):
        """Saisie des informations du tournoi (nouveau ou modification)"""
        print("\n--- INFORMATIONS TOURNOI ---")
        name = input(f"Nom du tournoi [{tournament.name if tournament else ''}]: ") or (tournament.name if tournament else "")
        location = input(f"Lieu [{tournament.location if tournament else ''}]: ") or (tournament.location if tournament else "")
        start_date = input(f"Date de début (JJ/MM/AAAA) [{tournament.start_date if tournament else ''}]: ") or (tournament.start_date if tournament else "")
        end_date = input(f"Date de fin (JJ/MM/AAAA) [{tournament.end_date if tournament else ''}]: ") or (tournament.end_date if tournament else "")
        description = input(f"Description [{tournament.description if tournament else ''}]: ") or (tournament.description if tournament else "")
        return name, location, start_date, end_date, description

    @staticmethod
    def display_tournaments(tournaments):
        """Affichage de la liste des tournois"""
        print("\n--- LISTE DES TOURNOIS ---")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"\n{idx}. {tournament.name} - {tournament.location}")
            print(f"   Dates: {tournament.start_date} au {tournament.end_date}")
            print(f"   Description: {tournament.description}")
            

    @staticmethod
    def select_tournament(tournaments):
        """Sélection d'un tournoi dans la liste"""
        print("\nSélectionnez un tournoi :")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament.name}")
        choice = input("Numéro du tournoi (0 pour annuler) : ")
        try:
            return int(choice) - 1
        except ValueError:
            return -1

    @staticmethod
    def display_success(message):
        print(f"\n✓ {message}")

    @staticmethod
    def display_error(message):
        print(f"\n✗ Erreur : {message}")
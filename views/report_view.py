class ReportView:
    @staticmethod
    def display_report_menu():
        """Menu simplifié des rapports"""
        print("\n=== MENU RAPPORTS ===")
        print("1. Liste de tous les joueurs (alphabétique)")
        print("2. Liste de tous les tournois")
        print("3. Détails d'un tournoi (rounds et matches)")
        print("4. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    def display_players(players):
        """Affiche la liste des joueurs"""
        print("\n--- LISTE DES JOUEURS ---")
        for idx, player in enumerate(sorted(players, key=lambda p: (p.last_name, p.first_name)), 1):
            print(f"{idx}. {player.last_name} {player.first_name} - Naissance: {player.birth_date}")

    @staticmethod
    def display_tournaments(tournaments):
        """Affiche la liste des tournois"""
        print("\n--- LISTE DES TOURNOIS ---")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"\n{idx}. {tournament.name} - {tournament.location}")
            print(f"   Du {tournament.start_date} au {tournament.end_date}")
            print(f"   Description: {tournament.description}")

    @staticmethod
    def display_rounds_and_matches(rounds):
        """Affiche les détails d'un tournoi"""
        print("\n--- DÉTAILS DU TOURNOI ---")
        for round in rounds:
            print(f"\n{round.name} (début: {round.start_time}, fin: {round.end_time})")
            for match in round.matches:
                print(f"  {match.player1.last_name} vs {match.player2.last_name}")
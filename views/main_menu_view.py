class MainMenuView:
    @staticmethod
    def display_main_menu():
        """Affiche le menu principal et retourne le choix de l'utilisateur"""
        print("\n=== CHESS TOURNAMENT MANAGER ===")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Rapports")
        print("4. Quitter")
        return input("Votre choix : ")

    @staticmethod
    def display_player_management_menu():
        """Affiche le menu de gestion des joueurs"""
        print("\n--- GESTION DES JOUEURS ---")
        print("1. Ajouter un joueur")
        print("2. Modifier le classement d'un joueur")
        print("3. Liste des joueurs")
        print("4. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    def display_tournament_management_menu():
        """Affiche le menu de gestion des tournois"""
        print("\n--- GESTION DES TOURNOIS ---")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des joueurs à un tournoi")
        print("3. Démarrer un tournoi")
        print("4. Gérer les rounds et matches")
        print("5. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    def display_report_menu():
        """Affiche le menu des rapports"""
        print("\n--- RAPPORTS ---")
        print("1. Liste de tous les joueurs (ordre alphabétique)")
        print("2. Liste de tous les joueurs (par classement)")
        print("3. Liste des joueurs d'un tournoi (ordre alphabétique)")
        print("4. Liste des joueurs d'un tournoi (par classement)")
        print("5. Liste de tous les tournois")
        print("6. Détails d'un tournoi (rounds et matches)")
        print("7. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    def display_message(message):
        """Affiche un message générique"""
        print(f"\n{message}")

    @staticmethod
    def display_error(message):
        """Affiche un message d'erreur"""
        print(f"\nERREUR: {message}")

    @staticmethod
    def get_player_info():
        """Demande les informations d'un nouveau joueur"""
        print("\n--- NOUVEAU JOUEUR ---")
        first_name = input("Prénom : ")
        last_name = input("Nom : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        gender = input("Sexe (M/F) : ")
        ranking = input("Classement : ")
        return first_name, last_name, birth_date, gender, ranking

    @staticmethod
    def get_tournament_info():
        """Demande les informations d'un nouveau tournoi"""
        print("\n--- NOUVEAU TOURNOI ---")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début (JJ/MM/AAAA) : ")
        end_date = input("Date de fin (JJ/MM/AAAA) : ")
        description = input("Description (optionnelle) : ")
        return name, location, start_date, end_date, description
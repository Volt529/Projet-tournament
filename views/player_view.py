from utils.validator import Validator

class PlayerView:
    @staticmethod
    def display_player_menu():
        """Affiche le menu de gestion des joueurs"""
        print("\n=== MENU JOUEURS ===")
        print("1. Ajouter un nouveau joueur")
        print("2. Modifier le classement d'un joueur")
        print("3. Lister tous les joueurs (alphabétique)")
        print("4. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    def get_player_info():
        """Nouvelle version avec validation, mais même retour qu'avant !"""
        print("\n--- NOUVEAU JOUEUR ---")
        
        # Saisie validée pour chaque champ
        first_name = Validator.prompt_valid_input(
            "Prénom : ",
            Validator.validate_name,
            "⚠️ Doit contenir 2-50 lettres (pas de chiffres)"
        )
        
        last_name = Validator.prompt_valid_input(
            "Nom : ",
            Validator.validate_name,
            "⚠️ Doit contenir 2-50 lettres (pas de chiffres)"
        )
        
        birth_date = Validator.prompt_valid_input(
            "Date de naissance (JJ/MM/AAAA) : ",
            Validator.validate_date,
            "⚠️ Format invalide. Exemple : 15/05/1990"
        )
        
        gender = Validator.prompt_valid_input(
            "Genre (M/F/NB) : ",
            Validator.validate_gender,
            "⚠️ Répondez par M, F ou NB"
        ).upper()  # Convertit en majuscule
        
        ranking = int(Validator.prompt_valid_input(
            "Classement (nombre ≥ 0) : ",
            Validator.validate_ranking,
            "⚠️ Entrez un nombre positif"
        ))
        
        return first_name, last_name, birth_date, gender, ranking
    
    @staticmethod
    def display_players(players):
        """Affiche la liste des joueurs triés par nom"""
        print("\n--- LISTE DES JOUEURS ---")
        # Tri alphabétique par défaut
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        for i, player in enumerate(sorted_players, 1):
            print(f"{i}. {player.last_name} {player.first_name} - "
                  f"Classement: {player.ranking} - "
                  f"Naissance: {player.birth_date}")


    @staticmethod
    def select_player(players):
        """Permet de sélectionner un joueur dans la liste"""
        print("\nSélectionnez un joueur :")
        for i, player in enumerate(players, 1):
            print(f"{i}. {player.last_name} {player.first_name}")
        choice = input("Numéro du joueur (0 pour annuler) : ")
        return choice

    @staticmethod
    def get_new_ranking(player):
        """Demande le nouveau classement pour un joueur"""
        print(f"\nModification du classement pour {player.last_name} {player.first_name}")
        print(f"Ancien classement : {player.ranking}")
        return input("Nouveau classement : ")

    @staticmethod
    def display_success(message):
        """Affiche un message de succès"""
        print(f"\n✓ {message}")

    @staticmethod
    def display_error(message):
        """Affiche un message d'erreur"""
        print(f"\n✗ Erreur : {message}")

    @staticmethod
    def display_player_details(player):
        """Affiche les détails complets d'un joueur"""
        print("\n--- FICHE JOUEUR ---")
        print(f"Nom complet : {player.last_name} {player.first_name}")
        print(f"Date de naissance : {player.birth_date}")
        print(f"Sexe : {player.gender}")
        print(f"Classement actuel : {player.ranking}")
        print(f"ID : {player.id}")
import re
from datetime import datetime

class Validator:
    @staticmethod
    def validate_date(date_str: str, format: str = "%d/%m/%Y") -> bool:
        """Valide qu'une date est conforme au format (par défaut JJ/MM/AAAA)."""
        try:
            datetime.strptime(date_str, format)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_name(name: str) -> bool:
        """Valide un prénom/nom (lettres, espaces, tirets)."""
        return bool(re.match(r"^[a-zA-ZÀ-ÿ\s-]{2,50}$", name))

    @staticmethod
    def validate_gender(gender: str) -> bool:
        """Valide le genre (M, F, NB)."""
        return gender.upper() in ["M", "F", "NB"]

    @staticmethod
    def validate_ranking(ranking: str) -> bool:
        """Valide que le classement est un entier positif."""
        return ranking.isdigit() and int(ranking) >= 0

    @staticmethod
    def prompt_valid_input(prompt: str, validation_method, error_msg: str, max_attempts: int = 3):
        """Boucle jusqu'à obtenir une saisie valide."""
        for _ in range(max_attempts):
            user_input = input(prompt).strip()
            if validation_method(user_input):
                return user_input
            print(f"❌ {error_msg}")
        raise ValueError(f"Trop de tentatives invalides pour {prompt}")
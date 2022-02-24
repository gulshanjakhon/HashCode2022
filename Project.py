class Project:
    def __init__(self, nbr_days, score, best_before, nbr_roles):
        self.caracteristiques = []
        self.caracteristiques[0] = [nbr_days, score, best_before, nbr_roles]
        self.caracteristiques.append({})


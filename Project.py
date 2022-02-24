class Project:
    def __init__(self, nbr_days, score, best_before, nbr_roles):
        self.details = [nbr_days, score, best_before, nbr_roles]
        self.skills = {}

    def add_skill(self, skill_name, lvl):
        self.skills[skill_name] = lvl
class Project:
    def __init__(self,name, nbr_days, Maxscore, best_before, nbr_roles):
        self.details = [nbr_days, Maxscore, best_before, nbr_roles]
        self.skills = {}
        self.name  = name

    def addSkill(self, skillName, lvl):
        self.skills[skillName] = lvl
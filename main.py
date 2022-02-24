from contributor import Contributor
import Project
files = ["a_an_example.in.txt"]


def process(files):
    for file in files:
        listContributor = []
        listProjet = []
        with open(file, "r") as f:
            C, P = (f.readline().split())
            for i in range(int (C)):
                name, numberSkill = f.readline().split()
                contributor = Contributor(name)
                listContributor.append(contributor)
                for j in range(int (numberSkill)):
                    skill, lvl = f.readline().split()
            for k in range(P):
                name, nbr_days, score, bb, roles = f.readline().split()
                project = Project(name, nbr_days, score, bb, roles)
                for l in range(int(roles)):
                    skill, lvl = f.readline().split()
                    project.add_skill(skill, lvl)
                listProjet.append(project)
            for project in listProjet:
                print(project.name)

        #with open("out/" + file + ".out", 'w+') as f:
        #pass # for output
        
        
if (__name__==  "__main__"):
    process(files)
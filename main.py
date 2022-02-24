from contributor import Contributor

files = ["a_an_example.in.txt"]


def process(files):
    for file in files:
        listContributor = []
        with open(file, "r") as f:
            C, P = (f.readline().split())
            for i in range(int (C)):
                name, numberSkill = f.readline().split()
                contributor = Contributor(name)
                listContributor.append(contributor)
                for j in range(int (numberSkill)):
                    skill, lvl = f.readline().split()
        print(listContributor)
            
            

        #with open("out/" + file + ".out", 'w+') as f:
        #pass # for output
        
        
if (__name__==  "__main__"):
    process(files)
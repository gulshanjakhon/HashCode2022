

files = ["e_elaborate.in"]


def process(files):
    for file in files:
        print("processing")
        with open(file + ".txt", "r") as f:
            C = (int) (f.readline())
            print(C)
            for i in range(C):
                like_content = f.readline().split()
                dislike_content = f.readline().split()
            

        with open("out/" + file + ".out", 'w+') as f:
           pass # for output
        
        
if (__name__==  "__main__"):
    process(files)
import random




with open("1n.txt") as n1, open("2n.txt") as n2, open("3n.txt") as n3, open("4n.txt") as n4, open(
        "1a.txt") as a1, open("2a.txt") as a2, open("3a.txt") as a3, open("4a.txt") as a4, open(
    "1v.txt") as v1, open("2v.txt") as v2, open("3v.txt") as v3, open("4v.txt") as v4, open("Output.txt") as Ou,open("Manualtemplate.txt") as MyFile:
    onenouns = set(line.strip() for line in n1)  # create a set of words from dictionary file
    twonouns = set(line.strip() for line in n2)
    threenouns = set(line.strip() for line in n3)
    fournouns = set(line.strip() for line in n4)
    oneadj = set(line.strip() for line in a1)  # create a set of words from dictionary file
    twoadj = set(line.strip() for line in a2)
    threeadj = set(line.strip() for line in a3)
    fouradj = set(line.strip() for line in a4)
    oneverb = set(line.strip() for line in v1)  # create a set of words from dictionary file
    twoverb = set(line.strip() for line in v2)
    threeverb = set(line.strip() for line in v3)
    fourverb = set(line.strip() for line in v4)
    Out = []
    for i in Ou.read().split():
        Out.append(i)

    #Templ = set(line.strip()) for line in MyFile)
    counter = 0
    for x in MyFile.read().split():
        number = random.randint(0, 10)
        count = 0

        if x == "n1":
            counter +=1
            print (number)
            print (count)
            print ("counter" + str(counter))
            for y in Out:
                if y in onenouns:
                    if count == number:
                        print (y)
                        print (count)

                    count+=1











def countWord () :
    filename = input("Enter the file name : ")
    file = open(filename, "r")
    noWords = 0
    
    for line in file :
        words = line.split()
        noWords = noWords + len(words)
        print("Number of words : ")
        print(noWords)

countWord()
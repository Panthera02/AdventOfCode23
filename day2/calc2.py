sum = 0

with open(".\day2\input.txt") as input:
    for line in input:
        minRed = 0
        minGreen = 0
        minBlue = 0

        id = 0
        inl = ""
        
        ll = line[5:]
        if ll[1] == ':':
            id = int(ll[0])
            inl = line[8:]
        elif ll[2] == ':':
            id = int(ll[0:2])
            inl = line[9:]
        elif ll[3] == ':':
            id = int(ll[0:3])
            inl = line[10:]
        else:
            print("id too high")
        
        index = []
        l = []
        for i in range(len(inl)):
            if inl[i] == ';' or inl[i] == '\n':
                l.append(i)
                index.append(l)
                l = []
            if inl[i] == ',':
                l.append(i)

        lastS = -2
        for semicolon in index:
            lastK = lastS
            for komma in semicolon:
                wort = inl[lastK+2:komma]
                #print(wort)
                num = 0
                farbe = ""
                if wort[1] == ' ':
                    num = int(wort[0])
                    farbe = wort[2:]
                else: 
                    num = int(wort[0:2])
                    farbe = wort[3:]
                lastK = komma
                if farbe == "red" and num > minRed: minRed = num
                if farbe == "green" and num > minGreen: minGreen = num
                if farbe == "blue" and num > minBlue: minBlue = num
            lastS = semicolon[-1]
        
        sum += minRed*minGreen*minBlue
        #print("minRed: " + str(minRed) + "; minGreen: " + str(minGreen) + "; minBlue: " + str(minBlue))
        #print("power: " + str(minRed*minGreen*minBlue) + "; Sum: " + str(sum))        
        #print()
    print(sum)
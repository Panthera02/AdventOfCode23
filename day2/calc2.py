sum = 0

with open(".\day2\input.txt") as input:
    for line in input:
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
        legal = True
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
                if farbe == "red" and num > 12: legal = False
                if farbe == "green" and num > 13: legal = False
                if farbe == "blue" and num > 14: legal = False
                lastK = komma
                if not legal: break
            if not legal: break
            lastS = semicolon[-1]
        
        
        #print(legal)
        if legal:
            sum += id
        #print("ID: " + str(id) + "; Sum: " + str(sum))        
        #print()
    print(sum)
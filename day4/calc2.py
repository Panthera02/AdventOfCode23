summe = 0
debug = True

def p(message):
    if debug:
        print(message)

def parse(array):
    ret = []
    for i in range(len(array)//3+2):
            try:
                ret.append(int(array[i*3:i*3+2]))
            except:
                try:
                    ret.append(int(array[i*3+1:i*3+2]))
                except: continue
    return ret


with open(".\day4\input.txt") as input:
    instances = [1 for _ in range(223)]
    for zeile,line in enumerate(input):
        card = line[10:]
        numbersYH = card[:29]
        winning = card[32:-1]
        p(card)
        myNumbers = parse(numbersYH)
        myWinning = parse(winning)
        matching = 0
        for n in myNumbers:
            if n in myWinning:
                matching += 1
        for i in range(1,matching+1):
            instances[zeile+i] += instances[zeile]

        p("Numbers: " + str(myNumbers) + "\n" + "Winning: " + str(myWinning) + "\n")
    p(instances)
    print(sum(instances))
    
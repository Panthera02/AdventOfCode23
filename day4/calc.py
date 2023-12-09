sum = 0
debug = False

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
    for line in input:
        card = line[10:]
        numbersYH = card[:29]
        winning = card[32:-1]
        p(card)
        myNumbers = parse(numbersYH)
        myWinning = parse(winning)
        points = 0
        for i in myNumbers:
            if i in myWinning:
                if points == 0: points = 1
                else: points *= 2
        sum += points
        
        p("Numbers: " + str(myNumbers) + "\n" + "Winning: " + str(myWinning) + "\n")
    print(sum)
    
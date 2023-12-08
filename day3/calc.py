allSymbols = ['$', '%', '&', '/', '=', '+', '*', '#', '@', '-']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sum = 0
debug = True

with open(".\day3\input.txt") as input:
    numbers = []
    symbols = []
    file = []

    for line in input:
        file.append(line)
        numbersLine = []
        symbolsLine = []

        num = ()
        for i,c in enumerate(line):
            if c in digits:
              num += (i,)
              if line[i+1] == '.' or line[i+1] in allSymbols:
                numbersLine.append(num)
                num = ()
            if c in allSymbols:
                symbolsLine.append(i)

        numbers.append(numbersLine)
        symbols.append(symbolsLine)
    
    for numLine, line in enumerate(numbers):
        for n in line:
            #print(input.readlines())
            #print(n)
            #print(file[numLine])
            num = int(file[numLine][n[0]:n[-1]+1])
            #print(n)
            #print(num)
            legal = False
            if n[0] != 0 and file[numLine][n[0]-1] in allSymbols:
                legal = True
            if file[numLine][n[-1]+1] in allSymbols:
                legal = True
            if n[0] != 0 and numLine != 0 and file[numLine-1][n[0]-1] in allSymbols:
                legal = True
            if numLine != 0 and file[numLine-1][n[-1]+1] in allSymbols:
                legal = True
            if n[0] != 0 and numLine != len(numbers)-1 and file[numLine+1][n[0]-1] in allSymbols:
                legal = True
            if numLine != len(numbers)-1 and file[numLine+1][n[-1]+1] in allSymbols:
                legal = True
            for i in n:
                if legal: break
                if numLine != 0 and file[numLine-1][i] in allSymbols:
                    legal = True
                if numLine != len(numbers)-1 and file[numLine+1][i] in allSymbols:
                    legal = True
            
            if legal:
                print(num)
                sum += num
        if debug:
            print(file[numLine-1])
            print(file[numLine])
            if numLine != len(numbers)-1: print(file[numLine+1])

    #print(numbers)
    #print(symbols)     
       
print(sum)

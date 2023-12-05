digitStrings = ["0","1","2","3","4","5","6","7","8","9"]
digitWords = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitWordsN = {"zero":0,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
#digits = {0,1,2,3,4,5,6,7,8,9}
sum = 0

with open("input.txt") as input:
    for line in input:
        numbers = []
        word = ""
        for c in line:
            if c in digitStrings:
                numbers.append(int(c))
                word = ""
                continue
            word += c
            for i in range(len(word)):
                for j in range(i, len(word)):
                    if word[i:j+1] in digitWords:
                        numbers.append(digitWordsN[word[i:j+1]])
                        word = c
        first = numbers[0]
        last = numbers[-1]
        sum += first*10 + last

print(sum)
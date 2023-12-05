digitWords = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
word = "oneight"

for i in range(len(word)):
    for j in range(i, len(word)):
        print(word[i:j+1] + " " + str(word[i:j+1] in digitWords))
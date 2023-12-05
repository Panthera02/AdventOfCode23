digitStrings = ["0","1","2","3","4","5","6","7","8","9"]
#digits = {0,1,2,3,4,5,6,7,8,9}
sum = 0

with open("input.txt") as input:
    for line in input:
        numbers = []
        for c in line:
            if c in digitStrings:
                numbers.append(int(c))
        first = numbers[0]
        last = numbers[-1]
        sum += first*10 + last

print(sum)
sum = 0

with open("input.txt") as input:
    for line in input:
        id = line[5]
        inl = line[8:]
        index = []
        for i in range(len(inl)):
            if inl[i] is ';':
                index.append(i)
        print(index)
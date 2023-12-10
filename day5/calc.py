def parse(line, first=False):
    dlim = [i for i,c in enumerate(line) if c in " \n"]
    if first: 
        return [int(line[dlim[i]+1:dlim[i+1]]) for i in range(len(dlim)-1)]
    return [int(line[0:dlim[0]])] + [int(line[dlim[i]+1:dlim[i+1]]) for i in range(len(dlim)-1)]
    

with open(".\day5\input.txt") as input:
    abschnitt = 0
    seeds = []
    seedToSoil = {}
    seedToSoilLength = []
    soilToFertilizer = {}
    soilToFertilizerLength = []
    fertilizerToWater = {}
    fertilizerToWaterLength = []
    waterToLight = {}
    waterToLightLength = []
    lightToTemperature = {}
    lightToTemperatureLength = []
    temperatureToHumidity = {}
    temperatureToHumidityLength = []
    humidityToLocation = {}
    humidityToLocationLength = []

    for line in input:
        if line == "\n": abschnitt += 1
        match abschnitt:
            case 0:
                seeds = parse(line, True)
            case 1:
                arr = parse(line)
                seedToSoil[arr[0]] = arr[1]
                seedToSoilLength.append(arr[2])
            case 2:
                arr = parse(line)
                soilToFertilizer[arr[0]] = arr[1]
                soilToFertilizerLength.append(arr[2])
            case 3:
                arr = parse(line)
                fertilizerToWater[arr[0]] = arr[1]
                fertilizerToWaterLength.append(arr[2])
            case 4:
                arr = parse(line)
                waterToLight[arr[0]] = arr[1]
                waterToLightLength.append(arr[2])
            case 5:
                arr = parse(line)
                lightToTemperature[arr[0]] = arr[1]
                lightToTemperatureLength.append(arr[2])
            case 6:
                arr = parse(line)
                temperatureToHumidity[arr[0]] = arr[1]
                temperatureToHumidityLength.append(arr[2])
            case 7:
                arr = parse(line)
                humidityToLocation[arr[0]] = arr[1]
                humidityToLocationLength.append(arr[2])

    for seed in seeds:
        pass
            
    print(seedToSoil)
    print(seedToSoilLength)
    
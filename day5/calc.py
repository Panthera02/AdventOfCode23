def parse(line, first=False):
    dlim = [i for i,c in enumerate(line) if c in " \n"]
    if first: 
        return [int(line[dlim[i]+1:dlim[i+1]]) for i in range(len(dlim)-1)]
    return [int(line[0:dlim[0]])] + parse(line, True)

def translate(elements, dict, dictLength):
    newElements = []
    for e in elements:
        appended = False
        if e in dict.keys():
            newElements.append(dict[e])
            continue
        for i,s in enumerate(dict.keys()):
            if e in range(s, dictLength[i]+1):
                newElements.append(dict[s]+(e-s))
                appended = True
                break
        if appended: continue
        newElements.append(e)
    return newElements
    

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
        if line == "\n": 
            abschnitt += 1
            continue
        if line[0] >= 'a' and not "seeds:" in line: continue
        match abschnitt:
            case 0:
                seeds = parse(line, True)
            case 1:
                arr = parse(line)
                seedToSoil[arr[1]] = arr[0]
                seedToSoilLength.append(arr[2])
            case 2:
                arr = parse(line)
                soilToFertilizer[arr[1]] = arr[0]
                soilToFertilizerLength.append(arr[2])
            case 3:
                arr = parse(line)
                fertilizerToWater[arr[1]] = arr[0]
                fertilizerToWaterLength.append(arr[2])
            case 4:
                arr = parse(line)
                waterToLight[arr[1]] = arr[0]
                waterToLightLength.append(arr[2])
            case 5:
                arr = parse(line)
                lightToTemperature[arr[1]] = arr[0]
                lightToTemperatureLength.append(arr[2])
            case 6:
                arr = parse(line)
                temperatureToHumidity[arr[1]] = arr[0]
                temperatureToHumidityLength.append(arr[2])
            case 7:
                arr = parse(line)
                humidityToLocation[arr[1]] = arr[0]
                humidityToLocationLength.append(arr[2])
    
    soils = translate(seeds, seedToSoil, seedToSoilLength)
    fertilizer = translate(soils, soilToFertilizer, soilToFertilizerLength)
    water = translate(fertilizer, fertilizerToWater, fertilizerToWaterLength)
    light = translate(water, waterToLight, waterToLightLength)
    temperature = translate(light, lightToTemperature, lightToTemperatureLength)
    humidity = translate(temperature, temperatureToHumidity, temperatureToHumidityLength)
    location = translate(humidity, humidityToLocation, humidityToLocationLength)

    print(min(location))
    
    
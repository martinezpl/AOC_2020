def getInput(inputfile):   
    data = []
    with open(inputfile, 'r') as f:
        for line in f:
            if line != '\n':
                 data.append(eval(line.replace("\n", "")))
    return data

def sortAndSearch2(aData):
    aData.sort()
    i = 0
    j = len(aData) - 1
    while i < j:
        if aData[i] + aData[j] == 2020:
            return aData[i], aData[j]
        elif aData[i] < 2020 - aData[j]:
            i += 1
        else:
            j -= 1

def sortAndSearch3(aData):
    aData.sort()
    i = 0
    j = len(aData) - 1
    k = len(aData) // 2
    while True:
        if aData[i] + aData[j] + aData[k] == 2020:
            return aData[i], aData[j], aData[k]
        if aData[i] < 2020 - aData[j]:
            i += 1
        else:
            j -= 1
        

if __name__ == "__main__":
    
    solution =  sortAndSearch3(getInput('input.txt'))
    
    print(solution)
   # print(str(solution[0] * solution[1] * solution[2]))

    

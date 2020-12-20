def entriesGenerator():
    f = open('input.txt', 'r')
    for line in f:
        if line == '\n':
            f.close()
            break
        yield line

def findTwoSumMembers(aList):
    for a in aList:
        for b in aList:
            if a + b == 2020:
                members = (a, b)
                return members

def findThreeSumMembers(aList):
    for a in aList:
        for b in aList:
            for c in aList:
                if a + b + c == 2020:
                    members = (a, b, c)
                    return members




if __name__ == "__main__":

    entries = entriesGenerator()
    entryList = []

    for entry in entries:
        entryList.append(int(entry))

    solution = findThreeSumMembers(entryList)

    print(solution)
    print(str(solution[0] * solution[1] * solution[2]))

    

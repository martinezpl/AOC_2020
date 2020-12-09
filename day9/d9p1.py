dataList = []
with open('input.txt') as f:
    for line in f:
        if line != '\n':
            dataList.append(int(line.strip()))


preambule = []

for i in range(0, 25):
    preambule.append(dataList[i])

buf = []
buf = list(preambule)
search_subject = 0
def findSum(buf, score):
        for x in buf:
            buf2 = list(buf)
            buf2.remove(x)
            for y in buf2:                   
                if x + y == score:
                    return True
        return False

for i in range(25, len(dataList)):
    if findSum(buf, dataList[i]):
        buf.append(dataList[i])
        buf.pop(0)
    else:
        search_subject = dataList[i]
        break

print(search_subject)

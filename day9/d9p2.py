dataList = []
with open('input.txt') as f:
    for line in f:
        if line != '\n':
            dataList.append(int(line.strip()))


weakNum = 3199139634
dataList = dataList[:dataList.index(weakNum)]

contig = []
a = 0
i = 0
while True:
    contig.append(dataList[i])
    if sum(contig) > weakNum:
        a = a+1
        i = a
        print(a)
        contig = []
    elif sum(contig) == weakNum:
        search_subject = min(contig) + max(contig)
        break
    else:
        i += 1

print(search_subject)

timestamp = 1008141

busIDs = "17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,x,x,787,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"
busIDl = busIDs.split(',')
arrivals = {}

viableIDs = [int(i) for i in busIDl if i != 'x']

for ID in viableIDs:
    i = ID
    while i < timestamp:
        i += ID
    arrivals[i] = ID


solution = (min(arrivals.keys()) - timestamp) * arrivals[min(arrivals.keys())]
print(solution)

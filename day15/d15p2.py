def elveGame(starting_sequence):
    spoken = {} 
    start = starting_sequence.split(',')
    turn = 1
    for n in start:
        spoken[int(n)] = ''
    for n in start:
        spoken[int(n)] = f'{turn} ' + spoken[int(n)]
        turn += 1
    cn = start[-1] # considered number

    while turn <= 2020:
        if cn in spoken:
            lastTurnSpoken = int(spoken[cn][:spoken[cn].find(' ')])
            turnBeforeThat = spoken[cn][spoken[cn].find(' '):]
            if len(turnBeforeThat) > 1:
                turnBeforeThat = turnBeforeThat[1:]
                turnBeforeThat = int(turnBeforeThat[:turnBeforeThat.find(' ')])
                spoken[cn] = f'{lastTurnSpoken} {turnBeforeThat}'
                newNumber = lastTurnSpoken - turnBeforeThat
                if newNumber in spoken:
                    spoken[newNumber] = f'{turn} ' + spoken[newNumber]
                else:
                    spoken[newNumber] = f'{turn} '
                cn = newNumber
            else:
                cn = 0
                spoken[cn] = f'{turn} ' + spoken[cn]
        else:
            cn = 0
            spoken[cn] = f'{turn} ' + spoken[cn]
        
        turn +=1


    return cn
        

print(elveGame('19,20,14,0,9,1'))

class Waypoint:
    
    def __init__(self):
        self.coordinates = {'NS': 1, 'WE': -10}
            
    def updateCoords(self, action, value):
        if action == 'N':
            self.coordinates['NS'] += value
        elif action == 'S':
            self.coordinates['NS'] -= value
        elif action == 'W':
            self.coordinates['WE'] += value
        elif action == 'E':
            self.coordinates['WE'] -= value
        else:
            if value == 180:
                self.coordinates['NS'] *= -1
                self.coordinates['WE'] *= -1
            else:
                if action == 'R':
                    if value == 90:
                        self.coordinates['NS'], self.coordinates['WE'] = self.coordinates['WE'], self.coordinates['NS']*-1
                    elif value == 270:
                        self.coordinates['WE'], self.coordinates['NS'] = self.coordinates['NS'], self.coordinates['WE']*-1
                elif action == 'L':
                    if value == 90:
                        self.coordinates['WE'], self.coordinates['NS'] = self.coordinates['NS'], self.coordinates['WE']*-1
                    if value == 270:
                        self.coordinates['NS'], self.coordinates['WE'] = self.coordinates['WE'], self.coordinates['NS']*-1

    def executeInstruction(self, inst):    
        action = inst[:1]
        value = int(inst[1:])
        self.updateCoords(action, value)

class Plane:
    def __init__(self):
        self.coordinates = {'NS': 0, 'WE': 0}

    def forward(self, NS, WE, value):
        self.coordinates['NS'] += NS*value
        self.coordinates['WE'] += WE*value

    def getManhattan(self):
        return abs(self.coordinates['NS']) + abs(self.coordinates['WE'])

if __name__ == '__main__':
    wp = Waypoint()
    pl = Plane()

    with open('input.txt') as f:
        for line in f:
            if len(line) > 1:
                if line.strip()[:1] == 'F':
                    pl.forward(wp.coordinates['NS'], wp.coordinates['WE'], int(line.strip()[1:]))
                else:
                    wp.executeInstruction(line.strip())

    print(pl.getManhattan())    

class coordNavigator:
    
    dirs = ['E', 'S', 'W', 'N']

    def __init__(self, inputFile=None):
        self.coordinates = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
        self.direction = 'E'
        self.compass = 0
        if inputFile:
            self.instructions = []
            with open(inputFile) as f:
                for line in f:
                    if len(line.strip()) > 0:
                        self.instructions.append(line.strip())
            for ins in self.instructions:
                self.executeInstruction(ins)
            
    def updateCoords(self, action, value):
        print(action, value)
        if action == 'F':
            self.coordinates[self.direction] += value
        elif action in self.coordinates.keys():
            self.coordinates[action] += value
        else:
            if action == 'R':
                self.compass += value // 90
            elif action == 'L':
                self.compass -= value // 90
            self.direction = self.dirs[self.compass % 4]

    def executeInstruction(self, inst):    
        print(self.coordinates)
        action = inst[:1]
        value = int(inst[1:])
        self.updateCoords(action, value)

    def getPosition(self):
        ns = [self.coordinates['N'], self.coordinates['S']]
        we = [self.coordinates['W'], self.coordinates['E']]
        x = max(we) - min(we)
        y = max(ns) - min(ns)
        return x, y

if __name__ == '__main__':
    print(sum(coordNavigator('input.txt').getPosition()))


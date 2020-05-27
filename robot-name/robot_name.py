import random

class Robot:
    nomes = []
    def __init__(self):
        prefix = random.sample(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],2)
        self.name = prefix[0] + prefix[1]
        for x in range(3):
            self.name += str(random.randint(0,9))
        Robot.nomes.append(self.name)

    def reset(self):
        prefix = random.sample(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],2)
        while self.name in Robot.nomes:
            prefix = random.sample(['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],2)
            self.name = prefix[0] + prefix[1]
            for x in range(3):
                self.name += str(random.randint(0,9))
        Robot.nomes.append(self.name)
            
             

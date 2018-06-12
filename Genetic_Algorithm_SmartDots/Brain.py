import numpy as np
import math
import random
from vector import Vector


class Brain():


    def __init__(self):
        self.directions = ()
        self.step = int(1)
        self.beststep = 0
        # self.Brain(varSize)

    def Brain(self, size):
        self.directions = np.zeros([size, 2])
        self.randomize()

    def randomize(self):
        for i in range(0, len(self.directions)):
            randomAngle = 2 * math.pi * random.random()
            x = 1 * math.cos(randomAngle)
            y = 1 * math.sin(randomAngle)
            self.directions[i] = np.array((x, y))


    def clone(self):
        cln = Brain()
        cln.Brain(len(self.directions))
        for i in range(0, len(self.directions)):
            cln.directions[i] = self.directions[i]
        return (cln.directions)

    def mutate(self, mutationRate = 0.001, ZeroConstant = 50, Mode = "normal"):
        BCmin = self.beststep - ZeroConstant
        BCmax = self.beststep + (ZeroConstant*2)

        for i in range(0, len(self.directions)):
            if Mode == "normal":
                rand = random.random()

                if rand < mutationRate:
                    randomAngle = 2 * math.pi * random.random()

                    x1 = 1 * math.cos(randomAngle)
                    y1 = 1 * math.sin(randomAngle)
                    self.directions[i] = np.array((x1, y1))

            elif Mode == "triangle":
                randomN = random.random()


                if i < self.beststep:
                    rand = i/(self.beststep - BCmin) - (BCmin/(self.beststep - BCmin))

                    if randomN < rand:
                        randomAngle = 2 * math.pi * random.random()

                        x1 = 1 * math.cos(randomAngle)
                        y1 = 1 * math.sin(randomAngle)
                        self.directions[i] = np.array((x1, y1))

                elif self.beststep < i:
                    rand = (-i)/(BCmax - self.beststep) + (BCmax / (BCmax - self.beststep))

                    if randomN < rand:
                        randomAngle = 2 * math.pi * random.random()

                        x1 = 1 * math.cos(randomAngle)
                        y1 = 1 * math.sin(randomAngle)
                        self.directions[i] = np.array((x1, y1))

# brn = Brain()
# brn.Brain(20)
# print(brn.directions)
# brn.mutate()
# print(brn.directions)
# directions[1] = np.array((5,6))
# print(directions)
# print(directions2)
# #print(directions[2])

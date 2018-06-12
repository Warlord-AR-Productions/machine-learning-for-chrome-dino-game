from Dot import Dot
import random
import numpy as np

class Population():

    def __init__(self,Input):
        self.fitnessSum = float(0)
        self.gen = 1
        self.bestDot = 0
        self.minStep = 700 # minStep should always be the same as number of instructions in the Dot class
        self.dots = []
        self.newDots = []
        self.bestDot = 0
        self.rand = 0
        self.sizedes = 0
        self.maxfitness = 0
        self.reachedGoal = False
        self.reachedGoalCheck = False
        self.firstGenGoal = None


        self.population(Input)

    def population(self, size):
        for i in range(0,size):
            Adot = Dot()
            self.dots.append(Adot)


        self.sizedes = size

    # def newGen(self): # test
    #     for i in range(0,self.sizedes):
    #         Adot = Dot()
    #         self.dots.append(Adot)


    def show(self):
        for i in range(1,len(self.dots)):
            self.dots[i].show()
        self.dots[0].show()

    def update(self):
        for i in range(0,len(self.dots)):
            if self.dots[i].brn.step > self.minStep:
                self.dots[i].dead = True
            elif self.dots[i].dead or self.dots[i].reachedGoal:
                pass
            else:
                self.dots[i].update()

    def calculateFitness(self):
        for i in range(0,len(self.dots)):
            self.dots[i].calculateFitness()



    def allDotsDead(self):
        for i in range(0,len(self.dots)):
            if not self.dots[i].dead and not self.dots[i].reachedGoal:
                return False
        return True



    def naturalSelection(self):
        Test = Population(len(self.dots))
        self.newDots = Test.dots
        self.setBestDot()
        self.calculateFitnessSum()

        self.newDots[0] = self.dots[self.bestDot].gimmeBaby()
        self.newDots[0].isBest = True
        self.newDots[0].beststep = self.dots[self.bestDot].brn.step
        #new------------------------------------------------------------
        self.newDots[1] = self.dots[self.bestDot].gimmeBaby()
        self.newDots[1].isUnique = True
        # new------------------------------------------------------------
        self.newDots[2] = self.dots[self.bestDot].gimmeBaby()
        self.newDots[2].isAscending = True

        for i in range(3,len(self.newDots)):
            parent = self.selectParent()
            # hier kan ik nog wat selectie aan toe voegen :D
            self.newDots[i] = parent.gimmeBaby()

        self.dots = self.clone()
        self.gen += 1
        # Set best step for mutation purpose
        self.dots[2].brn.beststep = self.dots[0].beststep



    def clone(self):
        clone = Population(len(self.dots))

        for i in range(0, len(self.newDots)):
            clone.dots[i] = self.newDots[i]
        return clone.dots


    def calculateFitnessSum(self):
        self.fitnessSum = 0
        for i in range(0,len(self.dots)):
            self.fitnessSum += self.dots[i].fitness


    def selectParent(self):
        Value = random.random()
        self.rand = self.fitnessSum * Value

        runningSum = 0

        for i in range(0,len(self.dots)):
            runningSum += self.dots[i].fitness
            if runningSum > self.rand:
                return self.dots[i]

        return 0


    def mutateDemBabies(self):
        for i in range(1,len(self.dots)):
            if i == 1:
                self.dots[i].brn.mutate(0.01)
            elif i == 2:
                self.dots[i].brn.mutate(Mode = "triangle")
            else:
                self.dots[i].brn.mutate()


    def setBestDot(self):
        max = float(0)
        maxIndex = int(0)
        for i in range(0,len(self.dots)):
            if self.dots[i].fitness > max:
                max = self.dots[i].fitness
                maxIndex = i
                self.maxfitness = "%.6f" % max
        self.bestDot = maxIndex




        if self.dots[self.bestDot].reachedGoal:
            minStep = self.dots[self.bestDot].brn.step
            print("step:", minStep)
            self.reachedGoal = True

            if not self.reachedGoalCheck:
                self.firstGenGoal = self.gen
                self.reachedGoalCheck = True

# A = Population(10)
# # print(A.dots[0].brn.directions)
# A.clone()
# print(A.dots[1].brn.directions)
# A.mutateDemBabies()
# print(A.dots[1].brn.directions)
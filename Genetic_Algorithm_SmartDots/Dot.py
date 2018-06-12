import pygame
from vector import Vector

import numpy as np

from Brain import Brain

BLACK = (0,0,0)
from Brain import Brain
import math
import pygame
from Obstacle import Obstacle
from vector import Vector
goal = Vector(375,25)
WHITE = (255, 255, 255)
size = (750, 750)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
Obs = Obstacle()


class Dot():



    def __init__(self):
        self.dead = False
        self.reachedGoal = False
        self.isBest = False
        self.isUnique = False
        self.isAscending = False

        self.brn = ()
        self.brain = ()
        self.acc = []
        self.vel = []
        self.pos = []
        self.fitness = 0
        self.beststep = 0

        self.Dot()


    def Dot(self):
        self.brn = Brain()
        self.brain = self.brn.Brain(700) #making a brain with n-amount of Instructions

        self.pos = Vector(375,725)
        self.vel = Vector(0,0)
        self.acc = Vector(0,0)
        return self.brain


    def show(self):
        if self.isBest:
            pygame.draw.ellipse(screen, (0,255,0), [self.pos.x,self.pos.y,10,10], 0)

        elif self.isUnique:
            pygame.draw.ellipse(screen, (255, 100, 0), [self.pos.x, self.pos.y, 7.5, 7.5], 0)

        elif self.isAscending:
            pygame.draw.ellipse(screen, (255, 100, 255), [self.pos.x, self.pos.y, 7.5, 7.5], 0)

        else:
            pygame.draw.ellipse(screen, BLACK, [self.pos.x,self.pos.y,5,5], 0)


    def move(self):
        if (len(self.brn.directions)>self.brn.step):
            x = self.brn.directions[self.brn.step][0]
            y = self.brn.directions[self.brn.step][1]
            self.acc = Vector(x,y)
            self.brn.step += 1
        else:
            self.dead = True

        self.vel.add(self.acc)
        self.vel.limit(5)
        self.pos.add(self.vel)

    def update(self):
        if not self.dead or not self.reachedGoal:
            self.move()
            if (self.pos.x < 1 or self.pos.y < 1 or self.pos.x > 750-3 or self.pos.y > 750-3): # near wall is dead#
                self.dead = True

            elif (math.sqrt(((self.pos.x - goal.x)**2)+((self.pos.y - goal.y)**2)) < 6): #reached goal
                self.reachedGoal = True

            else:
                #Obstacle Set 1
                # self.dead = Obs.obstacleSet1Boundairy(self.pos)

                #Obstacle Set 2
                self.dead = Obs.obstacleSet2Boundairy(self.pos)

            # elif  # any obstacles

    def calculateFitness(self):
        if (self.reachedGoal): # if the dot reached the goal then the fitness is based on the steps it took to get there
            self.fitness = 1/16 + 1000 / (self.brn.step * self.brn.step)
        else: # if the dot didn't reach the goal then he fitness is based on how close it is to the goal.
            distanceToGoal = math.sqrt(((self.pos.x - goal.x)**2)+((self.pos.y - goal.y)**2))
            self.fitness = 1/ (distanceToGoal * distanceToGoal)

            # Adding new fitness bonus for quick reach to the goal. so going in a certain directions is more beneficial.

    def gimmeBaby(self):
        baby = Dot()
        baby.brn.directions = self.brn.clone()

        return baby



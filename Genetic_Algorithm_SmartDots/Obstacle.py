import pygame

class Obstacle():

    def __init__(self):
        self.crd = 750/5


    def obstacleSet1(self,screen):
        pygame.draw.line(screen, (0,0,255), (300,0), (300,750) , 4)
        pygame.draw.line(screen, (0, 0, 255), (450, 0), (450, 750), 4)

    def obstacleSet1Boundairy(self,Input):
        if Input.x < 300 or Input.x > 450:
            Input.dead = True
            return (Input.dead)

    def obstacleSet2(self,screen):
        self.crd = (750/5)
        pygame.draw.line(screen, (0, 0, 255), (0, self.crd), (500, self.crd), 5)
        pygame.draw.line(screen, (0, 0, 255), (250, 2 * (self.crd)), (750, 2 * (self.crd)), 5)
        pygame.draw.line(screen, (0, 0, 255), (0, 3 * (self.crd)), (500, 3 * (self.crd)), 5)
        pygame.draw.line(screen, (0, 0, 255), (250, 4 * (self.crd)), (750, 4 * (self.crd)), 5)

    def obstacleSet2Boundairy(self,Input):
        if (self.crd - 2.5) < Input.y < (self.crd + 2.5) and ( 0 )< Input.x < ( 500 ):
            Input.dead = True
            return Input.dead

        elif (2*(self.crd) - 2.5) < Input.y < (2*self.crd + 2.5) and ( 250 )< Input.x < ( 750 ):
            Input.dead = True
            return Input.dead

        elif (3*self.crd - 2.5) < Input.y < (3*self.crd + 2.5) and (0) < Input.x < (500):
            Input.dead = True
            return Input.dead

        elif (4*self.crd - 2.5) < Input.y < (4*self.crd + 2.5) and (250) < Input.x < (750):
            Input.dead = True
            return Input.dead

    # def obstacleSet3(self,screen):


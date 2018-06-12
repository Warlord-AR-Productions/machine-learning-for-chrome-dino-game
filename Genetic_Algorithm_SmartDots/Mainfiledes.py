"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from Population import Population
from vector import Vector
from Obstacle import Obstacle
goal = Vector(10,10)

def main():

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    gen_update = False

    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (750, 750)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    test = Population(500)
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 15)
    myfont3 = pygame.font.SysFont('Comic Sans MS', 15)
    myfont4 = pygame.font.SysFont('Comic Sans MS', 15)
    myfont5 = pygame.font.SysFont('Comic Sans MS', 15)
    Obs = Obstacle()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic should go here
        if not gen_update:
            text = "Gen:" + str(test.gen)
            textsurface = myfont.render(text, False, (0, 0, 0))

            text2 = "Highest Fitness: " + str(test.maxfitness)
            textsurface2 = myfont2.render(text2, False, (255, 0, 0))
            print(test.gen)
            gen_update = True




        if not test.reachedGoalCheck:
            text3 = "Reached Goal: No"
            textsurface3 = myfont3.render(text3, False, (255, 0, 255))
            text4 = "FirstGen: " + str(test.firstGenGoal)
            textsurface4 = myfont4.render(text4, False, (100, 100, 100))

        elif test.reachedGoalCheck:
            text3 = "Reached Goal: Yes:"
            textsurface3 = myfont3.render(text3, False, (255, 100, 1000))
            text4 = "FirstGen: " + str(test.firstGenGoal)
            textsurface4 = myfont4.render(text4, False, (100, 100, 100))

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)
        screen.blit(textsurface, (0, 0))
        screen.blit(textsurface2, (0, 20))
        screen.blit(textsurface3, (0, 35))
        screen.blit(textsurface4, (0, 50))

        # --- Drawing code should go here

        #Goal
        pygame.draw.ellipse(screen, (255, 0, 0), [375,25,goal.x,goal.y], 0)

        #Obstacles

        #Obstacle Set 1
        # Obs.obstacleSet1(screen)

        #Obstacle Set 2
        Obs.obstacleSet2(screen)

        if test.allDotsDead():
            test.calculateFitness()
            test.naturalSelection()
            test.mutateDemBabies()
            gen_update = False
        else:
            test.update()
            test.show()


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()
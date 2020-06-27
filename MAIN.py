
import pygame
import random
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
 
 
def main():
   
    pygame.init()
 
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]

    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Tempo")
 
    DONE = False
 
    clock = pygame.time.Clock()
 
 
    # -------- Main Program Loop -----------
    while not DONE:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True
            
 
        screen.fill(BLACK)
 
        
        clock.tick(60)
 
        
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
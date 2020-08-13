import pygame
import os

#Classs Object - Player
  #Sprite
  #Location 
  #PLayer Health

  #Jump Script

#Class Object - Hazard
  #Sprite
  #Location

  #Movement

  #DoHit Player?

#Class Object - AbstractGameRunner
  #Holds Hazard

  #Make A Hazard

  #Timer 
    #Make a Hazard



#While Loop if Player Health > 0 
  #On AbstractGameRunner. Timer spawn Hazard
  #Player - Jump Movement
  #For each Hazard do "DoHit Player?"

  






img_patch = os.path.join('background2.png')
img_patch = os.path.join('mole.png')

class character(object):
    def __init__(self):
      character.image = pygame.image.load('mole.png')
      self.image = character.image

      self.x = 20
      self.y = 600
      self.hitbox = (self.x,self.y,65,65)
      
      self.x = 50
      self.y = 50
      self.width = 50
      self.height = 50
      self.vel = 5

      self.isJump = False
      self.jumpCount = 10
      self.left = False
      self.right = False 
      self.walkCount = 0


    def draw(self,surface):
      surface.blit(self.image,(self.x,self.y)) 
      self.image = pygame.transform.scale(self.image,(150,100))

    def upcheck():
      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT] and x > vel: 
        x -= vel 
      if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
      if not(isJump):  
        if keys[pygame.K_UP] and y > vel:
          y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
          y += vel
        if keys[pygame.K_SPACE]:
          isJump = True 
      else:
        if jumpCount >= -10:
          neg = 1
          if jumpCount < 0:
            neg = -1
          y == (jumpCount ** 2) * 0.5 * neg
          jumpCount == 1 
        else:
          isJump = False
          jumpCount = 10     



pygame.init()
pygame.display.set_caption("Jumpstacles")
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode(screen_width,screen_height)

jj = character()

running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running=0
    screen.fill((0,0,255))
    pygame.display.flip()
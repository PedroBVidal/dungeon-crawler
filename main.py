import pygame
import constants 
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")
#creating a clock for mantaining frame rate
clock = pygame.time.Clock()


#define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

def scale_img(image,scale):
  w = image.get_width()
  h = image.get_height()
  return pygame.transform.scale(image,(w* scale, h*scale))

player_image = pygame.image.load("assets/images/characters/elf/idle/0.png").convert_alpha()
player_image = pygame.transform.scale(player_image,(player_image.get_width()* constants.SCALE, player_image.get_height()*constants.SCALE))

# create Player 
player = Character(100,100,player_image)

# define player movement variables 
moving_left = False
moving_right = False
moving_up = False
moving_down = False



run = True

while run:
    clock.tick(constants.FPS)

    screen.fill(constants.BG)

    dx = 0
    dy = 0


    if moving_right == True:
        dx = constants.SPEED
    if moving_left == True:
        dx = -constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED

    print(str(dx) + ', ' + str(dy))

    player.move(dx,dy)

    # draw player on the screen 
    player.draw(screen) 

  #event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    #take keyboard presses
      if event.type == pygame.KEYDOWN:
        print("key down")
        if event.key == pygame.K_a:
          moving_left = True
          print("KEY A ")
        if event.key == pygame.K_d:
          moving_right = True
        if event.key == pygame.K_w:
          moving_up = True
        if event.key == pygame.K_s:
          moving_down = True

      #keyboard button released
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
          moving_left = False
        if event.key == pygame.K_d:
          moving_right = False
        if event.key == pygame.K_w:
          moving_up = False
        if event.key == pygame.K_s:
          moving_down = False
      
    pygame.display.update()
pygame.quit()
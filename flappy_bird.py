import pygame ,sys
pygame.init()
def move_base():
    my_view.blit(base_image,(base_move_x,450))
    my_view.blit(base_image,(base_move_x +288,450))
##It is for setting the size of a background
#As our assets size is 288*512 therefore
#We are also choosing this screen size for game
my_view= pygame.display.set_mode((288,512))

##fps object is for setting a cap of fps
fps = pygame.time.Clock()

##declaring variable for gravity apply on birds
gravity=0.25
bird_movement=0

##Adding some assets
bg_image = pygame.image.load('assets/background-day.png').convert()
base_image = pygame.image.load('assets/base.png').convert()           
base_move_x = 0
##Adding birds assets and making rectangle for bird for collision
bird_body=pygame.image.load('assets/redbird-midflap.png').convert()
rect_for_bird=bird_body.get_rect(center=(50,256))
##It is a loop for getting gamescreen till game is on
while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()
    my_view.blit(bg_image,(0,0))#From this image for background that we loaded will adjust in our game screen        
    my_view.blit(bird_body,rect_for_bird)#From this image for bird and its rectengular collision that we loaded will adjust in our game screen
    
    bird_movement+=gravity#Adding gravity on each time when bird move
    rect_for_bird.centery+=bird_movement
    
    base_move_x-=1#For geting a moving base animation
    move_base()
    if base_move_x <=-288:
        base_move_x = 0
    pygame.display.update()        
    fps.tick(120)
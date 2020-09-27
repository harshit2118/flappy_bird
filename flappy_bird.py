import pygame ,sys ,random
pygame.init()

##It is a function for adding the base image after its end
def move_base():
    my_view.blit(base_image,(base_move_x,450))
    my_view.blit(base_image,(base_move_x +288,450))

##It is a function for creating a pipe
def create_pipe():
    pipe_height=random.choice(height_of_pipe)
    get_pipe=pipe_body.get_rect(midtop=(344,pipe_height)) 
    return get_pipe   

##It is a function for moving the pipe from right to left
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx-=2.5
    return pipes        

def draw_pipes(pipes):
    for pipe in pipes:
        my_view.blit(pipe_body,pipe)
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

##Adding pipe in games
pipe_body=pygame.image.load('assets/pipe-green.png').convert()
list_of_pipe=[]
height_of_pipe=[240,300,360,400,380]
new_pipe=pygame.USEREVENT
pygame.time.set_timer(new_pipe,1200)

##It is a loop for getting gamescreen till game is on
try:
    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_SPACE:
                     bird_movement = 0
                     bird_movement -=6
            if event.type is new_pipe:
                list_of_pipe.append(create_pipe())
                          
        my_view.blit(bg_image,(0,0))#From this image for background that we loaded will adjust in our game screen        
        my_view.blit(bird_body,rect_for_bird)#From this image for bird and its rectengular collision that we loaded will adjust in our game screen
    
        #Adding gravity on each time when bird move
        bird_movement+=gravity
        rect_for_bird.centery+=bird_movement

        ##Calling function for drawing and moving pipes
        list_of_pipe=move_pipe(list_of_pipe)
        draw_pipes(list_of_pipe)
        
        #For geting a moving base animation
        base_move_x-=1
        move_base()
        if base_move_x <=-288:
            base_move_x = 0
        pygame.display.update()        
        fps.tick(120)
except:
    print("Game Over")        
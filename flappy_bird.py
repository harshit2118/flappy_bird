import pygame ,sys ,random

pygame.mixer.pre_init(frequency=44100,size=16,channels=1,buffer=512)
pygame.init()

##It is a function for adding the base image after its end
def move_base():
    my_view.blit(base_image,(base_move_x,450))
    my_view.blit(base_image,(base_move_x +288,450))

##It is a function for creating a pipe
def create_pipe():
    pipe_height=random.choice(height_of_pipe)
    get_pipe_bottom=pipe_body.get_rect(midtop=(344,pipe_height)) 
    get_pipe_top=pipe_body.get_rect(midbottom=(344,pipe_height-150))
    return (get_pipe_bottom,get_pipe_top)   

##It is a function for moving the pipe from right to left
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx-=2.5
    return pipes        

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            my_view.blit(pipe_body,pipe)
        else:
            flip_pipe=pygame.transform.flip(pipe_body,False,True)
            my_view.blit(flip_pipe,pipe)

##Function for checking collision between birds and pipe
def check_collision(pipes):
    for pipe in pipes:
        if rect_for_bird.colliderect(pipe):
            sound_of_collision.play()
            return False            
    if rect_for_bird.top <= 0 or rect_for_bird.bottom >=450:
        return False
    return True    

##For rotating a bird
def bird_rotate(bird):
    return pygame.transform.rotozoom(bird, -bird_movement*5,1)

##Function for adding rectangle on every animation of bird
def bird_animation():
    new_bird=bird_pos[bird_index]
    rect_for_new_bird=new_bird.get_rect(center=(50,rect_for_bird.centery))
    return new_bird,rect_for_new_bird

##Function for displaying score
def display_score(game_state):
    if game_state is 'game_running':        
        #For displaying only score
        score_body=game_font.render("Score:{}".format(str(int(score))),True,(156,50,220 ))
        rect_for_score=score_body.get_rect(center=(144,50))
        my_view.blit(score_body,rect_for_score)
   
    if game_state is 'game_over':
        #For displaying score
        score_body=game_font.render("Score:{}".format(str(int(score))),True,(156,50,220 ))
        rect_for_score=score_body.get_rect(center=(144,50))
        my_view.blit(score_body,rect_for_score)
        
        #For displaying high score
        high_score_body = game_font.render("High Score:{}".format(str(int(high_score))),True,(156,50,220 ))
        rect_for_high_score = high_score_body.get_rect(center=(144,430))
        my_view.blit(high_score_body,rect_for_high_score)

##Function for comparing score and and high score 
def update_score(score,high_score):
    if score>high_score:
        high_score=score
    return high_score    

##It is for setting the size of a background
#As our assets size is 288*512 therefore
#We are also choosing this screen size for game
my_view= pygame.display.set_mode((288,512))

##fps object is for setting a cap of fps
fps = pygame.time.Clock()

##declaring variable for gravity apply on birds
gravity=0.25     
bird_movement=0

##declearing font for text
game_font = pygame.font.Font('04B_19.TTF',40)
##Adding some assets
bg_image = pygame.image.load('assets/background-day.png').convert()
base_image = pygame.image.load('assets/base.png').convert()           
base_move_x = 0

##declearing birds assets and making rectangle for bird for collision
bird_down_flap=pygame.image.load('assets/redbird-downflap.png').convert_alpha()
bird_mid_flap=pygame.image.load('assets/redbird-midflap.png').convert_alpha()
bird_up_flap=pygame.image.load('assets/redbird-upflap.png').convert_alpha()
bird_pos=[bird_down_flap,bird_mid_flap,bird_up_flap]
bird_index=0
bird_body=bird_pos[bird_index]
rect_for_bird=bird_body.get_rect(center=(50,256))

bird_flap=pygame.USEREVENT + 1
pygame.time.set_timer(bird_flap,200)

##Adding pipe in games
pipe_body=pygame.image.load('assets/pipe-green.png').convert()
list_of_pipe=[]
height_of_pipe=[240,300,360,400,380]
new_pipe=pygame.USEREVENT
pygame.time.set_timer(new_pipe,1200)
game_on=True

##declearing score and high score
score=0
high_score=0

##Adding game_over screen
game_over_body=pygame.image.load('assets/gameover.png').convert_alpha()
game_over_rect=game_over_body.get_rect(center=(144,256))

##Adding sound effect
sound_of_flap=pygame.mixer.Sound('sound/sfx_wing.wav')
sound_of_collision=pygame.mixer.Sound('sound/sfx_hit.wav')
sound_of_score=pygame.mixer.Sound('sound/sfx_point.wav')
sound_of_score_time=100
##It is a loop for getting gamescreen till game is on
try:
    while True:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                        pygame.quit()
                        sys.exit()    
                if event.type is pygame.KEYDOWN:
                    if event.key is pygame.K_SPACE and game_on:
                         bird_movement = 0
                         bird_movement -=6
                         sound_of_flap.play()
                    ##For restarting the game from SPACE BAR                 
                    if event.key is pygame.K_SPACE and game_on is False:
                         game_on=True
                         list_of_pipe.clear()
                         rect_for_bird.center =(50,256)
                         bird_movement=0   
                         score=0       
                
                if event.type is new_pipe:
                    list_of_pipe.extend(create_pipe())

                ## For flapping bird at different flaps    
                if event.type is bird_flap:
                    if bird_index<2:
                        bird_index+=1
                    else:
                        bird_index=0   
                bird_body,rect_for_bird=bird_animation()         
           
            #From this image for background that we loaded will adjust in our game screen
            my_view.blit(bg_image,(0,0))        
           
            ##Checking the condition if game is still on
            if game_on:
                #Adding gravity on each time when bird move
                bird_movement+=gravity
                rotated_bird=bird_rotate(bird_body)
                rect_for_bird.centery+=bird_movement
                
                my_view.blit(rotated_bird,rect_for_bird)#From this image for bird and its rectengular collision that we loaded will adjust in our game screen
    
                #Calling function for checking collision
                game_on=check_collision(list_of_pipe)
            
                #Calling function for drawing and moving pipes
                list_of_pipe=move_pipe(list_of_pipe)
                draw_pipes(list_of_pipe)

                #Calling function for getting score
                score+=.01
                sound_of_score_time-=1
                if sound_of_score_time <=0:
                    sound_of_score.play()
                    sound_of_score_time=100
                display_score('game_running')
            else:
                my_view.blit(game_over_body,game_over_rect)
                high_score=update_score(score,high_score)
                display_score('game_over')    
        
            #For geting a moving base animation
            base_move_x-=1
            move_base()
            if base_move_x <=-288:
                base_move_x = 0
            pygame.display.update()        
            fps.tick(120)
except:
    print("Game Over")        
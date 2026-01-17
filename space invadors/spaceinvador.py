import  pygame
import os
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('FIRST GAME')
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(240, 231, 62)
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 2
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 60

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
YELLOW_SPACESHIP_IMAGE=pygame.image.load(r'C:\Users\olive\OneDrive\Desktop\game dev 2.0\space invadors\assets\yellow spaceship.png')

YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACECHIP_IMAGE=pygame.image.load(r'C:\Users\olive\OneDrive\Desktop\game dev 2.0\space invadors\assets\red spaceship.png')
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACECHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT )),270)
SPACE=pygame.transform.scale(pygame.image.load(r'C:\Users\olive\OneDrive\Desktop\game dev 2.0\space invadors\assets\space.png'),(WIDTH,HEIGHT))
def yellow_handle_movement(keys_presed,yellow):
    if keys_presed[pygame.K_a]:
        yellow.x= yellow.x-VEL
    if keys_presed[pygame.K_d]:
        yellow.x=yellow.==x+VEL
        

def game(): 
    red_rect=pygame.Rect(700,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow_rect=pygame.Rect(100,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    run=True
    while run:
        WIN.blit(SPACE,(0,0))
        WIN.blit(RED_SPACESHIP,(red_rect.x,red_rect.y))
        WIN.blit(YELLOW_SPACESHIP,(yellow_rect.x,yellow_rect.y))
        pygame.draw.rect(WIN,WHITE,BORDER)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

        keys_presed =pygame.key.get_pressed()
        yellow_handle_movement(keys_presed,yellow_rect)
game()import  pygame
import os
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('FIRST GAME')
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(240, 231, 62)
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 2
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 60

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
YELLOW_SPACESHIP_IMAGE=pygame.image.load(r'C:\Users\olive\OneDrive\Desktop\game dev 2.0\space invadors\assets\yellow spaceship.png')

YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACECHIP_IMAGE=pygame.image.load(r'C:\Users\olive\OneDrive\Desktop\game dev 2.0\space invadors\assets\red spaceship.png')
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACECHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT )),270)
SPACE=pygame.transform.scale(pygame.image.load(r'C:\Users\olive\OneDrive\Desktop\game dev 2.0\space invadors\assets\space.png'),(WIDTH,HEIGHT))
def yellow_handle_movement(keys_presed,yellow):
    if keys_presed[pygame.K_a]:
        yellow.x= yellow.x-VEL
    if keys_presed[pygame.K_d]:
        yellow.x=yellow.==x+VEL
        

def game(): 
    red_rect=pygame.Rect(700,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow_rect=pygame.Rect(100,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    run=True
    while run:
        WIN.blit(SPACE,(0,0))
        WIN.blit(RED_SPACESHIP,(red_rect.x,red_rect.y))
        WIN.blit(YELLOW_SPACESHIP,(yellow_rect.x,yellow_rect.y))
        pygame.draw.rect(WIN,WHITE,BORDER)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

        keys_presed =pygame.key.get_pressed()
        yellow_handle_movement(keys_presed,yellow_rect)
game()

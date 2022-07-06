            # IMPORTS
import pygame
import random
import sys
            ## IMPORTS

            # GAME SCREEN SIZE
pygame.init()
screen_w=1920  #1366
screen_h=1080  #768
            ## GAME SCREEN SIZE
            
            # COLORS
black=(0, 0 ,0)
white=(222, 222, 222)
red=(180, 0, 0)
blue=(0, 60, 255)
            ## COLORS
            
            # SET WINDOW TO FULLSCREEN, SET TITLE AND CLOCK VARIABLE
screen=pygame.display.set_mode([screen_w,screen_h],pygame.FULLSCREEN)
pygame.display.set_caption('Flight Fighter')
clock=pygame.time.Clock()
            ## SET WINDOW TO FULLSCREEN, SET TITLE AND CLOCK VARIABLE
            
            # SET FONT SIZE
arial_25 = pygame.font.SysFont('arial',28)
            ## SET FONT SIZE
            
            # SET ENEMY/SNOW EVENT TIMERS
ENEMYSPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMYSPAWN, 550)
            ## SET ENEMY/SNOW EVENT TIMERS
SNOWSPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(SNOWSPAWN, 500)
            
            # INNERGAME BACKGROUND VARIABLES
bg1 = pygame.image.load('./images/bg1.png').convert_alpha()
bg1 = pygame.transform.scale(bg1,(screen_w,screen_h))
bg2 = pygame.image.load('./images/bg2.png').convert_alpha()
bg2 = pygame.transform.scale(bg2,(screen_w,screen_h))
            ## INNERGAME BACKGROUND VARIABLES
            
            # LOCATION VARIABLES
b1x = b1y = 0
b2x , b2y = 0,-screen_h
            ## LOCATION VARIABLES
            
            # SPLASH SCREEN VARIABLES
op1 = pygame.image.load('./images/intro.png').convert_alpha()
op2 = pygame.image.load('./images/me.png').convert_alpha()
op3 = pygame.image.load('./images/fighters.png').convert_alpha()
            ## SPLASH SCREEN VARIABLES
            
            # SOUND VARIABLES
start_sound = pygame.mixer.Sound('./audio/Black Ops 2 - Adrenaline.mp3')
start_sound.set_volume(.3)
gameMusic = pygame.mixer.Sound('./audio/Black Ops 2 - Adrenaline.mp3')
gameMusic.set_volume(.3)
gameeasy = pygame.mixer.Sound('./audio/Fallguys - Everybody Falls.mp3')
gameeasy.set_volume(.7)
gamehard = pygame.mixer.Sound('./audio/Counter Strike Main Menu.mp3')
gamehard.set_volume(.7)
gameover_music = pygame.mixer.Sound('./audio/Fallguys - Everybody Falls.mp3')
gameover_music.set_volume(.3)
haha = pygame.mixer.Sound('./audio/haha.wav')
haha.set_volume(.5)
expl_sound = pygame.mixer.Sound('./audio/expl.wav')
expl_sound.set_volume(.3)
impact_sound = pygame.mixer.Sound('./audio/thud.wav')
impact_sound.set_volume(.4)
powerup = pygame.mixer.Sound('./audio/powerup.wav')
gunshot = pygame.mixer.Sound('./audio/gunshot.wav')
gunshot.set_volume(.4)
bomb = pygame.mixer.Sound('./audio/bomb.wav')
shotgun = pygame.mixer.Sound('./audio/shotgun.wav')
shotgun.set_volume(.3)
            ## SOUND VARIABLES
            
            # SETS GAME TRACK (TRACKS GO FROM 1-10)
gtrack = pygame.mixer.Channel(5)
            # SETS PRIMARY INNERGAME STARTING MUSIC TO 'SANDSTORM - DARUDE'
gametrack = gameeasy
            
            # DEFAULT SOUND SETTINGS
muted = False
music_change = True
            ## DEFAULT SOUND SETTINGS
            
            # SETS CLOUD VARIABLES
cloud1=pygame.image.load('./images/cloud (1).png').convert_alpha()
cloud2=pygame.image.load('./images/cloud (2).png').convert_alpha()
cloud3=pygame.image.load('./images/cloud (3).png').convert_alpha()
cloud4=pygame.image.load('./images/cloud (4).png').convert_alpha()
            ## SETS CLOUD VARIABLES
            
            # MORE LOCATION VARIABLES
c1x,c1y = 0,-100
c2x,c2y = 200,350
c3x,c3y = 600,100
c4x,c4y = 700,600
            ## MORE LOCATION VARIABLES
            
            # SETS PARTICLES TO SPRITE GROUPS
all_snow = pygame.sprite.Group()

all_sprites=pygame.sprite.Group()

all_blocks=pygame.sprite.Group()

all_bullets=pygame.sprite.Group()

all_ebullets = pygame.sprite.Group()
            ## SETS PARTICLES TO SPRITE GROUPS
            
            # UPGRADE ANIMATION
upgrade_anim = []
for i in range(1,10):
    filename = './images/Picture{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(black)
    img = pygame.transform.scale(img,(135,135))
    upgrade_anim.append(img)

class Upgrade_anim(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = upgrade_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
            ## UPGRADE ANIMATION
            
            # UPGRADE SYNC ?
    def update(self):
        self.rect.center = player.rect.center
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(upgrade_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = upgrade_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            ## UPGRADE SYNC ?
            
            # EXPLOSION ANIMATION SIZES
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['Xlg'] = []
            ## EXPLOSION ANIMATION SIZES
            
            # EXPLOSION ANIM
for i in range(9):
    filename = './images/regularExplosion0{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(black)
    img_Xlg = pygame.transform.scale(img, (210,210))
    explosion_anim['Xlg'].append(img_Xlg)
    img_lg = pygame.transform.scale(img, (95, 95))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
            ## EXPLOSION ANIM
            
            # EXPLOSION SIZE AND LOCATION
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
            ## EXPLOSION SIZE AND LOCATION
            
            # EXPLOSION SYNC ?
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            ## EXPLOSION SYNC ?
            
            # SPRITE BLOCK STUFF 
class Block(pygame.sprite.Sprite):
    def __init__(self,hp,speed):
        super().__init__()
        self.image = pygame.image.load('./images/e_jet.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.radius = (self.rect.centerx - self.rect.x)
        self.hp= hp
        self.speed = speed
        self.birth = pygame.time.get_ticks()
        self.shoot = 1400

            # SPRITE BLOCKS SYNC
    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.top>screen_h:
            self.kill()
        if pygame.time.get_ticks() - self.birth > self.shoot:
            if not muted: shotgun.play()
            ebullet = Bullet(1,15,'ejet')
            ebullet.rect.centerx=self.rect.centerx
            ebullet.rect.centery=self.rect.centery
            all_ebullets.add(ebullet)
            all_sprites.add(ebullet)
            self.birth = pygame.time.get_ticks()

            # CLASS FOR SNOW IN MENU
class Snow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/snow.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speedy = random.randrange(1,5)
        self.speedx = random.randrange(-2,2)
        
            # SNOW SPRITE SYNC
    def update(self):
        self.rect.centery += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.right>screen_w or self.rect.left<0 or self.rect.bottom>screen_h:
            self.kill()
      
            # PLAYER SPRITE CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self,hp):
        super().__init__()
        self.image = pygame.image.load('./images/jet.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.radius = (self.rect.centerx - self.rect.x)
        self.hp = hp
        self.speed = 8
        self.shoot_delay = 95
        self.last_shot = pygame.time.get_ticks()
        self.machinegun = False
        
            # PLAYER SPRITE SYNC
    def update(self):
        key = pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        
        self.rect.centerx=mouse_pos[0]
        self.rect.centery=mouse_pos[1]

            # MACHINE GUN LMAO
        if self.machinegun:
            if key[0] == 1:
                if pygame.time.get_ticks() - self.last_shot > self.shoot_delay:
                    if not muted:
                        gunshot.play()
                    self.last_shot = pygame.time.get_ticks()
                    bullet=Bullet(-1,50,'jet')
                    bullet.rect.centerx=player.rect.centerx
                    bullet.rect.centery=player.rect.centery
                    all_sprites.add(bullet)
                    all_bullets.add(bullet)     

            # BULLET SPRITE CLASS
class Bullet(pygame.sprite.Sprite):
    def __init__(self,direction,speed,btype):
        super().__init__()
        self.type = btype
        if self.type == 'jet':
            if player.machinegun:
                self.image = pygame.image.load('./images/bullet2.png').convert_alpha()
            else:
                self.image=pygame.image.load('./images/bullet.png').convert_alpha()
        if self.type == 'ejet':
            self.image = pygame.image.load('./images/ebullet.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.direction = direction
        self.speed = speed
        
            # BULLET SPRITE SYNC
    def update(self):
        self.rect.y+=(self.direction)*self.speed
        if self.rect.bottom<0:
            self.kill()
        if self.rect.top>screen_h:
            self.kill()

            # CLASS FOR IMAGES
class Image(pygame.sprite.Sprite):
    def __init__(self,image,center):
        super().__init__()
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = center

player=Player(6)
all_sprites.add(player)
score = 0
blockspeed1 = 3
blockspeed2 = 6
barHP = 3
upgrade = 0
increment = 10

            # CLASS FOR BUTTON FUNCTIONALITY
def button(msg,x,y,w,h,ap,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x-ap,y-ap,w+2*ap,h+2*ap))
        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    txt = arial_25.render(msg,True,white)
    txt_rect = txt.get_rect()
    txt_rect.center = ((x+w/2),(y+h/2))
    screen.blit(txt,txt_rect)

            # MUTE/UNMUTE FUNCTION
def mute():
    global muted
    pygame.mixer.pause() # pause
    muted = True
def unmute():
    global muted
    pygame.mixer.unpause() # unpause
    muted = False

            # SPLASH SCREEN FUNCTION
def op():
    start = pygame.time.get_ticks()
    cinematic = True
    if not muted: start_sound.play(-1)
    while cinematic:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if pygame.time.get_ticks()-start<6500:
            screen.blit(op1,(0,0))
        elif 6500<pygame.time.get_ticks()-start<10000:
            screen.blit(op2,(0,0))
        else:
            screen.blit(op3,(0,0))
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                break
        pygame.display.update()
        clock.tick(60)
    if not muted: start_sound.fadeout(1000)
    gameMusic.play(-1)

            # PAUSE FUNCTION
def pause():
    if not muted: 
        pygame.mixer.fadeout(500)
        gameMusic.play()
    paused = True
    pygame.mouse.set_visible(1)
    pauseimg = pygame.image.load('./images/pauseimg.png').convert_alpha()
    pauseimg = pygame.transform.scale(pauseimg,(screen_w,screen_h))
    pause_snow = pygame.sprite.Group()
    paused = pygame.image.load('./images/paused.png')
    paused = Image(paused,(screen_w/2-300,110))
    pause_images = pygame.sprite.Group()
    pause_images.add(paused)
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == SNOWSPAWN:
                snow = Snow()
                snow.rect.centery = random.randint(0,10)
                snow.rect.centerx = random.randint(screen_w/2+300,screen_w-5)
                pause_snow.add(snow)

        screen.blit(pauseimg,(0,0))

        pause_snow.draw(screen)
        pause_snow.update()
            # PAUSE BUTTONS
        button('Resume',21,600,300,40,3,(180, 175, 180, 70),(0, 0, 0),innergame)
        button('Menu',21,650,300,40,3,(180, 175, 180, 70),(0, 0, 0),menu)
        button('Quit',21,710,300,40,3,(180, 175, 180, 70),(0, 0, 0),quitgame)
              
        pause_images.draw(screen)


        pygame.display.update()
        clock.tick(60)

            # MAIN MENUUUU
def menu():

    player.kill()

    intro = True
    menu_snow = pygame.sprite.Group()
    menuimg = pygame.image.load('./images/menu.jpg').convert()

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == SNOWSPAWN:
                snow = Snow()
                snow.rect.centery = random.randint(0,10)
                snow.rect.centerx = random.randint(screen_w/2+300,screen_w-5)
                menu_snow.add(snow)

        screen.blit(menuimg,(0,0))

        menu_snow.draw(screen)
        menu_snow.update()
                
                # BUTTONS FOR MAIN MENU
        button('Play',21,490,300,40,3,(180, 175, 180, 70),(0, 0, 0),game)
        button('Credits',21,550,300,40,3,(180, 175, 180, 70),(0, 0, 0),credit)
        button('Mute',21,600,300,40,3,(180, 175, 180, 70),(0, 0, 0),mute)
        button('Unmute',21,650,300,40,3,(180, 175, 180, 70),(0, 0, 0),unmute)
        button('Quit',21,710,300,40,3,(180, 175, 180, 70),(0, 0, 0),quitgame)

        pygame.display.update()
        clock.tick(60)
    if not muted: gameMusic.fadeout(500)

                # CREDITS MENU
def credit():
    credits1=True

    menu2 = pygame.image.load('./images/menu2.jpg').convert_alpha()
    credit_snow = pygame.sprite.Group()

    creditimg = pygame.image.load('./images/credits.png')
    creditimg = Image(creditimg,(screen_w/2,400))

    credit_images = pygame.sprite.Group()
    credit_images.add(creditimg)
    
    while credits1:
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == SNOWSPAWN:
                snow = Snow()
                snow.rect.centery = random.randint(0,10)
                snow.rect.centerx = random.randint(screen_w/2+300,screen_w-5)
                credit_snow.add(snow)

        screen.blit(menu2,(0,0))

        credit_snow.draw(screen)
        credit_snow.update()

        credit_images.draw(screen)
            # BACK BUTTON
        button('Back',21,800,300,40,3,(180, 175, 180, 70),(0, 0, 0),menu)

        pygame.display.update()
        clock.tick(60)

            # QUIT FUNCTION
def quitgame():
    pygame.quit()
    sys.exit()

            # END GAME FUNCTION
def gameover():

    global score,muted

    if not muted:
        pygame.mixer.fadeout(500)
        gameover_music.play() # -1

    EMBERSPAWN = pygame.USEREVENT + 3
    pygame.time.set_timer(EMBERSPAWN,100)

    gameoverimg = pygame.image.load('./images/died.png')
    gameoverimg = Image(gameoverimg,(screen_w/2,100))
    over_images = pygame.sprite.Group()
    over_images.add(gameoverimg)
    
    skull = pygame.image.load('./images/skull.jpg').convert_alpha()
    skull = pygame.transform.scale(skull,(1920,1080))  # SKULL SCALE
    all_embers = pygame.sprite.Group()
    over = True
    while over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == EMBERSPAWN:
                ember = Snow()
                ember.image = pygame.image.load('./images/ember.png').convert_alpha()
                ember.rect.centery = random.randint(-5,10)
                ember.rect.centerx = random.randint(screen_w/2+300,screen_w-5)
                
                all_embers.add(ember)

        screen.blit(skull,(0,0))

        all_embers.draw(screen)
        all_embers.update()

        over_images.draw(screen)
            # GAME OVER BUTTONS
        button('Try Again',21,600,300,40,3,(180, 175, 180, 70),(0, 0, 0),game)
        button('Menu',21,650,300,40,3,(180, 175, 180, 70),(0, 0, 0),menu)
        button('Quit',21,710,300,40,3,(180, 175, 180, 70),(0, 0, 0),quitgame)

            # SCORE AFTER
        s_font = pygame.font.SysFont('arial',35)
        s = s_font.render("score :  "+str(score),True,(140,140,140))
        s_rect = s.get_rect()
        s_rect.center = (screen_w/2,150)
        screen.blit(s,s_rect)

        pygame.display.update()
        clock.tick(60)

            # MAIN GAME
def game():

    global player,blockspeed1,blockspeed2,barHP,upgrade,score,increment,increment,gametrack,music_change,muted
    
    all_blocks.empty()

    all_bullets.empty()

    all_ebullets.empty()

    all_sprites.empty()

    player=Player(6)
    all_sprites.add(player)
    blockspeed1 = 3
    blockspeed2 = 6
    barHP = 3
    upgrade = 0
    score = 0
    increment = 10
    gametrack = gameeasy
    pygame.time.set_timer(ENEMYSPAWN, 600)
    music_change = True
    
    innergame()

            # INNER GAME YEWW
def innergame():

    global player,blockspeed1,blockspeed2,barHP,upgrade,score,increment,b1x,b1y,b2x,b2y,c1x,c2x,c3x,c4x,c1y,c2y,c3y,c4y ,gametrack,music_change,muted

    pygame.mouse.set_visible(0)
    
    hp_color = blue
    crash=False
    kill = False
    up = False
    up_flashbool = False
    expl_large = False
    machinegun = False
    smg_not = False
    g_start = True

    smg = pygame.image.load('./images/machinegun.png')
    smg = Image(smg,(screen_w/2,400))
    upgraded = pygame.image.load('./images/upgraded.png')
    upgraded = Image(upgraded,(screen_w/2,200))
    upg_images = pygame.sprite.Group()
    upg_images.add(upgraded)

    if not muted:
        pygame.mixer.fadeout(500)
        gtrack.play(gametrack)
      

    while not crash:

        if not gtrack.get_busy():
            gtrack.play(gametrack)
            # UPGRADE FUNCTIONALITY AND INCREMENTATION 
        if score==increment:
            if not muted: powerup.play()
            blockspeed1 +=1
            blockspeed2 +=1
            up = True
            timer = pygame.time.get_ticks()
            upgrade +=1
            if player.hp <= 10:
                player.hp += 2
            up_flash = Upgrade_anim(player.rect.center)
            all_sprites.add(up_flash)
            if upgrade == 1: # AT 10 POINTS
                player.image = pygame.image.load('./images/jet2.png').convert_alpha()
                player.rect = player.image.get_rect()
                player.radius = (player.rect.centerx - player.rect.x)
            if upgrade == 2: # AT 20 POINTS
                player.image = pygame.image.load('./images/jet3.png').convert_alpha()
                player.rect = player.image.get_rect()
                player.radius = (player.rect.centerx - player.rect.x)
            if upgrade == 3: # AT 30 POINTS
                player.image = pygame.image.load('./images/jet4.png').convert_alpha()
                player.rect = player.image.get_rect()
                player.radius = (player.rect.centerx - player.rect.x)
            if upgrade == 4: # AT 40 POINTS
                player.machinegun = True
                smg_not = True
                player.image = pygame.image.load('./images/jet5.png').convert_alpha()
                player.rect = player.image.get_rect()
                player.radius = (player.rect.centerx - player.rect.x)
            if upgrade == 5: # AT 50 POINTS
                player.machinegun = True
                player.image = pygame.image.load('./images/jet6.png').convert_alpha()
                player.rect = player.image.get_rect()
                player.radius = (player.rect.centerx - player.rect.x)
            if upgrade == 6: # AT 60 POINTS
                player.machinegun = True
                player.image = pygame.image.load('./images/jet7.png').convert_alpha()
                player.rect = player.image.get_rect()
                player.radius = (player.rect.centerx - player.rect.x)
            increment = score+10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash=True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause()
            if event.type == ENEMYSPAWN:
                block = Block(3,random.randint(blockspeed1,blockspeed2))
                
                if 40 > score >= 10:
                    block.image = pygame.image.load('./images/e_jet2.png').convert_alpha()
                    block.rect = block.image.get_rect()
                    block.radius = (block.rect.centerx - block.rect.x)
                    block.hp = 5
                
                if 80 > score >= 40:
                    expl_large = True
                    block.image = pygame.image.load('./images/e_jet3.png').convert_alpha()
                    block.rect = block.image.get_rect()
                    block.radius = (block.rect.centerx - block.rect.x)-55
                    block.hp = 10    
                    block.speed = random.randint(3,6)
                    pygame.time.set_timer(ENEMYSPAWN,1500)
                    block.shoot = 800
                
                if score >= 80:
                    if music_change:
                        pygame.mixer.fadeout(1000)
                        if not muted:
                            haha.play()
                            gametrack = gamehard
                            gtrack.play(gametrack)
                        music_change = False
                    expl_large = True
                    block.image = pygame.image.load('./images/e_jet4.png').convert_alpha()
                    block.rect = block.image.get_rect()
                    block.radius = (block.rect.centerx - block.rect.x)-55
                    block.hp = 10    
                    block.speed = random.randint(3,6)
                    pygame.time.set_timer(ENEMYSPAWN,1500)
                    block.shoot = 710

                block.rect.centerx = random.randrange(screen_w)
                block.rect.centery = random.randint(-140,-90)
                all_blocks.add(block)
                all_sprites.add(block)
                
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and not player.machinegun:
                if not muted: gunshot.play()
                bullet=Bullet(-1,50,'jet')
                bullet.rect.centerx=player.rect.centerx
                bullet.rect.centery=player.rect.centery
                all_sprites.add(bullet)
                all_bullets.add(bullet)

        all_sprites.update()
        
        # BULLET CONTACT HANDLING 
        for bullet in all_bullets:
            block_hit_list=pygame.sprite.spritecollide(bullet,all_blocks,False,pygame.sprite.collide_circle)
            for block in block_hit_list:
                if not muted: impact_sound.play()
                expl = Explosion(bullet.rect.center,'sm')
                all_sprites.add(expl)
                block.hp -= 1
                bullet.kill()
                if block.hp<=0:
                    pygame.sprite.spritecollide(bullet, all_blocks, True)
                    if not muted: expl_sound.play()
                    if expl_large:
                        expl = Explosion(block.rect.center,'Xlg')
                    else:
                        expl = Explosion(block.rect.center,'lg')
                    all_sprites.add(expl)
                    bullet.kill()
                    if expl_large: score +=2
                    else: score+=1

        for ebullet in all_ebullets:
            ebullet_hit_list = pygame.sprite.spritecollide(player,all_ebullets,False,pygame.sprite.collide_circle)
            for ebullet in ebullet_hit_list:
                if not muted: impact_sound.play()
                expl = Explosion(player.rect.center,'sm')
                all_sprites.add(expl)
                player.hp -= 1
                ebullet.kill()
                if player.hp <= 0:
                    if not muted: bomb.play()
                    interval = 200
                    expl = Explosion(player.rect.center,'lg')
                    all_sprites.add(expl)
                    timi = pygame.time.get_ticks()
                    kill = True

        for bullet in all_bullets:
            bullet_ebullet_hits = pygame.sprite.spritecollide(bullet,all_ebullets,True)
            for bullet in bullet_ebullet_hits:
                expl = Explosion(bullet.rect.center,'sm')
                all_sprites.add(expl)
                bullet.kill()

        for blocks in all_blocks:
            jet_block_hit = pygame.sprite.spritecollide(player,all_blocks,True,pygame.sprite.collide_circle)
            for block in jet_block_hit:
                if not muted: expl_sound.play()
                if expl_large: expl = Explosion(block.rect.center,'Xlg')
                else: expl = Explosion(block.rect.center,'lg')
                all_sprites.add(expl)
                if expl_large:
                    player.hp -= 2
                else:
                    player.hp -= 1
                if player.hp <= 0:
                    if not muted: bomb.play()
                    interval = 200
                    expl = Explosion(player.rect.center,'lg')
                    all_sprites.add(expl)
                    timi = pygame.time.get_ticks()
                    kill = True
                   

            # KILL FUNCTION
        if kill == True:
            
            if pygame.time.get_ticks() - timi > interval:
                expl = Explosion(player.rect.center,'lg')
                all_sprites.add(expl)
                interval += 200
                
            if pygame.time.get_ticks() - timi > 1000:
                kill = False
                player.kill()
                crash = True
                pygame.mouse.set_visible(1)
                gameover()

        screen.blit(bg1,(b1x,b1y))
        screen.blit(bg2,(b2x,b2y))

        b1y += 2
        b2y += 2
        
        if b1y > screen_h : b1y = -screen_h
        if b2y > screen_h : b2y = -screen_h

        screen.blit(cloud1,(c1x,c1y))
        screen.blit(cloud2,(c2x,c2y))
        screen.blit(cloud3,(c3x,c3y))
        screen.blit(cloud4,(c4x,c4y))

        c1x+=1
        c2x+=3
        c3x+=4
        c4x+=2

        if c1x>screen_w+10: c1x = -700     
        if c2x>screen_w+10: c2x = -700
        if c3x>screen_w+10: c3x = -700
        if c4x>screen_w+10: c4x = -700
        
        
        all_snow.draw(screen)        
        all_sprites.draw(screen)


        # HP BAR    
        if g_start:
            if not barHP>=player.hp*67:
                barHP += 7
            else:
                g_start = False
        else:
            if not barHP<=player.hp*67:
                barHP -= 5
            if not barHP>player.hp*67:
                barHP += 5
            if player.hp<=2:
                hp_color = red
            if barHP<=3:
                barHP = 3
        pygame.draw.rect(screen,hp_color,(10,10,barHP,10))
        hp_surf = arial_25.render('Health',True,white)
        screen.blit(hp_surf,(10,25))

        # SCORE INGAME
        s_surf = arial_25.render("Score: "+str(score),True,white)
        screen.blit(s_surf,(10,60))

        if up:
            if smg_not:
                upg_images.add(smg)
            if pygame.time.get_ticks()-timer < 2420:
                hp_color = (191,191,191)
                upg_images.draw(screen)
            else:
                hp_color = blue
                up = False
                smg_not = False
                upg_images.remove(smg)
        
        clock.tick(60)
        pygame.display.update()
    pygame.mouse.set_visible(1)
op()
menu()

pygame.quit()

import math
import pygame as pg

pg.init()

#creating window
WIDTH, HEIGHT = 1000, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("gamer game")


#variables and images
BG1 = pg.image.load("BG1.png")
PLAYER = pg.image.load("player.png")
FPS = 60
playerLocationX, playerLocationY = 500, 0
playerVelocityY, playerVelocityX = 0, 0
grounded = False


def main():
    global playerLocationX
    global playerLocationY
    global playerVelocityY
    global playerVelocityX
    clock = pg.time.Clock()
    run = True
    while run:
        #gets list of keys down
        keys = pg.key.get_pressed()
        
        #updates at rate of FPS
        clock.tick(FPS)
        

        #event listener
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False
            #key press listener
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE and grounded:
                    playerVelocityY = playerVelocityY-7


        #key hold listener
        if keys[pg.K_a]:
            if abs(playerVelocityX)<7: playerVelocityX = playerVelocityX-0.2
        if keys[pg.K_d]:
            if abs(playerVelocityX)<7: playerVelocityX = playerVelocityX+0.2


        #showing images on screen
        WIN.blit(BG1, (0, 0))
        WIN.blit(PLAYER, (playerLocationX, playerLocationY))
        

        #acting on horizontal velocity
        playerLocationX = playerLocationX + playerVelocityX
        #acting on vertical velocity
        playerLocationY = playerLocationY + playerVelocityY
        #gravity
        playerVelocityY = playerVelocityY+0.2


        #simulating air drag/ground friction
        if playerVelocityX<0:
            playerVelocityX = playerVelocityX+0.08
        elif playerVelocityX<0.1 and playerVelocityX>0:
            playerVelocityX=0
        
        if playerVelocityX>0:
            playerVelocityX = playerVelocityX-0.08
        elif playerVelocityX>-0.1 and playerVelocityX<0:
            playerVelocityX=0


        #ground collision
        if playerLocationY>=450:
            grounded=True
            if playerVelocityY>1: playerVelocityY=playerVelocityY-(playerVelocityY*1.2)
            else: playerVelocityY=playerVelocityY-playerVelocityY
        else:
            grounded=False


        #teleports player if goes off screen
        if playerLocationX>1050:
            playerLocationX=-50
        if playerLocationX<-50:
            playerLocationX=1050
    

        print(math.floor(playerLocationX), math.floor(playerLocationY), playerVelocityX, math.floor(playerVelocityY), grounded)
        pg.display.update()     
    
    pg.quit()


if __name__ == "__main__":
    main()




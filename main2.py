# 1) Import required modules:
#    a) Import `math` to calculate distance for collision detection.
#    b) Import `random` to generate random enemy positions.
#    c) Import `pygame` to create the game window, load images, and handle events.
import pygame
import math
import random
# 2) Create constants to control game settings:
#    a) Screen size, player start position, enemy start range.
#    b) Enemy movement speed (X and Y), bullet speed, collision distance threshold.
screenwidth = 800
screenheight = 500
playerstartx = 370
playerstarty = 380
enemystartymin = 50
enemystartymax = 150
enemyspeedx = 4
enemyspeedy = 40
bulletspeedy = 10
collisiondistance = 27
# 3) Initialize pygame using `pygame.init()`.
pygame.init()
# 4) Create the game window (screen) using `pygame.display.set_mode(...)`
screen = pygame.display.set_mode((screenwidth,screenheight))
# 5) Load background image using `pygame.image.load('background.png')`.
background = pygame.image.load("background.png")
# 6) Set the game title and icon:
#    a) Use `pygame.display.set_caption("Space Invader")`.
#    b) Load icon image `ufo.png` and apply using `pygame.display.set_icon(icon)`.
pygame.display.set_caption("space invader")
item = pygame.image.load("ufo.png")
pygame.display.set_icon(item)
# 7) Setup the player:
#    a) Load the player image `player.png`.
#    b) Set initial player position using `playerX` and `playerY`.
#    c) Create `playerX_change = 0` to control horizontal movement.
playerimage = pygame.image.load("player.png")
playerx = playerstartx
playery = playerstarty
playerxchange = 0

# 8) Setup enemies using lists (multiple enemies):
#    a) Create empty lists for enemy image, x/y positions, and x/y movement changes.
#    b) Set `num_of_enemies = 6`.
enemiesimage = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numberofenemies = 6
# 9) Use a loop to create each enemy:
#    a) Load enemy image `enemy.png` and append it to `enemyImg`.
#    b) Set random starting X position within the screen width.
#    c) Set random starting Y position between ENEMY_START_Y_MIN and ENEMY_START_Y_MAX.
#    d) Set initial X speed (ENEMY_SPEED_X) and Y drop speed (ENEMY_SPEED_Y).
for i in range(6):
    enemiesimage.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,screenwidth-64))
    enemyy.append(random.randint(enemystartymin,enemystartymax))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)
# 10) Setup bullet:
#     a) Load bullet image `bullet.png`.
#     b) Set bullet starting positions and movement speed.
#     c) Use `bullet_state = "ready"` to track if bullet can be fired or is already moving.
bulletimage = pygame.image.load("bullet.png")
bulletx = 0
bullety = playerstarty
bulletxchange = 0
bulletychange = bulletspeedy
bulletstate = "ready"
# 11) Setup score display:
#     a) Initialize `score_value = 0`.
#     b) Load a font using `pygame.font.Font(...)`.
#     c) Set score text position (textX, textY).
scorevalue = 0
font = pygame.font.SysFont("Times New Roman",32)
textx = 10
texty = 10
# 12) Setup game-over text font using a larger font size.
overfont = pygame.font.SysFont("Times New Roman",64)
# 13) Define helper functions:
#     a) `show_score(x, y)` to render and display the score on the screen.
#     b) `game_over_text()` to display "GAME OVER" on the screen.
#     c) `player(x, y)` to draw the player image at (x, y).
#     d) `enemy(x, y, i)` to draw the i-th enemy at (x, y).
#     e) `fire_bullet(x, y)`:
#        - Set `bullet_state` to "fire"
#        - Draw the bullet slightly offset from the player position.
#     f) `isCollision(enemyX, enemyY, bulletX, bulletY)`:
#        - Calculate distance between enemy and bullet using the distance formula.
#        - Return True if distance is less than COLLISION_DISTANCE.
def show_score(x,y):
    score = font.render(f"score: {scorevalue}",True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext():
    overtext = font.render(f"game over!",True,(255,255,255))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(playerimage,(x,y))
def enemy(x,y,i):
    screen.blit(enemiesimage[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimage,(x+16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance < collisiondistance
# 14) Start the main game loop with `running = True`.
runing = True
while runing:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
# 15) Every frame inside the loop:
#     a) Clear the screen and draw the background image.

# 16) Handle events (keyboard and quit):
#     a) If `pygame.QUIT`, stop the loop.
#     b) If a key is pressed (`pygame.KEYDOWN`):
#        - LEFT arrow sets `playerX_change = -5`.
#        - RIGHT arrow sets `playerX_change = 5`.
#        - SPACE fires the bullet only if `bullet_state` is "ready":
#          i) Set `bulletX = playerX`
#          ii) Call `fire_bullet(bulletX, bulletY)`
#     c) If key is released (`pygame.KEYUP`) for LEFT/RIGHT:
#        - Set `playerX_change = 0` to stop movement.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

# 17) Update player movement:
#     a) Add `playerX_change` to `playerX`.
#     b) Clamp player position so it stays inside the screen boundaries.

# 18) Update enemy movement for each enemy:
#     a) If any enemy goes below Y > 340:
#        - Move all enemies off-screen (enemyY = 2000)
#        - Display "GAME OVER"
#        - Break out of enemy loop.
#     b) Move enemy horizontally using `enemyX_change[i]`.
#     c) If enemy hits left/right edge:
#        - Reverse direction by multiplying speed by -1.
#        - Move enemy downward by adding `enemyY_change[i]`.
#     d) Check collision between the enemy and bullet:
#        - If collision occurs:
#          i) Reset bullet position and set bullet_state back to "ready".
#          ii) Increase score by 1.
#          iii) Respawn enemy at a new random position.
#     e) Draw the enemy on the screen.

# 19) Update bullet movement:
#     a) If bullet goes off the top of the screen (`bulletY <= 0`):
#        - Reset bulletY and set `bullet_state = "ready"`.
#     b) If bullet_state is "fire":
#        - Draw the bullet.
#        - Move the bullet upward by decreasing `bulletY`.

# 20) Draw the player, show the score, and update the display:
#     a) Draw player at (playerX, playerY).
#     b) Display score using `show_score(textX, textY)`.
#     c) Refresh the screen using `pygame.display.update()`.
    pygame.display.update()
import pygame 
import random
pygame.init()
spritecolorchangeevent = pygame.USEREVENT+1
backgroundcolorchangeevent = pygame.USEREVENT+2
blue = pygame.Color("blue")
cyan = pygame.Color("cyan")
pink = pygame.Color("pink")
purple = pygame.Color("purple")
yellow = pygame.Color("yellow")
green = pygame.Color("green")
red = pygame.Color("red")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]    
    def update(self):
        self.rect.move_ip(self.velocity)
        boundaryhit = False 
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundaryhit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundaryhit = True
        if boundaryhit:
            pygame.event.post(pygame.event.Event(spritecolorchangeevent))
            pygame.event.post(pygame.event.Event(backgroundcolorchangeevent))
    def changecolor(self):
        self.image.fill(random.choice([red,blue,cyan,pink]))
def changebackgroundcolor():
    global backgroundcolor
    backgroundcolor = random.choice([green,yellow,purple])
allspritelist = pygame.sprite.Group()
screen = pygame.display.set_mode((500,400))
sprite1 = Sprite(pink,20,30)
sprite1.rect.x = random.randint(0,480)
sprite1.rect.y = random.randint(0,370)
allspritelist.add(sprite1)
sprite2 = Sprite(pink,20,30)
sprite2.rect.x = random.randint(0,480)
sprite2.rect.y = random.randint(0,370)
allspritelist.add(sprite2)
pygame.display.set_caption("boundary sprite")
backgroundcolor = red
screen.fill(backgroundcolor)
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == spritecolorchangeevent:
            sprite1.changecolor()
            sprite2.changecolor()
        elif event.type == backgroundcolorchangeevent:
            changebackgroundcolor()
    allspritelist.update()
    screen.fill(backgroundcolor)
    allspritelist.draw(screen)
    pygame.display.flip()        
pygame.quit()
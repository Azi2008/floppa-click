from pygame import *
import time


window = display.set_mode((700,500))
display.set_caption('mega flopper')

class Player(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = transform.scale(image.load("floppa.png"), (200, 200))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    



player = Player(150,200)

win_width = 700
win_height = 500
game = True
score = 0
point = 1
background = transform.scale(image.load('white.jpg'),(700,500)) 

font.init()
f1 = font.Font(None, 36)
cost1 = 10
cost2 = 100
cost3 = 1000
cost4 = 10000



def shop1():
    global point
    global cost1
    global score
    keys = key.get_pressed()
    if keys[K_1] and cost1 <= score:
        score -= cost1
        time.sleep(0.1)
        point +=1
        cost1 +=1 
def shop2():
    global point
    global cost2
    global score
    keys = key.get_pressed()
    if keys[K_2] and cost2 <= score:
        score -= cost2
        time.sleep(0.1)
        point +=5
        cost2 +=10

def shop3():
    global point
    global cost3
    global score
    keys = key.get_pressed()
    if keys[K_3] and cost3 <= score:
        score -= cost3
        time.sleep(0.1)
        point +=20
        cost3 +=50

def shop4():
    global point
    global cost4
    global score
    keys = key.get_pressed()
    if keys[K_3] and cost4 <= score:
        score -= cost4
        time.sleep(0.1)
        point +=100
        cost4 + 500


mouse = mouse.get_pos()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
              if 0 <= mouse[0] <=  700 and 0 <= mouse[1] <= 700:
                  score += point
                  player.image = transform.rotate(player.image,90)
                  print(score)
    window.blit(background,(0,0))
    window.blit(player.image,(150,200))
    text = f1.render("Счёт: " + str(score),True,(255,160,0))
    window.blit(text,(10,20))
    text = f1.render("Счёт за шлепок: " + str(point),True,(255,160,0))
    window.blit(text,(10,80))
    text = f1.render("мятные пряники--Цена: " + str(cost1),True,(255,160,0))
    window.blit(text,(350,0))
    text = f1.render("счёт + 1 ",True,(255,160,0))
    window.blit(text,(350,35))
    text = f1.render("нажмите 1 для покупки ",True,(255,160,0))
    window.blit(text,(350,70))
    text = f1.render("Тазик--Цена: " + str(cost2),True,(255,0,0))
    window.blit(text,(350,120))
    text = f1.render("счёт + 5 ",True,(255,0,0))
    window.blit(text,(350,155))
    text = f1.render("нажмите 2 для покупки ",True,(255,0,0))
    window.blit(text,(350,190))
    text = f1.render("пельмени--Цена: " + str(cost3),True,(0,160,0))
    window.blit(text,(350,240))
    text = f1.render("счёт + 20 ",True,(0,160,0))
    window.blit(text,(350,275))
    text = f1.render("нажмите 3 для покупки ",True,(0,160,0))
    window.blit(text,(350,310))
    text = f1.render("ШЛЁПАНЦЫ--Цена: " + str(cost4),True,(0,0,255))
    window.blit(text,(350,360))
    text = f1.render("счёт + 100 ",True,(0,0,255))
    window.blit(text,(350,395))
    text = f1.render("нажмите 4 для покупки ",True,(0,0,255))
    window.blit(text,(350,430))
    
    shop1()
    shop2()
    shop3()
    shop4()
    display.update()
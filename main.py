from pygame import *
import time


window = display.set_mode((700,500))
display.set_caption('mega flopper')

game = True
score = 0
point = 1
background = transform.scale(image.load('white.jpg'),(700,500)) 
floppa = transform.scale(image.load('floppa.png'),(200,200)) 
font.init()
f1 = font.Font(None, 36)
cost1 = 10


def shop1():
    global point
    global cost1
    global score
    keys = key.get_pressed()
    if keys[K_w] and cost1 <= score:
        score -= cost1
        time.sleep(1)
        point +=1
        cost1 +=1
        

mouse = mouse.get_pos()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
              if 0 <= mouse[0] <= 700 and  0 <= mouse[1] <= 500:
                  score += point
                  print(score)

    window.blit(background,(0,0))
    window.blit(floppa,(250,150))
    text = f1.render("Шлепков: " + str(score),True,(255,160,0))
    window.blit(text,(10,20))
    text = f1.render("Счёт за шлепок: " + str(point),True,(255,160,0))
    window.blit(text,(10,80))
    shop1()
    display.update()
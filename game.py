import pygame
from random import randint
import time
pygame.init()


'''створюємо вікно програми'''


back = (200,255,255)#колір фону (background)
mw = pygame.display.set_mode((500,500))#Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()


'''клас прямокутник'''


class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)#прямокутник
        self.fill_color = color


    def color(self, new_color):
        self.fill_color = new_color


    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)
    def outline(self, frame_color, thickness):#обведення існуючого прямокутника
        pygame.draw.rect(mw, frame_color,self.rect, thickness)

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
'''клас напис'''


class Label(Area):
	
    def set_text(self, Text, fsize =12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(Text,True, text_color)


    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))


YELLOW = (255,255,0)
DARK_BLUE = (0,0,100)
BLUE = (80,80,255)
GREEN=(0,255,51)
RED = (255,0,0)
LIGHT_RED=(255,128,114)
LIGHT_GREEN=(200,255,200)
start_time=time.time()
cur_time=start_time






cards = []
num_cards =4


x =70
time_text = Label(0,0,50,50,back)
time_text.set_text('Час:',40, DARK_BLUE)
time_text.draw(20, 20)


timer = Label(50,55,50,40,back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)


score_text = Label(380,0,50,50,back)
score_text.set_text('Рахунок:',45, DARK_BLUE)
score_text.draw(20,20)


score = Label(430,55,50,40,back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)

time_text = Label(0,0,50,50,back)
time_text.set_text('Час:',40, DARK_BLUE)
time_text.draw(20, 20)


timer = Label(50,55,50,40,back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)


score_text = Label(380,0,50,50,back)
score_text.set_text('Рахунок:',45, DARK_BLUE)
score_text.draw(20,20)


score = Label(430,55,50,40,back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)




for i in range(num_cards):
    new_card = Label(x,170,70,100, YELLOW)
    new_card.outline(BLUE,10)
    new_card.set_text('CLICK',26)
    cards.append(new_card)
    x = x +100


points=0
wait=0



while True:
    if wait == 0:
        #переносимо напис:
        wait = 20 #стільки тиків напис буде на одному місці
        click = randint(1, num_cards)
        for i in range(num_cards):
                cards[i].color(YELLOW)
                if (i + 1) == click:
                    cards[i].draw(10, 40)
                else:
                    cards[i].fill()
    else:
        wait -= 1
    


    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i in range(num_cards):
                    #шукаємо, в яку карту потрапив клік
                        if cards[i].collidepoint(x,y):
                            if i + 1 == click: #якщо на карті є напис - перефарбовуємо в зелений плюс очко
                                cards[i].color(GREEN)
                                points+=1
                            else: #інакше перефарбовуємо в червоний, мінус очко
                                cards[i].color(RED)
                                points-=1
                            
                            cards[i].fill()
                            score.set_text(str(points),40,DARK_BLUE)
                            score.draw(0,0)
    new_time=time.time()                        


    if new_time - start_time  >= 11:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text("Час вичерпано!!!", 60, DARK_BLUE)
        win.draw(110, 180)
        break
    
    if int(new_time) - int(cur_time) == 1: 
        timer.set_text(str(int(new_time - start_time)),40, DARK_BLUE)
        timer.draw(0,0)
        cur_time = new_time


    if points >= 5:
        win = Label(0, 0, 500, 500, LIGHT_GREEN)
        win.set_text("Ти переміг!!!", 60, DARK_BLUE)
        win.draw(140, 180)
        resul_time = Label(90, 230, 250, 250, LIGHT_GREEN)
        resul_time.set_text("Час проходження: " + str (int(new_time - start_time)) + " секунд", 40, DARK_BLUE)


        resul_time.draw(0, 0)


        break

    
    
    

    
    pygame.display.update()
    clock.tick(40)
pygame.display.update()



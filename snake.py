import sys
import pygame
import random


#蛇
class Snake(object):
#初始化长度 方向
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.addnode()

#方法
    def addnode(self):
        left,top = (0,0)
        if self.body:
            left,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left,top,25,25)
        #移动
        if self.dirction == pygame.K_LEFT:
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0,node)
    #删除增加 改变颜色 达到移动目的
    def delnode(self):
        self.body.pop()

    #死亡判断
    def isdead(self):
        #撞墙
        if self.body[0].x not in range(SCREEN_x):
            return True
        if self.body[0].y not in range(SCREEN_y):
            return True
        #撞自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    def move(self):
        self.addnode()
        self.delnode()
    #改变方向
    def changedirection(self,curkey):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD = [pygame.K_UP,pygame.K_DOWN]
        if curkey in LR + UD:
            if (curkey in LR) and (self.dirction in LR):
                return
            if (curkey in UD) and (self.dirction in UD):
                return
            self.dirction = curkey


#食物
class Food():
    def __init__(self):
        #第一次默认位置
        self.rect = pygame.Rect(-25,0,25,25)

    def remove(self):
        #颜色替换默认白背景
        self.rect.x = -25

    def set(self):
        if self.rect.x == -25:
            allpos = []
            #不能靠墙太近 25- -25
            for pos in range(25,SCREEN_x - 25,25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top = random.choice(allpos)
            print(self.rect)


SCREEN_x =750
SCREEN_y = 750
def show_text(screen,pos,text,color,font_bold=False,font_size=60,font_italic=False):
    #获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体",font_size)
    #设置是否加粗
    cur_font.set_bold(font_bold)
    #设置是否斜体
    cur_font.set_italic(font_italic)
    #设置文字内容
    text_fmt = cur_font.render(text,True,color)
    #绘制文字
    screen.blit(text_fmt,pos)

def level():
    if scores == 0:
        clock.tick(6)
    if scores >= 10 and scores < 50:
        clock.tick(7)
    if scores >= 50 and scores < 100:
        clock.tick(8)
    if scores >= 100 and scores < 150:
        clock.tick(9)
    if scores >= 150 and scores < 200:
        clock.tick(10)
    if scores >= 200 and scores < 250:
        clock.tick(11)
    if scores >= 250 and scores < 300:
        clock.tick(12)
    if scores >= 300 and scores < 350:
        clock.tick(13)
    if scores >= 350 and scores < 400:
        clock.tick(14)
    if scores >= 400 and scores <= 450:
        clock.tick(15)
    if scores >450: 
        clock.tick(16)
def main():
    #初始化
    pygame.init()
    screen_size = (SCREEN_x,SCREEN_y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('贪吃蛇')
    global clock
    clock = pygame.time.Clock()
    global scores
    scores= 0
    isdead = False
    snake = Snake()
    food = Food()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #按到下方向键
            if event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                if event.key == pygame.K_SPACE and isdead:
                    return main()
        #背景填充
        screen.fill((255,255,255))
        #画蛇身子
        if not isdead:
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen,(000000),rect,0)
        #显示死亡文字
        isdead = snake.isdead()

        if isdead:
            show_text(screen,(100,200),"you！dead！",(227,29,18),False,100)
            show_text(screen,(150,260),"space to again",(0,0,22),False,30)
            #食物的处理 吃到加10  长度加1
        if food.rect == snake.body[0]:
            scores += 10

            food.remove()
            snake.addnode()
        #重新放食物
        food.set()
        pygame.draw.rect(screen,(136,0,24),food.rect,0)
        #显示分数
        show_text(screen,(10,500),'scores:'+str(scores),(223,223,223))
        pygame.display.update()
        level()

main()


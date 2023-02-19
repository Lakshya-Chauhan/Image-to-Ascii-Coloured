import pygame
from os import system
def cls():
    system("cls")
pygame.init()
screen = pygame.display.set_mode((800,800))
icon = pygame.image.load('Images/test3.png')
pygame.display.set_caption("Grayscale")
pygame.display.set_icon(icon)
cls()
updater = 0
running = True
clock = pygame.time.Clock()
# img = pygame.transform.scale(pygame.image.load("Images/test11.png"), (200, 200))
img = pygame.transform.scale(pygame.image.load("Images/240520012_388539089419359_4219417691054480737_n.jpg"), (200, 96))
screen.blit(img, (0, 0))

chars = '█▓▒$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i! lI;:,"^`\'. '
# chars = '█▓▒░ '
x = 0
y = 0
sentence = ""
while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if x < 200 and y < 200:
        pxlColor = screen.get_at((x,y))[:3]
        intensity = (sum(pxlColor))/len(pxlColor)
        try:
            Ratio = [round(pxlColor[0]/max(pxlColor)), round(pxlColor[1]/max(pxlColor)), round(pxlColor[2]/max(pxlColor))]
        except:
            Ratio = [0, 0, 0]
            sentence += "\33[90m"

        if Ratio == [0, 0, 1]:
            sentence += "\33[34m"
        elif Ratio == [0, 1, 0]:
            sentence += "\33[32m"
        elif Ratio == [0, 1, 1]:
            sentence += "\33[36m"
        elif Ratio == [1, 0, 0]:
            sentence += "\33[31m"
        elif Ratio == [1, 0, 1]:
            sentence += "\33[35m"
        elif Ratio == [1, 1, 0]:
            sentence += "\33[33m"
        elif Ratio == [1, 1, 1]:
            sentence += "\33[37m"

        sentence += "\33[1m" + chars[int(-(intensity/255)*(len(chars)-1))-1]
        x += 1

    elif x >= 200:
        x=0
        y+=1
        print(sentence)
        sentence = ""
    #Code Here
    pygame.display.update()
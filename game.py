import pygame, math
from random import randrange
import pygame.freetype
import random
from tkinter import *
pygame.init()

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.freetype.SysFont('Comic Sans MS', 30)

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
SCHWARZ = ( 0, 0, 0)
WEiSS   = ( 255, 255, 255)
breite = 640
hoehe = 480

halbeBreite = breite / 2

#erster Balken
breiteRect = 80
hoeheRect = 20
spawnX = randrange(halbeBreite - 60, halbeBreite +60)
spawnY = 20
spawnX1 = spawnX + 175 #zweiter Balken
spawnX2 = spawnX - 175 #driter Balken
spawnX3 = spawnX + 350 #vierter Balken
spawnX4 = spawnX - 350 #fünfter Balken

#erster Balken für zweite Reihe
newSpawnReiheX = randrange(halbeBreite - 60, halbeBreite +60)
newSpawnReiheY = - 80
newSpawnReiheX1 = spawnX + 175 #zweiter Balken
newSpawnReiheX2 = spawnX - 175 #driter Balken

posPointsX = 600
posPointsY = 30
points = 0
# Fenster öffnen
screen = pygame.display.set_mode((breite, hoehe))

pygame.display.set_caption("Pygame-Spiel")

lauf = 0
minusLauf = 0.5
# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

#hier GAME OVER Fenster mit RESTART Button
#fenster = Tk()
#fenster.title("Python Game")

clock = pygame.time.Clock()
ball_posX = 320
ball_posY = 440

bewegX = 1
bewegY = 3
pressed = pygame.key.get_pressed()
# Schleife Hauptprogramm
while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("QUIT-BUTTON")
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball_posX = ball_posX + 35
            elif event.key == pygame.K_LEFT:
                ball_posX = ball_posX - 35

    # Spielfeld löschen
    screen.fill(SCHWARZ)

    #Figuren
    pygame.draw.ellipse(screen, WEiSS, [ball_posX, ball_posY, 20, 20]) #Ball
    pygame.draw.rect(screen, ORANGE, [spawnX, spawnY, 80, 20])
    pygame.draw.rect(screen, ORANGE, [spawnX1, spawnY, 80, 20])
    pygame.draw.rect(screen, ORANGE, [spawnX2, spawnY, 80, 20])
    pygame.draw.rect(screen, ORANGE, [spawnX3, spawnY, 80, 20])
    pygame.draw.rect(screen, ORANGE, [spawnX4, spawnY, 80, 20])

    #hier zweite Balkenreihe
    pygame.draw.rect(screen, ORANGE, [newSpawnReiheX, newSpawnReiheY, 80, 20])
    pygame.draw.rect(screen, ORANGE, [newSpawnReiheX1, newSpawnReiheY, 80, 20])
    pygame.draw.rect(screen, ORANGE, [newSpawnReiheX2, newSpawnReiheY, 80, 20])

    myfont.render_to(screen, (posPointsX, posPointsY), str(points), (255, 255, 255))
    #bewegen des Balkens nach unten
    spawnY = spawnY + bewegY
    newSpawnReiheY = newSpawnReiheY + bewegY

    # bewegen des Balkens nach links und rechts
    spawnX = spawnX + bewegX
    spawnX1 = spawnX1 + bewegX
    spawnX2 = spawnX2 + bewegX
    spawnX3 = spawnX3 + bewegX
    spawnX4 = spawnX4 + bewegX

    newSpawnReiheX = newSpawnReiheX + bewegX
    newSpawnReiheX1 = newSpawnReiheX1 + bewegX
    newSpawnReiheX2 = newSpawnReiheX2 + bewegX

    lauf = lauf + minusLauf
    if lauf > 20:
        minusLauf = minusLauf * (-1)
        bewegX = -1
    if lauf < -20:
        minusLauf = minusLauf *(-1)
        bewegX = 1

    #damit der Ball im Spielfeld bleibt
    if ball_posX > breite - 20:
        ball_posX = breite - 20
    elif ball_posX < 0:
        ball_posX = 0

    #damit der balken immer wieder neu runter fällt und an verschiedenen Stellen

    if spawnY > 480:
        spawnY = 0
        spawnX = randrange(halbeBreite - 60, halbeBreite +60)
        spawnX1 = spawnX + 175
        spawnX2 = spawnX - 175
        spawnX3 = spawnX + 350
        spawnX4 = spawnX - 350
        points = points + 10
        if points > 90 and points < 110:
            posPointsX = posPointsX - 10
        if points > 990 and points < 1010:
            posPointsX = posPointsX - 10
        if points >= 50 and points < 60:
            bewegY = bewegY + 1
        elif points >= 100 and points < 110:
            bewegY = bewegY + 1
            minusLauf = minusLauf + 0.5
        elif points >= 200 and points < 210:
            bewegY = bewegY + 1
        elif points >= 300 and points < 310:
            bewegY = bewegY + 1
        elif points >= 400 and points < 410:
            bewegY = bewegY + 1

    if newSpawnReiheY > 480:
        newSpawnReiheY = spawnY - 100
        newSpawnReiheX = randrange(halbeBreite - 60, halbeBreite + 60)
        newSpawnReiheX1 = newSpawnReiheX + 175
        newSpawnReiheX2 = newSpawnReiheX - 175

    if spawnY == ball_posY - 20:
        if ball_posX < spawnX + breiteRect and ball_posX > spawnX:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False
    if spawnY == ball_posY -20:
        if ball_posX < spawnX1 + breiteRect and ball_posX > spawnX1:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False
    if spawnY == ball_posY - 20:
        if ball_posX < spawnX2 + breiteRect and ball_posX > spawnX2:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False
    if spawnY == ball_posY - 20:
        if ball_posX < spawnX3 + breiteRect and ball_posX > spawnX3:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False
    if spawnY == ball_posY - 20:
        if ball_posX < spawnX4 + breiteRect and ball_posX > spawnX4:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False

    if newSpawnReiheY == ball_posY - 20:
        if ball_posX < newSpawnReiheX + breiteRect and ball_posX > newSpawnReiheX:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False
    if newSpawnReiheY == ball_posY - 20:
        if ball_posX < newSpawnReiheX1 + breiteRect and ball_posX > newSpawnReiheX1:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False
    if newSpawnReiheY == ball_posY - 20:
        if ball_posX < newSpawnReiheX2 + breiteRect and ball_posX > newSpawnReiheX2:
            screen.fill(SCHWARZ)
            myfont.render_to(screen, (40, 350), "Game Over!", (255, 255, 255))
            spielaktiv = False


    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)
pygame.time.wait(2000)
pygame.quit()
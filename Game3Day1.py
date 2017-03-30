from gamelib import *

game = Game(800,600,"Exploring List", 60)
bk = Animation("images\\field_5.png",5,game,1000,1000)
game.setBackground(bk)

asteroids = []

for num in range(150):
    asteroids.append(  Animation("images\\asteroid1t.gif",41,game,2173/41, 52, 2 )   )


for asteroid in asteroids:
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(4,8)
    asteroid.moveTo(x,y)
    asteroid.setSpeed(s,90)


while not game.over:
    game.processInput()
    game.drawBackground()

    for asteroid in asteroids:
        asteroid.move()

    game.update(30)

game.quit()

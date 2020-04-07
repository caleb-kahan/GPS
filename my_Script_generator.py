from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
time = 0
rot = 0
rotAddition = 1
while(rot>=0):
    print(time)
    t = new_matrix()
    ident(t)
    csystems = [ t ]

    if rot == 90:
        rotAddition = -1
    f = open("my_script", "w")
    f.write('''#BODY
    push
    move
    225 250 0
    rotate
    y -50
    rotate
    x {}
    box
    -100 125 50 200 250 100

    #HEAD
    push
    move
    0 175 0
    rotate
    y 90
    sphere
    0 0 0 50
    pop

    #LEFT ARM
    push
    move
    -100 125 0
    rotate
    x -70
    rotate
    y 45
    rotate
    z {}
    box
    -40 0 40 40 100 40
    #LEFT LOWER ARM
    push
    move
    -20 -100 20
    rotate
    z {}
    box
    -10 0 10 20 125 20
    pop
    pop
    #RIGHT ARM
    push
    move
    70 100 0
    rotate
    x -70
    rotate
    y 45
    rotate
    z {}
    box
    0 0 40 40 100 40
    #RIGHT LOWER ARM
    push
    move
    20 -100 20
    rotate
    z {}
    box
    -10 0 10 20 125 20
    pop
    pop

    #LEFT LEG
    push
    move
    -100 -125 0
    box
    0 0 40 50 120 80
    pop
    #RIGHT LEG
    push
    move
    100 -125 0
    box
    -50 0 40 50 120 80
    save
    pic{}.png
    '''.format(70+8*rot/90.0,rot,-rot,rot,-rot,time))
    f.close()
    parse_file( 'my_script', csystems, screen, color )
    clear_screen(screen)
    rot += rotAddition
    time +=1

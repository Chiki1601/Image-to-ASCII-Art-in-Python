from pywhatkit import image_to_ascii_art as sac
pic = 'upgrade.jpg'
text = "upgrade"        
sac(pic, text)

import turtle as t 
a_x = -170              
a_y = 350

p = t.Pen()
t.setup(430,768)
t.bgcolor('black')
p.speed(0)
p.up()
p.width(3)
f_n = 0
d_n = 4


def set_color(c):
    sym = {".": '#aaaaaa', "S" : '#00ff00', "#" : '#00ff00', "&" : '#00ff00', "@":'#00ff00', "$" : '#00ff00', "%" : '#00ff00', "!":'white', ":" :'white', "*":'black'}
    color = sym[c]
    p.pencolor(color)

def b(n, a_sym):
     p.up()
     if a_sym != '\n':
         set_color(a_sym)

     p.goto(a_x- n, a_y )
     p.down()
     p.forward(1)

text = open('upgrade.txt','r')
te = text.readlines()
for i in te:
    for j in i:
        b(f_n, j)
        f_n -= 4
    a_y -= 8
    a_x = -170    
    f_n = 0
    d_n = 4

t.done()


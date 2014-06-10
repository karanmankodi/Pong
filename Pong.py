from Tkinter import *
import time
import threading

root = Tk()

# Variables
width = 600
height = 400
paddle1 = 0
paddle2 = 0
ball = 0
paddle1x1 = 0.0
paddle1y1 = 0.0
paddle1x2 = 0.0
paddle1y2 = 0.0
paddle2x1 = 0.0
paddle2y1 = 0.0
paddle2x2 = 0.0
paddle2y2 = 0.0
ballx1 = 0.0
bally1 = 0.0
ballx2 = 0.0
bally2 = 0.0
dx = 0.005
dy = 0.005
ax = 0.005
ay = 0.005
        
# Draw Objects
def drawBall(canvas,x,y):
    global ball
    ball = canvas.create_oval(x-20,y-20,x+20,y+20,width=0,fill='blue')
    
def drawPaddle1(canvas,y):
    global paddle1
    paddle1 = canvas.create_rectangle(5, y, 10, y+80, fill='black')
    
def drawPaddle2(canvas,y):
    global paddle2
    paddle2 = canvas.create_rectangle(590, y, 595, y+80, fill='black')

# Paddle Movements
def key(event):
    keyPressed = str(event.keysym)
    print "pressed", keyPressed
    
    if (keyPressed == 'Up'):
        #move paddle 1 up
        global paddle1
        global paddle1y1
        paddle1y1 = canvas.coords(paddle1)[1]
        if (not(paddle1y1 < 0)):
            canvas.move(paddle1, 0 , -10)
            canvas.update()
        
        
    if (keyPressed == 'Down'):
        #move paddle 1 down
        global paddle1
        global paddle1y2
        global height
        paddle1y2 = canvas.coords(paddle1)[3]
        if (not(paddle1y2 > height)):
            canvas.move(paddle1, 0, 10)
            canvas.update()
        
    if (keyPressed == 'w'):
        #move paddle 2 up
        global paddle2
        global paddle2y1
        paddle2y1 = canvas.coords(paddle2)[1]
        if (not(paddle2y1 < 0)):
            canvas.move(paddle2, 0, -10)
            canvas.update()
        
    if (keyPressed == 's'):
        #move paddle 2 down
        global paddle2
        global paddle2y2
        global height
        paddle2y2 = canvas.coords(paddle2)[3]
        if (not(paddle2y2 > height)):
            canvas.move(paddle2, 0, 10)
            canvas.update()


# Ball movements
def moveBall():
    global dx
    global dy
    global ax
    global ay
    global ball
    while True:
        bounceOffTop()
        bounceOffBottom()
        collideWithPaddle1()
        collideWithPaddle2()
        canvas.move(ball, dx, dy)
        canvas.update()
        if (dx < 0):
            dx = dx - ax
        else:
            dx = dx + ax
        if (dy < 0):
            dy = dy - ay
        else:
            dy = dy + ay
        threading.Timer(1000, moveBall).start()
    

def bounceOffTop():
    global bally1
    global dy
    bally1 = canvas.coords(ball)[1]
    if (bally1 < 0):
        dy = -dy
        
def bounceOffBottom():
    global bally2
    global dy
    global height
    bally2 = canvas.coords(ball)[3]
    if (bally2 > height):
        dy = -dy
 
def collideWithPaddle1():
    global paddle1x2
    global paddle1y1
    global paddle1y2
    global ballx1
    global bally1
    global bally2
    global dy
    global dx
    ballx1 = canvas.coords(ball)[0]
    bally1 = canvas.coords(ball)[1]
    bally2 = canvas.coords(ball)[3]
    paddle1x2 = canvas.coords(paddle1)[2]
    paddle1y1 = canvas.coords(paddle1)[1]
    padlle1y2 = canvas.coords(paddle1)[3]
    if ((ballx1 <= paddle1x2) and (paddle1y1 < ((bally2 + bally1)/2) < paddle1y2)):
        dx = -dx

def collideWithPaddle2():
    global paddle2x1
    global paddle2y1
    global paddle2y2
    global ballx2
    global bally1
    global bally2
    global dy
    global dx
    ballx2 = canvas.coords(ball)[2]
    bally1 = canvas.coords(ball)[1]
    bally2 = canvas.coords(ball)[3]
    paddle2x1 = canvas.coords(paddle2)[0]
    paddle2y1 = canvas.coords(paddle2)[1]
    padlle2y2 = canvas.coords(paddle2)[3]
    if ((ballx2 >= paddle2x1) and (paddle2y1 < ((bally2 + bally1)/2) < paddle2y2)):
        dx = -dx
 
# Start Game    
def callback(event):
    canvas.focus_set()
    print "Game Started!"
    moveBall() 

# Draw Canvas
canvas = Canvas(root, bg="green", height=height, width=width)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()

#Draw Game Elements
canvas.create_line(300,0,300,400)
canvas.create_rectangle(0,0,600,400)
drawBall(canvas,300,200)
drawPaddle1(canvas, 300)
drawPaddle2(canvas, 40)  

root.mainloop()
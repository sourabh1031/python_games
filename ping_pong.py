from tkinter import *
import random
import time

counter = 0
counter1 = 0

root = Tk()
root.title("Perfect Goal")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(root,width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg = "black")
canvas.pack()
canvas.create_line(250,0,250,400,fill="white")

gameon = False

def startGame(event):
    global gameon
    gameon = True

startbtn = Button(root,text = "Start")
startbtn.pack()
startbtn.bind("<Button-1>",startGame)

root.update()

class Ball:
    def __init__(self,canvas,paddle_left,paddle_right,color):
        self.canvas = canvas
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id,235,200)
        starts = [-2,2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hitPaddleLeft(self,pos):
        paddle_pos = self.canvas.coords(self.paddle_left.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False
    
    def hitPaddleRight(self,pos):
        paddle_pos = self.canvas.coords(self.paddle_right.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
            self.score(True)
        if pos[2] >= self.canvas_width:
            self.x = -2
            self.score(False)
        if self.hitPaddleLeft(pos) == True:
            self.x = 2
        if self.hitPaddleRight(pos) == True:
            self.x = -2

    def score(self,val):
        global counter
        global counter1

        if val == True:
            a = self.canvas.create_text(375,40,text=counter,font=("Arial",40),fill="white")
            canvas.itemconfig(a,fill="black")
            counter += 1
            a = self.canvas.create_text(375,40,text=counter,font=("Arial",40),fill="white")

        if val == False:
            a = self.canvas.create_text(125,40,text=counter1,font=("Arial",40),fill="white")
            canvas.itemconfig(a,fill="black")
            counter1 += 1
            a = self.canvas.create_text(125,40,text=counter1,font=("Arial",40),fill="white")

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,20,250,fill = color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('h',self.moveUp)
        self.canvas.bind_all('l',self.moveDown)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
    
    def moveUp(self,event):
        self.y = -2

    def moveDown(self,event):
        self.y = 2

class Paddle1:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(480,150,500,250,fill = color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Up>',self.moveUp)
        self.canvas.bind_all('<KeyPress-Down>',self.moveDown)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
    
    def moveUp(self,event):
        self.y = -2

    def moveDown(self,event):
        self.y = 2 

paddle_left = Paddle(canvas,"purple")
paddle_right = Paddle1(canvas,"orange")
ball = Ball(canvas,paddle_left,paddle_right,"white")

while 1:
    if(gameon == True):
        ball.draw()
        paddle_left.draw()
        paddle_right.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    
    if counter == 10:
        ball.x = 0
        ball.y = 0
        paddle_left.y = 0
        paddle_right.y = 0
        break
        
    
    if counter1 == 10:
        ball.x = 0
        ball.y = 0
        paddle_left.y = 0
        paddle_right.y = 0
        break
        

if(counter == 10):
    canvas.create_text(250,200,text="Congrats Player 2 !! You won",font = ("Cursive",20),fill = "green")
    canvas.create_text(250,235,text="Score is:" + str(counter1) + " , " +str(counter),font = ("Cursive",15),fill = "green")
if(counter1 == 10):
    canvas.create_text(250,200,text="Congrats Player 1 !! You won",font = ("Cursive",20),fill = "green")
    canvas.create_text(250,235,text="Score is:" + str(counter1) + " , " +str(counter),font = ("Cursive",15),fill = "green")

root.mainloop()
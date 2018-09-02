from tkinter import *
import random
import time
root = Tk()
root.title("Save the Ball!!")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(root,width = 500, height = 500, bd = 0, highlightthickness = 0,bg = "black")
canvas.pack()
count = -1
gameon = False

def startGame(event):
    global gameon
    gameon = True
    ball.score()
# ans.configure(text = "Score: " + str(0))
# def pauseGame():
#     pass

# def closeGame():
#     pass

startbtn = Button(root,text = "Start")
startbtn.pack()
startbtn.bind("<Button-1>",startGame)

# pausebtn = Button(root,text = "Pause",command = pauseGame)
# pausebtn.pack(side = LEFT)
# pausebtn.bind("<Button-1>",pauseGame)
# exitbtn = Button(root,text = "Exit")
# exitbtn.pack(side = RIGHT)
root.update()

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id,250,100)
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hitPaddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score()
                return True
            return False

    def score(self):
        global count
        self.scoreboard = canvas.create_text(400,40,text = "Score: " + str(count),fill = "white",font=("Cursive",20))
        canvas.itemconfig(self.scoreboard,fill = "black")
        count += 1
        self.scoreboard = canvas.create_text(400,40,text = "Score: " + str(count),fill = "white",font=("Cursive",20))

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            if count <= 10:
                canvas.itemconfig(self.scoreboard,fill = "black")
                canvas.create_text(350,40,text = "You are Beginner",fill = "white",font=("Cursive",20))
            elif count > 10 and count <= 30:
                canvas.itemconfig(self.scoreboard,fill = "black")
                canvas.create_text(350,40,text = "You are Intermediate",fill = "white",font=("Cursive",20))
            elif count > 30 and count <= 50:
                canvas.itemconfig(self.scoreboard,fill = "black")
                canvas.create_text(350,40,text = "You are Advanced",fill = "white",font=("Cursive",20))
            else:
                canvas.itemconfig(self.scoreboard,fill = "black")
                canvas.create_text(350,40,text = "You are Expert",fill = "white",font=("Cursive",20))
            canvas.create_text(250,100,text = "Game Over",font=('Cursive',20),fill="yellow")
            canvas.create_text(250,130,text = "Your Score is: " +str(count),font=('Cursive',10),fill="yellow")
            # canvas.create_text(250,200,text = "Do you want to start again ?",font=('Cursive',22),fill="green")
            # canvas.create_text(250,240,text = "Press y for yes or n for no",font=('Cursive',14),fill="green")
            # answer = self.canvas.bind("<Return>",self.playAgain)
            # print(answer)   
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
        if self.hitPaddle(pos) == True:
            self.y = -2

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = color)
        self.canvas.move(self.id,200,350)
        self.x = 0
        self.canvas.bind_all("<KeyPress-Left>",self.moveLeft)
        self.canvas.bind_all("<KeyPress-Right>",self.moveRight)
        self.canvas_width = self.canvas.winfo_width()
    
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
        
    def moveLeft(self,evt):
        self.x = -2
    def moveRight(self,evt):
        self.x = 2

paddle = Paddle(canvas,'white')
ball = Ball(canvas,paddle,'red')

while 1:
    if ball.hit_bottom == False and gameon == True:
        ball.draw()
        paddle.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()
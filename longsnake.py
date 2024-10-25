import turtle
import time
import random
import os
import webbrowser
window=turtle.Screen()
window.colormode(255)
window.bgcolor(0,0,255)
c1=0
c2=255
"""Vytvoreni okna. Registrace obrazku"""
window.title("Hladik")
window.setup(width=900, height=580)
turtle.register_shape('birdo.gif')
turtle.register_shape('judge.gif')
turtle.register_shape('speech2.gif')
turtle.register_shape('cages.gif')
"""Zpracovani txt"""
with open("texts.txt", "r") as my_file:
    lines = str(my_file.read())
phraselist=[]
line=""
for i in lines:
    if i =="\n":
        phraselist.append(line)
        line=""
    else:
        line+=i
phraselist.append(line)
"""Dokumentace"""
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cesta k html
html_file_path = os.path.join(current_dir, 'Dokumentace.html')
"""Tvorba hada"""
snake=turtle.Turtle()
snake.speed(0)
snake.penup()
snake.goto(250,290)
snake.pendown()
snake.goto(250,-290)
"""Funkce pro poslouchani klaves"""
def up():
    snake.setheading(90)
window.listen()
def left():
    snake.setheading(180)
def right():
    snake.setheading(0)
def down():
    snake.setheading(270)
def move():
    snake.forward(15)
def znovu():
    done=True
def pomoc():
    webbrowser.open_new_tab('file://' + html_file_path)
    
window.onkeypress(up,"Up")
window.onkeypress(left,"Left")
window.onkeypress(right,"Right")
window.onkeypress(down,"Down")
window.onkeypress(znovu, 'space')
window.onkeypress(pomoc, 'h')
"""Dotvoreni hada"""
snake.shape("square")
snake.color(0,0,0)
snake.penup()
snake.goto(0,0)
"""tvorba jidla"""
food=turtle.Turtle()
food.penup()
food.speed(0)
food.shape('circle')
food.color(255,0,0)
food.goto(200,200)
window.tracer(0)
casprom=0.001
class Snake:
    def __init__(self,hlava):
        self.structure=[hlava]
        self.positonlist=[]
        self.head=hlava
        self.movement=3
        self.novyclen=False
        self.pocitadlo=0
    def growth(self):
        """pocatecni stizeni obtiznosti pak je jiz neprijemny had"""
        if self.movement<15:
            self.movement+=1
        """for i in self.structure:
            velikost=i.turtlesize()
            increase=(1.1 * x for x in velikost)
            print(increase)
            i.shapesize(*increase)"""
        for i in range(5):
            body = turtle.Turtle()
            body.shape("square")
            body.color(0, 0, 0)
            body.penup()
            body.goto(self.head.pos())
            self.structure.append(body)
        self.novyclen=True

    def die(self):
        for i in range(len(self.structure)-1):
            self.structure[-1].hideturtle()
            self.structure[-1].goto(350,-100)
            self.structure.pop(-1)
        self.movement=3
        self.structure[0].goto(0,0)
        
    def move(self):
        zaloldpos=self.head.pos()
        oldpos=self.head.pos()
        self.head.forward(self.movement)
        for i in self.positonlist:
            if self.head.distance(i)<1:
                finish()
                
        for i in range(1,len(self.structure)):
            newoldpos=self.structure[i].pos()
            self.structure[i].goto(oldpos)
            oldpos=newoldpos
        if len(self.structure)>20:
            self.positonlist=[self.structure[i] for i in range(20,len(self.structure))]
class Duolingo:
    def __init__(self):
        """owl"""
        self.freedom=False
        owl=turtle.Turtle()
        owl.shape('judge.gif')
        owl.speed(0)
        owl.penup()
        owl.goto(350,-100)
        self.picture1=owl
        """klec"""
        cage=turtle.Turtle()
        cage.shape('cages.gif')
        cage.speed(0)
        cage.penup()
        cage.goto(350,-50)
        
        self.pen=turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        bubble=turtle.Turtle()
        bubble.shape('speech2.gif')
        bubble.speed(0)
        bubble.penup()
        bubble.hideturtle()
        bubble.goto(350,100)
        self.picture2=bubble
    def speakingbird(self):
        self.picture2.showturtle()
        phrase=random.choice(phraselist)
        self.pen.clear()
        y=140
        self.pen.goto(350,y)
        word=""
        counter=0
        sentence=""
        for i in phrase:
            word+=i
            counter+=1
            if ord (i)==32:
                if counter>13:
                    self.pen.write(sentence ,align="center", font=("calibri",15,"bold"))
                    sentence=""
                    counter=len(word)
                    y-=15
                    self.pen.goto(350,y)
                sentence+=word
                word=""
                    

        if counter>13:
                    self.pen.write(sentence ,align="center", font=("calibri",15,"bold"))
                    y-=15
                    self.pen.goto(350,y)
                    self.pen.write(word ,align="center", font=("calibri",15,"bold"))
        else:
            sentence+=word
            self.pen.write(sentence ,align="center", font=("calibri",15,"bold"))
    def unleashed(self):
        self.pen.clear()
        self.picture2.hideturtle()
        self.picture1.shape("birdo.gif")
        self.freedom=True
        self.planning()
    def planning(self):
        self.picture1.goto(random.randint(-200,100),290)
        self.picture1.setheading(random.randint(230,310))
    def arrest(self):
        self.freedom=False
        self.picture1.shape("judge.gif")
        self.picture1.goto(350,-100)
        
        
            
            
        
        
        

def finish():
    snakecomp.die()
    ptak.arrest()
    global score
    score=0
    pen.clear()
    pen.write(f"Skóre: {score}",align="center", font=("calibri",24,"bold"))
pred=1
counter=0
snakecomp=Snake(snake)
"""Score-pocitani"""
score=0
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,250)
pen.write(f"Skóre: {score}",align="center", font=("calibri",24,"bold"))
"""Duolingo bird object int"""
ptak=Duolingo()
done=False
while not done:
    if snake.distance(food)<20:
        if not ptak.freedom:
            utek=random.randint(1,7)
            if utek!=5:
                ptak.speakingbird()
            else:
                ptak.unleashed()
        x,y=random.randint(-250,250),random.randint(-230,230)
        food.goto(x,y)
        snakecomp.growth()
        score+=1
        pen.clear()
        pen.write(f"Skóre: {score}",align="center", font=("calibri",24,"bold"))
    snakecomp.move()
    counter+=1
    window.update()
    time.sleep(casprom)
    if snake.xcor()>250 or snake.xcor()<-440 or snake.ycor()<-290 or snake.ycor()>290:
        finish()
    if counter==1:
        if c2>253:
            pred=-1
        elif c2<3:
            pred = 1
        counter=0
        c2+=pred
        c1-=pred
        if ptak.freedom:
            window.bgcolor(c1, 0, c2)
        else:
            window.bgcolor(0, c1, c2)
    if ptak.freedom:
        if(ptak.picture1.pos()[1]<(-280)):
           ptak.planning()
        else:
            ptak.picture1.forward(6)
            if ptak.picture1.distance(snakecomp.head)<30:
                ptak.arrest()
                score+=3
                pen.clear()
                pen.write(f"Skóre: {score}",align="center", font=("calibri",24,"bold"))
            for i in snakecomp.structure:
                if ptak.picture1.distance(i)<30:
                    finish()
    
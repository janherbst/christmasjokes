import sys
from Tkinter import *

windowone= Tk()

windowone.geometry("700x300+50+50")

windowone.title("Christmas Jokes For Kids")

var= "Hey Kids, are you ready to laugh about some funny jokes? \n If yes, click onto one of the four images. Let's see what happens."
Text= Label(windowone, text=var, relief=RAISED, bd=0, fg = "red", font = "Arial 13 bold italic")
Text.pack()

frame = Frame(windowone)
frame.pack()

frame = Frame(windowone)
frame.pack( side = TOP )


def treejoke1answer1():
    treejoke1ans = Tk()
    treejoke1ans.title("Answer: Joke 1")
    treejoke1ans.geometry("300x50+700+20")

    var= "A pineapple!"
    Text= Label(treejoke1ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(treejoke1ans, text="Close", width=20, command=treejoke1ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    treejoke1ans.mainloop()

def treejoke1answer2():
    treejoke1ans = Tk()
    treejoke1ans.title("Answer: Joke 2")
    treejoke1ans.geometry("300x50+700+20")

    var= "They both drop needles"
    Text= Label(treejoke1ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(treejoke1ans, text="Close", width=20, command=treejoke1ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    treejoke1ans.mainloop()
    
def treejoke1answer3():
    treejoke1ans = Tk()
    treejoke1ans.title("Answer: Joke 3")
    treejoke1ans.geometry("300x50+700+20")

    var= "A broken drum - you can't beat it!"
    Text= Label(treejoke1ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(treejoke1ans, text="Close", width=20, command=treejoke1ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    treejoke1ans.mainloop()

def treejoke1answer4():
    treejoke1ans = Tk()
    treejoke1ans.title("Answer: Joke 4")
    treejoke1ans.geometry("300x50+700+20")

    var= "Camel ye faithful!"
    Text= Label(treejoke1ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(treejoke1ans, text="Close", width=20, command=treejoke1ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    treejoke1ans.mainloop()


def robinjoke2answer1():
    robinjoke2ans = Tk()
    robinjoke2ans.title("Answer: Joke 1")
    robinjoke2ans.geometry("300x50+700+20")

    var= "Water!"
    Text= Label(robinjoke2ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(robinjoke2ans, text="Close", width=20, command=robinjoke2ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    robinjoke2ans.mainloop()

def robinjoke2answer2():
    robinjoke2ans = Tk()
    robinjoke2ans.title("Answer: Joke 2")
    robinjoke2ans.geometry("300x50+700+20")

    var= "Deep pan, crisp and even!"
    Text= Label(robinjoke2ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(robinjoke2ans, text="Close", width=20, command=robinjoke2ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    robinjoke2ans.mainloop()

def robinjoke2answer3():
    robinjoke2ans = Tk()
    robinjoke2ans.title("Answer: Joke 3")
    robinjoke2ans.geometry("300x50+700+20")

    var= "Silent Night!"
    Text= Label(robinjoke2ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(robinjoke2ans, text="Close", width=20, command=robinjoke2ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    robinjoke2ans.mainloop()

def robinjoke2answer4():
    robinjoke2ans = Tk()
    robinjoke2ans.title("Answer: Joke 4")
    robinjoke2ans.geometry("300x50+700+20")

    var= "Jungle bells, jungle bells!"
    Text= Label(robinjoke2ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(robinjoke2ans, text="Close", width=20, command=robinjoke2ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    robinjoke2ans.mainloop()


def snowmanjoke4answer1():
    snowmanjoke4ans = Tk()
    snowmanjoke4ans.title("Answer: Joke 1")
    snowmanjoke4ans.geometry("300x50+700+20")

    var= "Can you smell carrot?"
    Text= Label(snowmanjoke4ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(snowmanjoke4ans, text="Close", width=20, command=snowmanjoke4ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    snowmanjoke4ans.mainloop()

def snowmanjoke4answer2():
    snowmanjoke4ans = Tk()
    snowmanjoke4ans.title("Answer: Joke 2")
    snowmanjoke4ans.geometry("300x50+700+20")

    var= "He waits for the weather to get warmer!"
    Text= Label(snowmanjoke4ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(snowmanjoke4ans, text="Close", width=20, command=snowmanjoke4ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    snowmanjoke4ans.mainloop()

def snowmanjoke4answer3():
    snowmanjoke4ans = Tk()
    snowmanjoke4ans.title("Answer: Joke 3")
    snowmanjoke4ans.geometry("300x50+700+20")

    var= "Frosted flakes!"
    Text= Label(snowmanjoke4ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(snowmanjoke4ans, text="Close", width=20, command=snowmanjoke4ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    snowmanjoke4ans.mainloop()

def snowmanjoke4answer4():
    snowmanjoke4ans = Tk()
    snowmanjoke4ans.title("Answer: Joke 4")
    snowmanjoke4ans.geometry("300x50+700+20")

    var= "Freeze a jolly good fellow!"
    Text= Label(snowmanjoke4ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(snowmanjoke4ans, text="Close", width=20, command=snowmanjoke4ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    snowmanjoke4ans.mainloop()


def santajoke3answer1():
    santajoke3ans = Tk()
    santajoke3ans.title("Answer: Joke 1")
    santajoke3ans.geometry("300x50+700+20")

    var= "Santa Jaws!"
    Text= Label(santajoke3ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(santajoke3ans, text="Close", width=20, command=santajoke3ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    santajoke3ans.mainloop()

def santajoke3answer2():
    santajoke3ans = Tk()
    santajoke3ans.title("Answer: Joke 2")
    santajoke3ans.geometry("300x50+700+20")

    var= "Only one, after that it's not empty any more!"
    Text= Label(santajoke3ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(santajoke3ans, text="Close", width=20, command=santajoke3ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    santajoke3ans.mainloop()

def santajoke3answer3():
    santajoke3ans = Tk()
    santajoke3ans.title("Answer: Joke 3")
    santajoke3ans.geometry("300x50+700+20")

    var= "Santa Paws!"
    Text= Label(santajoke3ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(santajoke3ans, text="Close", width=20, command=santajoke3ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    santajoke3ans.mainloop()

def santajoke3answer4():
    santajoke3ans = Tk()
    santajoke3ans.title("Answer: Joke 4")
    santajoke3ans.geometry("300x50+700+20")

    var= "Crisp Cringle!"
    Text= Label(santajoke3ans, text=var, relief=RAISED, bd=0)
    Text.pack()

    quit0 = Button(santajoke3ans, text="Close", width=20, command=santajoke3ans.destroy)
    quit0.pack(side='bottom', padx=0,pady=0)

    santajoke3ans.mainloop()


def treejokes():
    windowone = Tk()
    windowone.title("Tree Jokes")
    windowone.geometry("700x150+50+50")

    treejoke1 = Button(windowone, text="What do you get if you cross an apple with a Christmas tree?", width=600, command=treejoke1answer1)
    treejoke1.pack(side='top', padx=0,pady=0)

    treejoke2 = Button(windowone, text="Why are Christmas trees like bad knitters?", width=600, command=treejoke1answer2)
    treejoke2.pack(side='top', padx=0,pady=0)

    treejoke3 = Button(windowone, text="What is the best Christmas present in the world?", width=600, command=treejoke1answer3)
    treejoke3.pack(side='top', padx=0,pady=0)

    treejoke4 = Button(windowone, text="What carol is heard in the desert?", width=600, command=treejoke1answer4)
    treejoke4.pack(side='top', padx=0,pady=0)

    quit1 = Button(windowone, text="Close", width=20, command=windowone.destroy)
    quit1.pack(side='bottom', padx=0,pady=0)

    windowone.mainloop()

def robinjokes():
    windowone = Tk()
    windowone.title("Robin Jokes")
    windowone.geometry("700x150+50+50")

    robinjoke1 = Button(windowone, text="What do you call an old snowman?", width=600, command=robinjoke2answer1)
    robinjoke1.pack(side='top', padx=0,pady=0)

    robinjoke2 = Button(windowone, text="How does Good King Wenceslas like his pizzas?", width=600, command=robinjoke2answer2)
    robinjoke2.pack(side='top', padx=0,pady=0)

    robinjoke3 = Button(windowone, text="What Christmas carol is a favourite of parents?", width=600, command=robinjoke2answer3)
    robinjoke3.pack(side='top', padx=0,pady=0)

    robinjoke4 = Button(windowone, text="What do monkeys sing at Christmas?", width=600, command=robinjoke2answer4)
    robinjoke4.pack(side='top', padx=0,pady=0)

    quit2 = Button(windowone, text="Close", width=20, command=windowone.destroy)
    quit2.pack(side='bottom', padx=0,pady=0)

    windowone.mainloop()
    
def snowmanjokes():
    windowone= Tk()
    windowone.title("Snowman Jokes")
    windowone.geometry("700x150+50+50")

    snowmanjoke1 = Button(windowone, text="What did one snowman say to the other snowman?", width=600, command=snowmanjoke4answer1)
    snowmanjoke1.pack(side='top', padx=0,pady=0)

    snowmanjoke2 = Button(windowone, text="How does a snowman lose weight?", width=600, command=snowmanjoke4answer2)
    snowmanjoke2.pack(side='top', padx=0,pady=0)

    snowmanjoke3 = Button(windowone, text="What do snowmen eat for breakfast?", width=600, command=snowmanjoke4answer3)
    snowmanjoke3.pack(side='top', padx=0,pady=0)

    snowmanjoke4 = Button(windowone, text="What do you sing at a snowman's birthday party?", width=600, command=snowmanjoke4answer4)
    snowmanjoke4.pack(side='top', padx=0,pady=0)

    quit3 = Button(windowone, text="Close", width=20, command=windowone.destroy)
    quit3.pack(side='bottom', padx=0,pady=0)

    windowone.mainloop()

def santajokes():
    windowone= Tk()
    windowone.title("Santa Jokes")
    windowone.geometry("700x150+50+50")

    santajoke1 = Button(windowone, text="Who delivers presents to baby sharks at Christmas?", width=600, command=santajoke3answer1)
    santajoke1.pack(side='top', padx=0,pady=0)

    santajoke2 = Button(windowone, text="How many presents can Santa fit in an empty sack?", width=600, command=santajoke3answer2)
    santajoke2.pack(side='top', padx=0,pady=0)

    santajoke3 = Button(windowone, text="Who gives puppies Christmas presents?", width=600, command=santajoke3answer3)
    santajoke3.pack(side='top', padx=0,pady=0)

    santajoke4 = Button(windowone, text="What do you get if Santa goes down the chimney when the fire is lit?", width=600, command=santajoke3answer4)
    santajoke4.pack(side='top', padx=0,pady=0)

    quit4 = Button(windowone, text="Close", width=20, command=windowone.destroy)
    quit4.pack(side='bottom', padx=0,pady=0)

    windowone.mainloop()
    
tree = PhotoImage(file = "christmas_tree.gif")
treebutton = Button(frame, text="Christmas Tree", image=tree, bd=0, command = treejokes)
treebutton.pack( side = LEFT)

robin = PhotoImage(file = "robin.gif")
robinbutton = Button(frame, text="Robin", image=robin, bd=0, command = robinjokes)
robinbutton.pack( side = LEFT )

snowman = PhotoImage(file = "snowman.gif")
snowmanbutton = Button(frame, text="Snowman", image=snowman, bd=0, command = snowmanjokes)
snowmanbutton.pack( side = RIGHT )

santa = PhotoImage(file = "santa.gif")
santabutton = Button(frame, text="Santa", image=santa, bd=0, command = santajokes)
santabutton.pack( side = RIGHT )

quit0 = Button(windowone, text="Quit", width=20, command=windowone.destroy)
quit0.pack(side='bottom', padx=0,pady=0)

windowone.mainloop()

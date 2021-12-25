from tkinter import *
import random
tk = Tk()
tk.title("Светофор")
tk.geometry("400x600")
tk.configure(bg='light blue')
tk.iconbitmap("icon.ico")
time = 10
y1 = 540
game = True
y2 = 0
a = random.randint(3, 6)
img = PhotoImage(file='img.png')
btn3 = None
start = 1

def go():
    global txt1, btn1, btn2, btn3, player, y1, y2, a, game, time, win, start
    y1 = y1-3
    player.place(x=199, y=y1, width=50, height=58)
    if start == 1:
        timer()
        green()
        start = 0
    if y1 <= 45:
        win = True
        clear()
def goevent(event):
    if game == True:
        go()
def timer():
    global txt1, btn1, btn2, btn3, player, y1, y2, a, game, time, win, start
    if game == False:
        btn1.after_cancel(green)
        txt1.destroy()
        if win == True:
            btn1.configure(text="Победа", bg="lime")
            return
        elif win == False:
            btn1.configure(text="Поражение", bg="orange")
            return
    time = time - 1
    txt1.configure(text=time)
    if time == 0:
        btn1.configure(text="Время вышло", bg="orange")
        game = False
        win = False
        tk.after_cancel(timer)
        clear()
        return
    tk.after(1000, timer)
def red():
    global txt1, btn1, btn2, btn3, player, y1, y2, a, game, time, win, start
    btn1.configure(text="Красный свет", bg="red")
    if game == False:
        btn1.after_cancel(red)
        if win == True:
            btn1.configure(text="Победа", bg="lime")
        elif win == False:
            btn1.configure(text="Поражение", bg="orange")
        return
    if y1 == y2:
        game = False
        win = False
        clear()
    if time == 0:
        btn1.after_cancel(red)
        return
    if a == 0:
        btn1.after_cancel(red)
        a = random.randint(1000, 2500)
        green()
        return
    if a != 0:
        a = a - 1
        btn1.after(1, red)
def green():
    global txt1, btn1, btn2, btn3, player, y1, y2, a, game, time, win, start
    btn1.configure(text="Зелёный свет", bg="green")
    if game == False:
        btn1.after_cancel(green)
        clear()
        if win == True:
            btn1.configure(text="Победа", bg="lime")
        elif win == False:
            btn1.configure(text="Поражение", bg="orange")
        return
    if a < 300:
        btn1.configure(text="Жёлтый свет", bg="yellow")
    if time == 0:
        btn1.after_cancel(green)
        return
    if a == 0:
        btn1.after_cancel(green)
        a = random.randint(700, 1500)
        y2 = y1 - 3
        red()
        return
    if a != 0:
        a = a - 1
        btn1.after(1, green)
def restart():
    global txt1, btn1, btn2, btn3, player, y1, y2, a, game, time, win, start
    a = random.randint(1000, 3000)
    if game == False and btn3:
        btn3.destroy()
        btn3 = None
    start = 1
    game = True
    y1 = 540
    y2 = y1 - 3
    time = 15
    txt1 = Label(text=time, bg="light blue", font=("Impact", 25))
    txt1.place(x=340, y=70, width = 60, height= 60)
    btn1 = Button(text="Зелёный свет", bg="green", font=("Impact", 20))
    btn1.place(x=0, y=0, width=402, height=70)
    btn2 = Button(text="↑", command=go, bg="purple", font=("Impact", 35))
    btn2.place(x=5, y=525, width=70, height=70)
    player=Label(image=img)
    player.place(x=199, y=y1, width=50, height=58)
def playagain(event):
    if game == False:
        restart()
def clear():
    global txt1, btn1, btn2, btn3, player, y1, y2, a, game, time, win
    game = False
    if btn3:
        btn3.destroy()
    btn3 = Button(text="Играть снова", bg="red", font=("Impact", 20), command=restart)
    btn3.place(x=120, y=510)
    txt1.destroy()
    btn2.destroy()
    player.destroy()
tk.bind('<Up>', goevent)
tk.bind('<KeyPress-w>', goevent)
tk.bind('<Return>', playagain)
restart()
tk.mainloop()




from tkinter import *


def go(event):
    x, y, vx, vy = float(X.get()), float(Y.get()), float(VX.get()), float(VY.get())
    m, k, dt, t = float(M.get()), float(K.get()), float(DT.get()), float(T.get())
    g = 9.806
    ball = None
    while t > 0:
        t -= dt
        ay = (m * g - k * vy) / m
        ax = (- k * vx) / m
        y += vy * dt + ay * (dt ** 2) / 2
        x += vx * dt + ax * (dt ** 2) / 2
        vx += ax * dt
        vy += ay * dt
        ball = c.create_oval(x, y, x+5, y+5, fill="black")
        print('x: ', x, 'y: ', y, 'vy: ', vy, 'vx: ', vx)


root = Tk()
root.resizable(width=False, height=False)
root.geometry('900x700')

X = Entry(width=20)
X.focus_set()
X.pack()

Y = Entry(width=20)
Y.focus_set()
Y.pack()

VX = Entry(width=20)
VX.focus_set()
VX.pack()

VY = Entry(width=20)
VY.focus_set()
VY.pack()

M = Entry(width=20)
M.focus_set()
M.pack()

K = Entry(width=20)
K.focus_set()
K.pack()

DT = Entry(width=20)
DT.focus_set()
DT.pack()

T = Entry(width=20)
T.focus_set()
T.pack()

start = Button(text="Вывести")
start.bind('<Button-1>', go)
start.pack()

c = Canvas(root, width=650, height=500, bg='gray')
c.pack()

root.mainloop()

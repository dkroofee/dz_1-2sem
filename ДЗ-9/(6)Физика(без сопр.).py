x = float(input())
y = float(input())
Vx = float(input())
Vy = float(input())
m = float(input())
dt = float(input())
T = float(input())
T1 = 0
a = -10
while T1 < T:
    T1 += dt
    y = y + Vy * dt + a * (dt ** 2) / 2
    x = x + Vx * dt
    Vy = Vy + a * dt
    print('T1 = ', T1, ' x = ', x, ' y = ', y, ' Vy = ', Vy)
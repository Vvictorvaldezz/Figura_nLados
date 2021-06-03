"""VICTOR HUGO VALDEZ ROBLES
GRAFICACION 3061"""
from turtle import Turtle

def DDA(fig, lon):     
    tortuga=Turtle()
    tortuga.color('yellow')
    longitu=lon
    nLado=fig
    X1=5
    Y1=4
    X2=6
    Y2=5
    dx = abs(X2 - X1)
    dy = abs(Y2 - Y1)
    steps = 0
    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)
          
    xInc = float(dx / steps)
    yInc = float(dy / steps)
    xInc = round(xInc,1)
    yInc = round(yInc,1)

    tortuga.screen.bgcolor('black')
    tortuga.pensize(2)
    tortuga.hideturtle()
    tortuga.speed(45)

    for i in range(0, int(steps)):
        tortuga.setx(X1)
        tortuga.sety(Y1)        
        angulo=180-(((nLado-2)/nLado)*180)         
        for i in range(nLado):
            tortuga.left(angulo)
            tortuga.fd(0)
            for i in range(longitu):
                tortuga.fd(15)
                coor=tortuga.pos()
                print('\n  '+str(coor))
                for i in range(4):
                    tortuga.forward(15)
                    tortuga.left(90)
            tortuga.forward(15)
        

def bres(fig, lon):
    tortuga=Turtle()
    tortuga.color('blue')
    longitu=lon
    nLado=fig

    X1=5
    Y1=4
    X2=7
    Y2=8
   
    dx = abs(X2 - X1)
    dy = abs(Y2 - Y1)
    p = 2*dy - dx
    X = X1
    Y = Y1

    tortuga.screen.bgcolor('black')
    tortuga.pensize(2)
    tortuga.hideturtle()
    tortuga.speed(45)    
    while (X <= X2):
        if(dx<0):
            X -= 1
        else:
            X +=1
        if (dy<0):
            if p <0:
                p = p + 2 * dy
                Y -= 1
            else:
                p = p + (2*dy) -(2*dx)
        else:
            if(p<0):
                p = p + 2 * dy
            else:
                p = p + (2*dy) -(2*dx)
                Y += 1
        angulo=180-(((nLado-2)/nLado)*180) 
        for i in range(nLado):
            tortuga.left(angulo)
            tortuga.fd(0)
            for i in range(longitu):
                tortuga.fd(15)
                coor=tortuga.pos()
                print('\n  '+str(coor))     
                for i in range(4):
                    tortuga.forward(15)
                    tortuga.left(90)
            tortuga.forward(15)

def main():
 fig = int (input("¿De cuantos lados es la figura que desea graficar? "))
 lon = int (input("¿Longuitud de las lineas?"))
 entrada = int(input("¿Qué algoritmo deseas usar? \n(1) DDA\n(2) Bresenham\n Elije un algoritmo : "))
 print("  X      Y")
 if entrada == 1:
        DDA(fig, lon)
 elif entrada == 2:
        bres(fig, lon)
 else:
        print("Adios!!")   

if __name__ == '__main__':
    main()
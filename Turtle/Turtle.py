import turtle
import math

bob = turtle.Turtle()
bib = turtle.Turtle()

def triangulo(t,tamanho, bool):
    for i in range(3):
        if bool == True:
            t.fd(tamanho)
            t.lt(120)
        elif bool == False:
            t.fd(tamanho)
            t.lt(-120)

def quadrado(t, tamanho, bool):
    for i in range(4):
        t.fd(tamanho)
        if bool == True:
            t.lt(90)
        elif bool == False:
            t.lt(-90)

def polygon(tartaruga, quant_lados, tamanho):
    angle = 360 / quant_lados

    for i in range(quant_lados):
        tartaruga.fd(tamanho)
        tartaruga.lt(angle)

def p(tartaruga, t2, quant_lados, tamanho):
    angle = 360 / quant_lados

    for i in range(quant_lados):
        tartaruga.fd(tamanho)
        t2.fd(tamanho)
        tartaruga.lt(angle)
        t2.lt(angle)


print(math.sqrt(4))
p(bob, bib, 8, 15)
polygon(bob, 60, 5)
polygon(bob, 360, 1)

turtle.mainloop()
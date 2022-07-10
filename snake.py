from re import S
import turtle 
import time
import random

posponer = 0.1

score = 0
high_score = 0
#configuracion ventana 
ventana_grafica = turtle.Screen()
ventana_grafica.title('Snake Game')
ventana_grafica.bgcolor('black')
#configura en ancho y alto de la ventana 
ventana_grafica.setup(width=600, height = 600)
ventana_grafica.tracer(0)
#cabeza de la serpiente 
cabeza = turtle.Turtle()
cabeza.speed(0)
#forma de la canbeza
cabeza.shape('circle')
#elimina el rastro de la serpiente para que no se muestre en pantalla 
cabeza.penup()
#la posicion desde donde queremos que inicie la serpiente 
cabeza.goto(0,0)
cabeza.color('white')
cabeza.direction = 'stop'


#comida 
comida = turtle.Turtle()
comida.speed(0)
comida.shape('square')
comida.penup()
comida.goto(0,100)
comida.color('red')

#cuerpo de la serpiente
segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('score: 0                      Higth Score: 0', align='center',font=('curier',15,'normal'))
#funciones 

#funciones de direccion 
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def derecha():
    cabeza.direction = 'right'
def izquierda():
    cabeza.direction = 'left'

#funcion demovimiento 
def movimiento ():
    if cabeza.direction == 'up': 
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#teclado 
ventana_grafica.listen()
ventana_grafica.onkeypress(arriba,'Up')
ventana_grafica.onkeypress(abajo,'Down')
ventana_grafica.onkeypress(izquierda,'Left')
ventana_grafica.onkeypress(derecha,'Right')


while True:
    ventana_grafica.update()
    if cabeza.xcor() > 280  or cabeza.ycor() > 280 or cabeza.xcor() < -280  or cabeza.ycor() <  -290 :
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'
        #esconder 
        for segmento in segmentos:
            segmento.goto(1000,1000)
        #limpiar segmentos 
        segmentos.clear()
        #resetear marcador 
        score = 0
        texto.clear()
        texto.write('score: {}                      Higth Score: {}'.format(score , high_score), align='center',font=('curier',15,'normal'))
        
    #colisiones comida
    if cabeza.distance(comida) < 20:
        xc= random.randint(-280, 280)
        yc = random.randint(-280, 280)
        comida.goto(xc,yc)
        #crear el segmento nuevo
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.penup()
        nuevo_segmento.shape('circle')
        nuevo_segmento.color('grey')
        segmentos.append(nuevo_segmento)
        

        score += 10 

        if score > high_score:
            high_score = score
        texto.clear()
        texto.write('score: {}                      Higth Score: {}'.format(score , high_score), align='center',font=('curier',15,'normal'))
    #mover el cuerpo de la serpeinte 
    totalseg = len(segmentos)
    for i in range(totalseg - 1, 0,-1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x,y)
    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    movimiento()

    # colisiones con el cuerpo

    for seg in segmentos:
        if seg.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = 'stop'
            for sig in segmentos:
                sig.goto(1000,10000)
            segmentos.clear()
            score = 0
            texto.clear()
            texto.write('score: {}                      Higth Score: {}'.format(score , high_score), align='center',font=('curier',15,'normal'))

    time.sleep(posponer)

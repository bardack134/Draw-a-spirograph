# Importa las clases Turtle y Screen, y las funciones forward, onkeypress y setheading del módulo turtle
from turtle import Turtle, Screen, forward, onkeypress, setheading

# Importa el módulo random para generar números aleatorios
import random



#TODO:random color
# Esta función cambia el color de una tortuga de forma aleatoria
def change_color(turtle):
    
    # Genera un número aleatorio entre 0 y 1 para la componente roja del color
    R=random.random()   
    
    # Genera un número aleatorio entre 0 y 1 para la componente azul del color
    B=random.random()
    
    # Genera un número aleatorio entre 0 y 1 para la componente verde del color
    G=random.random()
    
    # Asigna el color generado a la tortuga usando el método color
    turtle.color(R,G,B)
    
    

        


# Crea un objeto de la clase Turtle
turtle=Turtle()

# Aumenta la velocidad de la tortuga a la máxima posible
turtle.speed("fastest")

# Llama a la función change_color para cambiar el color de la tortuga
change_color(turtle)

# Crea un bucle que se repite 72 veces
for grades in range(0, 360, 5):
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(turtle)
    # Establece la orientación de la tortuga según el valor de la variable grades
    turtle.setheading(grades)
    # Dibuja un círculo de radio 100 con la tortuga
    turtle.circle(100)






# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Crea un objeto de la clase Screen
my_screen =Screen()


# Cierra la ventana al hacer click en la pantalla
my_screen.exitonclick()

inicio = 1
while inicio < 10:
    print("Juguemos al Mad Lib\nYo te haré una serie de preguntas y en base a tus respuestas, construiré una historia")
    nombre = input("¿Cómo te llamas?: ")
    edad = int(input("¿Qué edad tienes?: "))
    mascota = input("¿Qué nombre le pondrías a una mascota?: ")
    madre = input("¿Qué nombre tiene tu madre?: ")
    accion = input("¿Qué acción quieres realizar?: ")

# Comienzo de la historia 

    print("En el monte, " + nombre.capitalize(), "se avecina.")
    print("Es un humano de " + str(edad), "años, pero a nadie le interesa.")
    print("El único a quien le importa su existencia es a " + mascota.capitalize(), end=". ")
    print("Su madre, " + madre.capitalize(), "trabaja todos los días hasta altas horas de la noche. Esperando un futuro mejor.")
    print("Pero un día, " + nombre.capitalize(), "decide " + accion.lower(), "a todos en su aldea.")
    repetir = input("¿Quieres volver a jugar? (s/n): ")

if "s" in repetir:
    inicio = inicio + 1
elif "n" in repetir:
    inicio = inicio + 11 
# Método para ingresar la puntuación y el comentario
def ingresar_puntuacion_comentario():
    """
    Solicita al usuario una puntuación entre 1 y 5 y un comentario.
    Luego, guarda ambos en un archivo de texto.
    """
    while True:
        # Se solicita al usuario que ingrese una puntuación entre 1 y 5
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()

        # Verificamos si la entrada es un número
        if point.isdecimal():
            point = int(point)
            # Validamos que el número esté entre 1 y 5
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                # Si el número es válido, se solicita un comentario
                print('Por favor, introduzca un comentario')
                comment = input()
                # Guardamos la puntuación y el comentario en un archivo
                post = f'Puntuación: {point}, Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')  # Guardamos los datos en una nueva línea
                break  # Salimos del bucle una vez que los datos se hayan ingresado correctamente
        else:
            # Si no se ingresa un número, se le pide al usuario que lo intente de nuevo
            print('Por favor, introduzca la puntuación en números')

# Método para mostrar los resultados almacenados hasta el momento
def mostrar_resultados():
    """
    Lee y muestra el contenido del archivo de texto que almacena las puntuaciones y comentarios.
    """
    print('Resultados hasta la fecha:')
    try:
        # Intentamos abrir el archivo y leer su contenido
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print("Aún no se han registrado puntuaciones ni comentarios.")
    except FileNotFoundError:
        # Si el archivo no existe, mostramos un mensaje indicando que no hay datos
        print("Aún no se han registrado puntuaciones ni comentarios.")

# Método para finalizar el programa
def mostrar_mensaje_final():
    """
    Muestra un mensaje indicando que el programa ha finalizado.
    """
    print('Finalizando...')

# Método principal que controla el menú del programa
def menu_principal():
    """
    Muestra el menú principal del programa y permite al usuario seleccionar entre las opciones:
    1. Ingresar puntuación y comentario.
    2. Ver los resultados almacenados.
    3. Finalizar el programa.
    """
    while True:
        # Mostramos las opciones del menú al usuario
        print('Seleccione el proceso que desea aplicar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')

        # Recibimos la entrada del usuario
        num = input()

        # Verificamos que la entrada sea un número válido
        if num.isdecimal():
            num = int(num)
            if num == 1:
                # Llamamos al método para ingresar puntuación y comentario
                ingresar_puntuacion_comentario()
            elif num == 2:
                # Llamamos al método para mostrar los resultados almacenados
                mostrar_resultados()
            elif num == 3:
                # Llamamos al método para finalizar el programa
                mostrar_mensaje_final()
                break  # Salimos del bucle y finalizamos el programa
            else:
                # Si el número ingresado no está entre 1 y 3, se muestra un mensaje de error
                print('Por favor, introduzca un número del 1 al 3')
        else:
            # Si el usuario no ingresa un número, se le pide que lo intente de nuevo
            print('Por favor, introduzca un número del 1 al 3')

# Ejecutar el menú principal para iniciar el programa
menu_principal()
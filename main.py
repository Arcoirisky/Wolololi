from Tarea_1 import *
from random import randint

root = tk.Tk()
root.geometry('{}x{}'.format("550", "650"))
app = Application(master=root)


def Numero_segun_columna(col):
    if col == 0:
        numero = randint(0, 20)
    elif col == 1:
        numero = randint(21, 40)
    elif col == 2:
        numero = randint(41, 60)
    elif col == 3:
        numero = randint(61, 80)
    else:
        numero = randint(81, 100)
    return numero


def Forma_tableros_desde_cero():
    jug = 1
    while jug <= 2:
        for i in range(5):
            for j in range(5):
                numero_puesto = False
                while not numero_puesto:
                    numero = Numero_segun_columna(j)
                    if app.agregar(numero):
                        app.colocar_numero(i, j, numero, jug)
                        numero_puesto = True
        jug += 1
    app.reiniciar_contador()  # Esto es para que se borre el contador y que
    # funcione la tombola :D


def Tombola_dice():  # Esto simula un número de la tombola
    numero_puesto = False
    while not numero_puesto:
        numero = randint(0, 100)
        if app.agregar(numero):
            return numero


def Apuesta_entre_todos():
    j1 = app.preguntar_monto(1)
    j2 = app.preguntar_monto(2)
    if j1 > j2:
        apuesta = int(input("""
        ¿Cuanto dinero vais a apostar?
        [hasta {}]
        See... Todo por tí jugador 2 :T Así que ¡¡apuestenlo todo!!
        """.format(j2)))
        return apuesta
    else:
        apuesta = int(input("""
    	¿Cuanto dinero vais a apostar?
        [hasta {}]
    	See... Todo por tí jugador 1 :O Así que ¡¡apuestenlo todo!!
    	""".format(j1)))
        return apuesta


def Actualizar_dineros(saldo1, saldo2):
    app.mostrar_dinero(1, saldo1)
    app.mostrar_dinero(2, saldo2)


def Buscar_Numero(numero):
    for i in range(5):
        for j in range(5):
            if numero == app.obtener_numero(i, j, 1):
                app.marcar_numero(i, j, True, 1)
            if numero == app.obtener_numero(i, j, 2):
                app.marcar_numero(i, j, True, 2)


def Hay_Ganador():
    diag1 = True
    for i in range(5):
        for j in range(5):
            if i == j:
                if app.esta_marcado(i, j, 1) == False:
                    diag1 = False
                    break

    diag2 = True
    for i in range(5):
        for j in range(5):
            if i == j:
                if app.esta_marcado(i, j, 2) == False:
                    diag2 = False
                    break

    y1 = True
    for i in range(5):
        for j in range(5):
            if i == j:
                if app.esta_marcado(i, j, 1) == False:
                    y1 = False
                    break
            if j == 4 and i == 0:
                if app.esta_marcado(i, j, 1) == False:
                    y1 = False
                    break
            if j == 3 and i == 1:
                if app.esta_marcado(i, j, 1) == False:
                    y1 = False
                    break
            if j == 3 and i == 2:
                if app.esta_marcado(i, j, 1) == False:
                    y1 = False
                    break
            if j == 4 and i == 2:
                if app.esta_marcado(i, j, 1) == False:
                    y1 = False
                    break

    y2 = True
    for i in range(5):
        for j in range(5):
            if i == j:
                if app.esta_marcado(i, j, 2) == False:
                    y2 = False
                    break
            if j == 4 and i == 0:
                if app.esta_marcado(i, j, 2) == False:
                    y2 = False
                    break
            if j == 3 and i == 1:
                if app.esta_marcado(i, j, 2) == False:
                    y2 = False
                    break
            if j == 3 and i == 2:
                if app.esta_marcado(i, j, 2) == False:
                    y2 = False
                    break
            if j == 4 and i == 2:
                if app.esta_marcado(i, j, 2) == False:
                    y2 = False
                    break

    ent1 = True
    for i in range(5):
        for j in range(5):
            if app.esta_marcado(i,j,1) == False:
                ent1 = False
                break

    ent2 = True
    for i in range(5):
        for j in range(5):
            if app.esta_marcado(i,j,2) == False:
                ent2 = False
                break

    if ent1 == True and ent2 == False:
        return 1
    elif ent2 == True and ent1 == False:
        return 2
    elif ent1 == ent2 and ent1 != False:
        return 3

    elif y1 == True and y2 == False:
        return 1
    elif y2 == True and y1 == False:
        return 2
    elif y1 == y2 and ent1 != False:
        return 3

    elif diag1 == True and diag2 == False:
        return 1
    elif diag2 == True and diag1 == False:
        return 2
    elif diag1 == diag2 and ent1 != False:
        return 3

    else:
        return 0


def Pueden_continuar():
    d1 = app.preguntar_monto(1)
    d2 = app.preguntar_monto(2)
    if d1 <= 0 or d2 <= 0:
        return False
    else:
        return True


def Procramar_y_ajustar_cuentas(gana):
    app.mostrar_ventana(False)
    costo = app.obtener_apuesta()
    d1 = app.preguntar_monto(1)
    d2 = app.preguntar_monto(2)
    if gana == 1:
        print("""MIRA TUUUUUU...
            Jugador {}
            ¡¡¡eres el ganador!!!
            Felicidades por tu ganancia de {}
            """.format(gana, costo))
        app.mostrar_dinero(1, d1 - costo)
        app.mostrar_dinero(2, d2 + costo)
    elif gana == 0:
        print("EMPATEEEEEEEEEEEEEEE YAAAAY")

    else:
        print("""MIRA TUUUUUU...
            Jugador {}
            ¡¡¡eres el ganador!!!
            Felicidades por tu ganancia de {}
            """.format(gana, costo))
        app.mostrar_dinero(1, d1 + costo)
        app.mostrar_dinero(2, d2 - costo)

    if Pueden_continuar():
        cont = input("¿Desean continuar? [Si/No]")
        if cont == "Si":
            app.mostrar_ventana(True)
        else:
            app.cerrar_ventana()
            print("ADIOOOS")
    else:
        app.cerrar_ventana()
        print("Se acabó el dinero de las apuestas :( Nos vemos")


def turno():
    dice = Tombola_dice()
    app.mostrar_mensaje("Tombola dice: {}".format(dice))
    Buscar_Numero(dice)
    gana = Hay_Ganador()
    if gana != 0:
        if gana == 3:
            app.mostrar_mensaje("¡EMPATE!")
            Procramar_y_ajustar_cuentas(0)
        elif gana == 1:
            app.mostrar_mensaje("GANA JUGADOR 1")
            Procramar_y_ajustar_cuentas(1)
        else:
            app.mostrar_mensaje("GANA JUGADOR 2")
            Procramar_y_ajustar_cuentas(2)


app.mostrar_ventana(False)
print(""" ¡¡BIENVENIDO USUARIO!!

¡TE PRESENTO NUESTRO PRINGO!

[Ya sabes... Progra + Bingo, lo sé, estamos despiediendo al
creador del nombre pero los derechos no nos da para más :(]
""")

inicio = input("¿Deseas empezar ya el juego? [Si/No]\n --> ")
if inicio == "Si":
    print(""" COOL
    Pero, primero lo primero, no estamos aquí simplemente para jugar
    y lo sabes bien ;D
    Así queeee...
    """)
    saldo1 = int(input("¿Cuánto deseas jugar Jugador 1?\n --> "))
    saldo2 = int(input("¿Y Tú, Jugador 2?\n --> "))
    print("""    Perfecto <3

    Dame unos segundos que cargo la consola :D

            **** L O A D I N G ***
    """)
    Actualizar_dineros(saldo1, saldo2)
    Forma_tableros_desde_cero()
    print(""" \n\n\nUPS
    Olvidé preguntar algo importante
    """)
    apuesta = Apuesta_entre_todos()
    app.poner_apuesta(apuesta)
    app.mostrar_ventana(True)
    app.mostrar_mensaje("Click en 'Siguiente' para aceptar"
                        " la apuesta de {}".format(apuesta))


# ESTO NO SE TOCA
app.button.config(command=turno)
app.mainloop()

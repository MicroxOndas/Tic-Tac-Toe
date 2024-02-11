import random
def menu():
    print('🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩')
    print('🟩 #️⃣  🆒  🆒  Bienvenido a super tic tac toe  🆒  🆒  #️⃣  🟥')
    print('🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩 🟥 🟩')
    input('pulsa enter para comenzar...')

    print()
    print('Player 1: ')
    name_1 = input('Nombre: ')
    low_totem_1 = input('Con que totem juegas? (tableros locales): ')
    high_totem_1 = input('Con que SUPERtotem juegas? (tableros global): ')
    print('Jugador registrado como: \n' f'{name_1} \n' f'{low_totem_1} \n' f'{high_totem_1}')
    print()
    print('Player 2: ')
    name_2 = input('Nombre: ')
    low_totem_2 = input('Con que totem juegas? (tableros locales): ')
    high_totem_2 = input('Con que SUPERtotem juegas? (tableros global): ')
    print('Jugador registrado como: \n' f'{name_2} \n' f'{low_totem_2} \n' f'{high_totem_2}')

    return (name_1,name_2),(low_totem_1,low_totem_2),(high_totem_1,high_totem_2)

def leer_entero(msg,max):
    invalido = True
    while invalido:
        try:
            valor = int(input(msg))
        except:
            print('Entrada invalida')
        else:
            if  0 <= valor <= max: invalido = False
    return valor

def crear_tablero(ancho=3,largo=3):
    tablero = list()
    for fila_1 in range(largo):
        tablero.append([])
        for columna_1 in range(ancho):
            tablero[fila_1].append([])
            for fila_2 in range(largo):
                tablero[fila_1][columna_1].append([])
                for columna_2 in range(ancho):
                    tablero[fila_1][columna_1][fila_2].append([None])
    return tablero

def crear_senuelo(ancho=3,largo=3):
    matriz_senuelo = []
    for i in range(ancho):
        matriz_senuelo.append([])
        for j in range(largo):
            matriz_senuelo[i].append([None])
    return matriz_senuelo

def remplazar_none(x,y):
    if x[0]=='':
        x[0] = '🟢'
    if x[1]=='':
        x[1] = '🔴'
    if y[0]=='':
        y[0] = '🟩'
    if y[1]=='':
        y[1] = '🟥'
    return x,y

def hay_sitio(matriz,destino):
    if [None] == matriz[destino[0]][destino[1]]: return True
    else: return False

def matriz_display(matriz,destino):
    if destino != 'any' and not hay_sitio(matriz_global,destino):
        destino = 'any'
    print('--------------------------------------')
    morado = 0
    for _ in range(3):
        naranja = 0
        for _ in range(3):
            azul = 0
            for _ in range(3):
                print(' | ',end = '')
                for verde in matriz[morado][azul][naranja]:
                    if verde[0] == 0: ficha = jugadores[0]['Totem_l']
                    elif verde[0] == 1: ficha = jugadores[1]['Totem_l']
                    elif verde[0] == 2: ficha = jugadores[0]['Totem_h']
                    elif verde[0] == 3: ficha = jugadores[1]['Totem_h']
                    else: 
                        if (morado,azul) == destino:
                            ficha = '🔳'
                        elif destino == 'any':
                            ficha = '🔳'
                        else: ficha = '⬛'
                    print(ficha, end = ' ')
                azul += 1
            print(' | ',end = ' ')
            naranja += 1
            print()
        morado += 1
        print('---------------------------------------')
    print('---------------------------------------')
    for i in matriz_global:
        print(' | ',end = '')
        for j in i: 
            if j[0] == 0: a = jugadores[0]['Totem_h']
            if j[0] == 1: a = jugadores[1]['Totem_h']
            else: a = '⬛'
            print(a, end = ' ')
    print(' | ')
    print('---------------------------------------')

def posicion_invalida(ficha_fila_tablero,ficha_columna_tablero,ficha_fila,ficha_columna):
    if matriz[ficha_fila_tablero][ficha_columna_tablero][ficha_fila][ficha_columna] == [None]:
        return False
    else: 
        print('Posición invalida')
        return True

def colocar_ficha(ficha,destino):
    print()
    print(f'Puedes colocar en {destino}')
    print()
    invalido = True
    if destino != 'any' and not hay_sitio(matriz_global,destino):
        destino = 'any'
    if destino == 'any' or [1] == matriz_global[destino[0]][destino[1]] or [0] in matriz_global[destino[0]][destino[1]]:
        while invalido:
            ficha_fila_tablero = leer_entero('Elige las coords fila tablero: ',2)
            ficha_columna_tablero = leer_entero('Elige las coords columna tablero: ',2)
            ficha_fila = leer_entero('Elige las coords fila: ',2)
            ficha_columna = leer_entero('Elige las coords columna: ',2)
            invalido = posicion_invalida(ficha_fila_tablero,ficha_columna_tablero,ficha_fila,ficha_columna)
        destino = (ficha_fila_tablero,ficha_columna_tablero)
        matriz[ficha_fila_tablero][ficha_columna_tablero][ficha_fila][ficha_columna] = [ficha]
    else:
        while invalido:
            ficha_fila = leer_entero('Elige las coords fila: ',2)
            ficha_columna = leer_entero('Elige las coords columna: ',2)
            invalido = posicion_invalida(destino[0],destino[1],ficha_fila,ficha_columna)
        matriz[destino[0]][destino[1]][ficha_fila][ficha_columna] = [ficha]

    resultado = tres_en_raya(matriz[destino[0]][destino[1]])
    if resultado:
        print(f'EL JUGADOR {ficha + 1} HACE TRES EN RAYA LOCAL')
        matriz_global[destino[0]][destino[1]] = [resultado[0]]
        rellenar_tablero(matriz[destino[0]][destino[1]],ficha)
        print(resultado)
    
    resultado = tres_en_raya(matriz_global)
    if resultado:
        print(f'EL JUGADOR {ficha + 1} HACE TRES EN RAYA GLOBAL')
        print(resultado)
        print()
        print(f'Ganador, {jugadores[ficha]["Player"]}')
        matriz_display(matriz)
        return (ficha_fila,ficha_columna),False,ficha


    return (ficha_fila,ficha_columna),True,ficha

def tres_en_raya(matriz):
    # Rojo
    if matriz[0][0][0] != None and matriz[0][0][0] == matriz[0][1][0] == matriz[0][2][0]: return matriz[0][0][0],'línea horizontal'
    if matriz[1][0][0] != None and matriz[1][0][0] == matriz[1][1][0] == matriz[1][2][0]: return matriz[1][0][0],'línea horizontal'
    if matriz[2][0][0] != None and matriz[2][0][0] == matriz[2][1][0] == matriz[2][2][0]: return matriz[2][0][0],'línea horizontal'

    if matriz[0][0][0] != None and matriz[0][0][0] == matriz[1][0][0] == matriz[2][0][0]: return matriz[0][0][0],'línea vertical'
    if matriz[0][1][0] != None and matriz[0][1][0] == matriz[1][1][0] == matriz[2][1][0]: return matriz[0][1][0],'línea vertical'
    if matriz[0][2][0] != None and matriz[0][2][0] == matriz[1][2][0] == matriz[2][2][0]: return matriz[0][2][0],'línea vertical'

    if matriz[2][0][0] != None and matriz[2][0][0] == matriz[1][1][0] == matriz[0][2][0]: return matriz[2][0][0],'línea diagonal'
    if matriz[0][0][0] != None and matriz[0][0][0] == matriz[1][1][0] == matriz[2][2][0]: return matriz[0][0][0],'línea diagonal'
    return False

def rellenar_tablero(matriz,ficha):
    if ficha%2 == 0: ficha = 2
    else: ficha = 3
    for fila in matriz:
        for columna in fila:
            columna[0] = ficha

# Setup program
matriz = crear_tablero()
matriz_global = crear_senuelo()
# Main
nombres,totems_l,totems_h = menu()
totems_l,totems_h = remplazar_none(list(totems_l),list(totems_h))
jugadores = [{'Player': nombres[0], 'Totem_l': totems_l[0], 'Totem_h':totems_h[0]},{'Player': nombres[1], 'Totem_l': totems_l[1], 'Totem_h':totems_h[1]}]
destino = 'any'
continuar = True
turnos = 0
while continuar:
    turnos += 1
    if turnos%2 == 0:
        print(f'Turno {turnos}, {jugadores[1]["Player"]}')
        ficha = 1
    else:
        print(f'Turno {turnos}, {jugadores[0]["Player"]}')
        ficha = 0
    matriz_display(matriz,destino)
    destino,continuar,ficha = colocar_ficha(ficha,destino)

matriz_test =                                                                               [
[
    [
            [[], [], []],
            [[], [], []], 
            [[], [], []]                                                                ],

    [                          [[], [], []], 
                               [[], [], []], 
                               [[], [], []]                                             ],

    [                                                   [[], [], []], 
                                                        [[], [], []], 
                                                        [[], [], []]
                                                                                        ]
],

[   [           [[], [], []], 
                [[], [], []], 
                [[], [], []]                                                            ],

    [                                  [[], [], []],                                
                                       [[], [], []], 
                                       [[], [], []]                                     ],

    [                                                          [[], [], []], 
                                                               [[], [], []], 
                                                               [[], [], []]
                                                                                        ]
],

[   [         [[], [], []], 
              [[], [], []], 
              [[], [], []]                                                              ],

    [                                  [[], [], []], 
                                       [[], [], []], 
                                       [[], [], []]                                     ],

    [                                                           [[], [], []], 
                                                                [[], [], []], 
                                                                [[], [], []]
                                                                                        ]
]
                                                                                            ]
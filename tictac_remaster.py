import pygame
import time
matriz_coords = (


    (
        (
            ((20,20), (100,20), (180,20)),
            ((20,100), (100,100), (180,100)), 
            ((20,180), (100,180), (180,180))
        ),
        (
                                                    ((320,20), (400,20), (480,20)),
                                                    ((320,100), (400,100), (480,100)),
                                                    ((320,180), (400,180), (480,180))
        ),
        (
                                                                                                ((620,20), (700,20), (780,20)),
                                                                                                ((620,100), (700,100), (780,100)),
                                                                                                ((620,180), (700,180), (780,180))
        )
    ),
    (
        (
            ((20,320), (100,320), (180,320)),
            ((20,400), (100,400), (180,400)),
            ((20,480), (100,480), (180,480))
        ),
        (
                                                    ((320,320), (400,320), (480,320)),
                                                    ((320,400), (400,400), (480,400)),
                                                    ((320,480), (400,480), (480,480))
        ),
        (
                                                                                                ((620,320), (700,320), (780,320)),
                                                                                                ((620,400), (700,400), (780,400)),
                                                                                                ((620,480), (700,480), (780,480))
        )
    ),
    (
        (
            ((20,620), (100,620), (180,620)),
            ((20,700), (100,700), (180,700)),
            ((20,780), (100,780), (180,780))
        ),
        (
                                                    ((320,620), (400,620), (480,620)),
                                                    ((320,700), (400,700), (480,700)),
                                                    ((320,780), (400,780), (480,780))
        ),
        (
                                                                                                ((620,620), (700,620), (780,620)),
                                                                                                ((620,700), (700,700), (780,700)),
                                                                                                ((620,780), (700,780), (780,780))
        )
    )
)

mini_matriz = (
    ((35,35),(70,35),(105,35)),
    ((35,70),(70,70),(105,70)),
    ((35,105),(70,105),(105,105))
)

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
                    if verde[0] == 0: ficha = jugadores['Totem_l_1']
                    elif verde[0] == 1: ficha = jugadores['Totem_l_2']
                    elif verde[0] == 2: ficha = jugadores['Totem_h_1']
                    elif verde[0] == 3: ficha = jugadores['Totem_h_2']
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
            else: a = j[0]
            print(a, end = ' ')
    print(' | ')
    print('---------------------------------------')

def posicion_invalida(ficha_fila_tablero,ficha_columna_tablero,ficha_fila,ficha_columna):
    if matriz_global[ficha_fila_tablero][ficha_columna_tablero] != [None]:
        # print('Posición invalida')
        consola_graphic('Posición invalida',extra=20)
        return True
    if matriz[ficha_fila_tablero][ficha_columna_tablero][ficha_fila][ficha_columna] == [None]:
        return False
    else: 
        # print('Posición invalida')
        consola_graphic('Posición invalida',extra=20)
        return True

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

def draw(matriz,matriz_global):
    for i in range(3):
        for j in range(3):
            if matriz_global[i][j] != [3] and matriz_global[i][j] != [2]:
                for k in range(3):
                    for l in range(3):
                        if matriz[i][j][k][l] != [0] and matriz[i][j][k][l] != [1]:
                            return False
    return True

def relleno(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] != [0] and matriz[i][j] != [1]:
                return False
    return True

# Setup program

matriz = crear_tablero()
matriz_global = crear_senuelo()

jugadores = {'Player_1': 'Player 1','Player_2': 'Player 2'}

blanco = (255,255,255)

destino = 'any'

pygame.display.init()
screen = pygame.display.set_mode((1500,1000))
pygame.display.set_caption('Super Tic Tac Toe')

fondo = pygame.image.load('static/tablero3.png')
fondo2 = pygame.image.load('static/tablero.jpg')
X = pygame.image.load('static/X.png')
O = pygame.image.load('static/O.png')
blurr = pygame.image.load('static/blurr.png')
blurrB = pygame.image.load('static/Blurr3.png')
blurrA = pygame.image.load('static/Blurr4.png')
blurrAz = pygame.image.load('static/Blurr5.png')

fondo = pygame.transform.scale(fondo,(1000,1000))
blurr = pygame.transform.scale(blurr,(75,75))
X = pygame.transform.scale(X,(75,75))
O = pygame.transform.scale(O,(75,75))

blurrB = pygame.transform.scale(blurrB,(291,291))
blurrA = pygame.transform.scale(blurrA,(291,291))
blurrAz = pygame.transform.scale(blurrAz,(291,291))
XB = pygame.transform.scale(X,(240,240))
OB = pygame.transform.scale(O,(240,240))

blurrM = pygame.transform.scale(blurr,(800,800))
XM = pygame.transform.scale(X,(840,840))
OM = pygame.transform.scale(O,(840,840))


#PYGAME
def dibujar_titulo(coords):
    color = ((255,0,0),(0,255,0))
    for i in range(15):
        pygame.draw.rect(screen,color[i%2],rect=pygame.Rect(coords[0] +90*i+25,coords[1],80,80),border_radius=8)
    for i in range(3):
        pygame.draw.rect(screen,color[i%2],rect=pygame.Rect(coords[0] +90*i+25,coords[1]+120,80,80),border_radius=8)
    i+=1
    escribir_texto('segoe semibold',100,blanco,(coords[0] +100*i+25,coords[1]+120),'  SUPER TIC-TAC-TOE   ') 
    for i in range(14,11,-1):
        pygame.draw.rect(screen,color[i%2],rect=pygame.Rect(coords[0] +90*i+25,coords[1]+120,80,80),border_radius=8)
    for i in range(15):
        pygame.draw.rect(screen,color[i%2],rect=pygame.Rect(coords[0] +90*i+25,coords[1]+240,80,80),border_radius=8)
    
    

def calcular_relativo(mousex,mousey):
    tablerox = mousex // 300
    tableroy = mousey // 300
    fila = ((mousex-20) % 300) // 80
    columna = ((mousey-20) % 300) // 80
    return tablerox,tableroy,fila,columna

def click_valido(mousex,mousey,destino,matriz_coords):
    consola_graphic(f'Solo puedes poner aquí uwu: {destino}',color=(255,255,255))
    if destino == 'any':
        for i in range(3):
            for j in range(3):
                if (matriz_coords[i][j][0][0][0] <= mousex <= matriz_coords[i][j][2][2][0] + 80) and (matriz_coords[i][j][0][0][1] <= mousey <= matriz_coords[i][j][2][2][1] + 80):
                    return True
    else:
        if (matriz_coords[destino[0]][destino[1]][0][0][0] <= mousex <= matriz_coords[destino[0]][destino[1]][2][2][0] + 80) and (matriz_coords[destino[0]][destino[1]][0][0][1] <= mousey <= matriz_coords[destino[0]][destino[1]][2][2][1] + 80):
            return True

def sumar_tupla(tupla,add):
    new_tuple = 'a',
    for element in tupla:
        element += add
        new_tuple += element,
    return new_tuple[1:]


def dibujar(imagen,coords):
    screen.blit(imagen,coords)

def graficar_tablero(fondo,X,O,matriz,destino):
    screen.blit(fondo,(0,0))
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for index,d in enumerate(matriz[a][b][c]):
                    if d[0] == 0: dibujar(X,sumar_tupla(matriz_coords[a][b][c][index],63))
                    elif d[0] == 1: dibujar(O,sumar_tupla(matriz_coords[a][b][c][index],63))
                    if destino == 'any':
                        if d[0] == None: dibujar(blurr,sumar_tupla(matriz_coords[a][b][c][index],63))
                    if (a,b) == destino:
                        if d[0] == None: dibujar(blurr,sumar_tupla(matriz_coords[a][b][c][index],63))
                        

def graficar_tablero_global(X,O,matriz):
    for a in range(3):
        for index,b in enumerate(matriz[a]):
            if b[0] == 2: 
                dibujar(blurrB,sumar_tupla(matriz_coords[a][index][0][0],35))
                dibujar(X,sumar_tupla(matriz_coords[a][index][0][0],63))
            elif b[0] == 3:
                dibujar(blurrAz,sumar_tupla(matriz_coords[a][index][0][0],35))
                dibujar(O,sumar_tupla(matriz_coords[a][index][0][0],63))
            elif b[0] == -1:
                dibujar(blurrA,sumar_tupla(matriz_coords[a][index][0][0],35))
                
def escribir_texto(fuente,tamaño,color,coords,msg):
    pygame.init()
    font = pygame.font.SysFont(fuente,tamaño)
    texto = font.render(msg,True,color)
    screen.blit(texto, coords)

def consola_graphic(msg,extra=0,fuente='segoe semibold',tamaño=25,color=blanco,pos = 1000):
    pygame.init()
    font = pygame.font.SysFont(fuente,tamaño)
    texto = font.render(msg,True,color)
    screen.blit(texto,(pos+50,extra+600))

def graphic_menu(pos,jugadores,turno,destino):
    screen.fill((15,14,23))
    escribir_texto('segoe semibold',65,blanco,(pos+25,10),'SUPER TIC TAC TOE')
    pygame.draw.line(screen, blanco, (pos+25,60), (pos+462,60), 5)

    s1 = 50
    escribir_texto('segoe semibold',40,blanco,(pos+50,s1+70),jugadores['Player_1'])
    dibujar(pygame.transform.scale(X,(50,50)),(pos+50,s1+100))
    escribir_texto('segoe semibold',40,blanco,(pos+50,s1+170),jugadores['Player_2'])
    dibujar(pygame.transform.scale(O,(50,50)),(pos+50,s1+200))
    t = 170
    if turno%2 != 0:
        escribir_texto('segoe semibold',40,blanco,(pos+250,s1+70),f'Turno {turno}')
    else:
        escribir_texto('segoe semibold',40,blanco,(pos+250,s1+70),f'Turno {turno}')
    dibujar(pygame.transform.scale(fondo2,(t,t)),(pos+250,s1+100))
    if destino !='any' and turno%2 != 0:
        dibujar(pygame.transform.scale(X,(t//3-10,t//3-10)),(192+pos+(t*(mini_matriz[destino[0]][destino[1]][0]/100)),92+t*(mini_matriz[destino[0]][destino[1]][1]/100)))
    elif destino !='any':
        dibujar(pygame.transform.scale(O,(t//3-10,t//3-10)),(192+pos+(t*(mini_matriz[destino[0]][destino[1]][0]/100)),92+t*(mini_matriz[destino[0]][destino[1]][1]/100))) 
    else:
        if turno%2 != 0:
            for i in range(3):
                for j in range(3):
                    dibujar(pygame.transform.scale(X,(t//3-10,t//3-10)),(192+pos+(t*(mini_matriz[i][j][0]/100)),92+t*(mini_matriz[i][j][1]/100)))
        else:
            for i in range(3):
                for j in range(3):
                    dibujar(pygame.transform.scale(O,(t//3-10,t//3-10)),(192+pos+(t*(mini_matriz[i][j][0]/100)),92+t*(mini_matriz[i][j][1]/100)))

    escribir_texto('segoe semibold',40,blanco,(pos+50,550),'Eventos')
    pygame.draw.line(screen, blanco, (pos+50,577), (pos+452,577), 5)



destino = 'any'
game_over = False
clock = pygame.time.Clock()
turno = 1

# graphic setup


menu_loop = True
text = ""
n = 1
while menu_loop:
    clock.tick(30)
    screen.fill((15,14,23))
    if n != 3:
        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                text += event.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                if event.key == pygame.K_RETURN:
                    jugadores[f'Player_{n}'] = text
                    text = ""
                    n+=1
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            dibujar_titulo((50,20)) 
            escribir_texto('segoe semibold',150,blanco,(500-len(text)*30,450),f'Player {n}: {text}')        
            pygame.display.update()
    else:
        screen.fill((15,14,23))
        dibujar_titulo((50,20))
        a = 275
        b = 500
        wd = 950
        hg = 300
        pygame.draw.rect(screen,(255,0,0),rect=pygame.Rect(a,b,wd,hg),border_radius=60)
        escribir_texto('segoe semibold',150,blanco,(a+(wd/2)-125,b+(hg/2)-50),f'Start')
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex , mousey = event.pos
                if (a <= mousex <= a+wd) and (b <= mousey <= b+hg):
                    menu_loop = False
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
        pygame.display.update()

if jugadores['Player_1'] == "": jugadores['Player_1'] = "Player 1"
if jugadores['Player_2'] == "": jugadores['Player_2'] = "Player 2"

jugadores['Totem_l_1'] = '🟢'
jugadores['Totem_l_2'] = '🔴'
jugadores['Totem_h_1'] = '🟩'
jugadores['Totem_h_2'] = '🟥'

graphic_menu(1000,jugadores,turno,destino)
graficar_tablero(fondo,X,O,matriz,destino)

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex , mousey = event.pos
            if click_valido(mousex-63,mousey-63,destino,matriz_coords):
                tablerox,tableroy,fila,columna = calcular_relativo(mousex-63,mousey-63)
                if not posicion_invalida(tableroy,tablerox,columna,fila):
                    turno += 1
                    if turno%2 != 0:
                        # print(f'Turno {turno}, {jugadores["Player_2"]}')
                        consola_graphic(f'Turno {turno}, {jugadores["Player_2"]}')
                        ficha = (1,3)
                    else:
                        # print(f'Turno {turno}, {jugadores["Player_1"]}')
                        consola_graphic(f'Turno {turno}, {jugadores["Player_1"]}')
                        
                        ficha = (0,2)  
                    matriz[tableroy][tablerox][columna][fila] = [ficha[0]]
                    local = tres_en_raya(matriz[tableroy][tablerox])

                    if relleno(matriz[tableroy][tablerox]):
                        matriz_global[tableroy][tablerox] = [-1]
                        
                    if local:
                        matriz_global[tableroy][tablerox] = [ficha[1]]
                    if matriz_global[columna][fila] !=[None]: destino = 'any'
                    else: destino = columna,fila
                    
                    if draw(matriz,matriz_global):
                        turno = -1
                        game_over = True
                    graphic_menu(1000,jugadores,turno,destino)
                    # matriz_display(matriz,destino)
                    graficar_tablero(fondo,X,O,matriz,destino)
                    graficar_tablero_global(XB,OB,matriz_global)
                    
                    glob = tres_en_raya(matriz_global)
                    if turno%2 != 0:
                        consola_graphic((f'{jugadores["Player_1"]} puede colocar en: {destino}'),-200,tamaño=30)
                    else:
                        consola_graphic((f'{jugadores["Player_2"]} puede colocar en: {destino}'),-200,tamaño=30)
                    t = 20    
                    if glob:
                        if turno%2 != 0:
                            consola_graphic(f'{jugadores["Player_2"].upper()} HACE TRES EN RAYA GLOBAL',t)
                            consola_graphic(f'Debido a: {glob[-1]}',20+t)
                        else:
                            consola_graphic(f'{jugadores["Player_1"].upper()} HACE TRES EN RAYA GLOBAL',t)
                            consola_graphic(f'Debido a: {glob[-1]}',20+t)
                        images = (XM,OM)
                        coords = ((73,83),(83,83))
                        dibujar(images[ficha[0]],coords[ficha[0]])
                        game_over = True
                    else:
                        if local:
                            if turno%2 != 0:
                                consola_graphic(f'{jugadores["Player_2"].upper()} HACE TRES EN RAYA LOCAL',t)
                                consola_graphic(f'Debido a: {local[-1]}',20+t)
                            else:
                                consola_graphic(f'{jugadores["Player_1"].upper()} HACE TRES EN RAYA LOCAL',t)
                                consola_graphic(f'Debido a: {local[-1]}',20+t)
    pygame.display.update()
pygame.draw.rect(screen,(15,14,23),pygame.Rect(0,356,1000,290),border_radius=30)    # (220,360,560,270)

if turno < 0: pygame.draw.rect(screen,(255,255,0),pygame.Rect(170,410,650,170),border_radius=30)
elif turno%2 != 0: pygame.draw.rect(screen,(50,20,235),pygame.Rect(170,410,650,170),border_radius=30)
else: pygame.draw.rect(screen,(255,20,50),pygame.Rect(170,410,650,170),border_radius=30)

if turno < 0:
    escribir_texto('segoe semibold',90,(0,0,0),(320,425),'Bien jugado.')
    escribir_texto('segoe semibold',90,(0,0,0),(275,500),'Empate táctico')
elif turno%2 != 0:
    escribir_texto('segoe semibold',90,blanco,(340,445),f'{jugadores["Player_2"].upper()}')
    escribir_texto('segoe semibold',90,blanco,(375,500),'wins =D')
else:
    escribir_texto('segoe semibold',90,blanco,(340,445),f'{jugadores["Player_1"].upper()}')
    escribir_texto('segoe semibold',90,blanco,(375,500),'wins B)')

pygame.display.update()
loop = True
while loop:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen = pygame.display.set_mode((500,250))
                loop = False
                screen.fill((15,14,23))
                escribir_texto('segoe semibold',60,blanco,(20,80),'Gracias por jugar <3')
                escribir_texto('segoe semibold',60,blanco,(25,130),'- MicroxOndas')
                pygame.display.update()
                time.sleep(0.5)
print('Gracias por jugar :D')
print('- MicroxOndas')
pygame.quit()
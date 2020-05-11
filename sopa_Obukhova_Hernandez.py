import random
from random import randrange

def tablero_vacio(ancho,alto):
    '''Dado dos números, devuelve un tablero con el alto y el ancho de los números.
    Recibe dos números y devuelve una lista de listas de strings
    tablero_vacio: Number, Number -> Lista de listas'''
    tablero=[]
    for i in range(alto):
        fila = []
        for j in range(ancho):
            fila.append(' ')
        tablero.append(fila)
    return tablero

def test_tablero_vacio():
    '''Función que testea a la función tablero_vacio()'''
    assert tablero_vacio(2,2) == [[' ',' '],[' ',' ']]
    assert tablero_vacio(5,2) == [[' ',' '],[' ',' '],[' ',' '],[' ',' '],[' ',' ']]

def palabra_larga(lista_palabras):
    '''Dada una lista de palabras, devuelve aquella con la mayor cantidad
    de letras.
    palabra_larga: Lista de Strings -> String
    Recibe una lista de strings que representan las palabras y devuelve un string
    que representa la palabra más larga de la lista.
    Si la lista que recibe es una lista vacía no devuelve nada. '''

    LARGO_SOPA = len(lista_palabras)
    p = ''  #palabra
    i = 0   #indice de la palabra en la lista
    while i < LARGO_SOPA:
        LARGO_PALABRA = len(lista_palabras[i])
        if len(p) < LARGO_PALABRA:
            p = lista_palabras[i]
            i += 1
        else:
            i += 1
    return p


def range_palabra(palabra, ancho, sentido):
    '''Dada una palabra, el ancho de la sopa y la dirección de la palabra,
    devuelve un intervalo en el cual es posible que empiece la palabra.
    range_palabra: String, Number, String -> Intervalo
    El string representa la palabra, el número el ancho de la sopa y el
    String representa la dirección de la palabra. '''
    
    if sentido == 'normal':
        return (0, ancho - len(palabra) + 1)
    if sentido == 'anti-normal':
        return (len(palabra) - 1, ancho + 1)

def test_range_palabra():
    '''Función que testea a range_palabra()'''
    assert range_palabra('hola',7, 'normal') == (0, 2)
    assert range_palabra('chinchulin', 25, 'anti-normal') == (9, 25)
    
       

def mayusculas(lista_palabras):
    '''Recibe una lista de palabras y devuelve una lista de palabras en mayúscula.
    La lista de palabras es representanda por una Lista de Strings.
    mayusculas: Lista de Strings -> Lista de Strings'''
    for i in range(len(lista_palabras)):
        palabra = lista_palabras[i]
        lista_palabras[i] =  palabra.upper()
    return lista_palabras

def test_mayusculas():
    '''Función que testea a la función mayuscula()'''
    assert mayusculas(['hola','CHAU']) == ['HOLA','CHAU']
    assert mayusculas(['hOlA','ChAu']) == ['HOLA','CHAU']

def tablero_pantalla(sopa):
    ''' Recibe una sopa de letras y la imprime en pantalla.
    La sopa es representada como una lista de listas.
    tablero_pantalla: Lista de Listas -> None'''
    
    for fila in sopa:
        print('|', end = ' ')
        for columna in fila:
            print(columna,end= ' | ')
        print()

def chequear_palabra(sopa, palabra, c, f, s, direccion):
    '''Dada la sopa de palabras, la palabra que quiere verificar y la posición donde se quiere ubicar,
    verifica no haya otra letra de otra palabra ya puesta allí, y si lo hay, se fija si son iguales.
    Si son distintas, devuelve False y vuelve a seleccionar una posición. Si son iguales, devuelve True
    y continua con el proceso de ubicación.'''

    
    l = 0 #letra
    fila=f
    col=c
    LARGO_PALABRA = len(palabra)
    
    while l < LARGO_PALABRA and (sopa[fila][col] == ' ' or sopa[fila][col] == palabra[l]):
    
        if direccion == 'vertical':
            fila += s
            l += 1

        if direccion == 'horizontal':
            col += s
            l += 1
                
        if direccion == 'diagonal':
            col += s
            fila += s
            l += 1
                
        if direccion == 'anti-diagonal':
            col += s
            fila -= s
            l += 1

    if l == LARGO_PALABRA:
        return True
    else:
        return False


def rellenar_sopa(sopa):
    '''Dada una sopa de letras sin completar, devuelve
    una sopa de letras donde se reemplazó los espacios vacíos por letras
    aleatorias.
    Recibe una lista de listas de strings, que representan la sopa de letras
    sin rellenar, devuelve una lista de listas de strings, que representan
    la sopa de letras con las letras aleatorias.
    rellenar_sopa: Lista de Listas de Strings -> Lista de Listas de Strings'''

    abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    LARGO = len(sopa)
    for fila in range(LARGO):
        columna = 0
        while columna < LARGO:
            if sopa[fila][columna] == ' ':
                sopa[fila][columna] = random.choice(abecedario)
                columna += 1
            else:
                columna += 1
    return sopa

def ingresar_palabras():
    '''Función que recibe palabras mediantes un input y devuelve una lista con las palabras.
    Recibe strings que representan a las palabras y devuelve una lista de esos strings.
    ingresar_palabras: String1,String2, ... , StringX -> Lista de Strings'''
    lista=[]
    palabra = " "
    while palabra != "":
        palabra = input("Ingrese la palabra que quiera en la sopa de letras, cuando finalice precione enter: ")
        lista.append(palabra)
    return lista[:len(lista)-1]

def opcion_1():
    ''' Función que devuelve una sopa de letras.
    Si la lista está vacía devuelve un string informandolo.
    Recibe una lista de strings que representan las palabras que queremos en la
    sopa de letras.
    Devuelve una lista de listas que representa la sopa de letras.'''
    lista_palabras = ingresar_palabras()
    print(lista_palabras)
   
    
    if lista_palabras == []:
        print('La lista de palabras está vacía')
    else:
        ANCHO = ALTO = len(palabra_larga(lista_palabras))+5
        TAMAÑO = ANCHO * ALTO
        lista_palabras = mayusculas(lista_palabras)
        sopa = tablero_vacio(ANCHO, ALTO)
        i = 0 #indice que representa cada palabra de la lista
        
        while i < len(lista_palabras):
            
            
            l = 0 #índice de la letra de la palabra
            
            sentido = random.choice(['normal','anti-normal'])  #elije aleatoriamente un sentido
            direccion = random.choice(['horizontal','vertical','diagonal','anti-diagonal']) #elije aleatoriamente una dirección
            
            if sentido == 'normal':
                s = 1
            if sentido == 'anti-normal':
                s = -1
            
            if  direccion == 'vertical':
                tupla = range_palabra(lista_palabras[i], ALTO, sentido)
                f = randrange(tupla[0],tupla[1])
                c = randrange(ALTO)
                
                while not chequear_palabra(sopa, lista_palabras[i], c, f, s, direccion):
                    tupla = range_palabra(lista_palabras[i], ALTO, sentido)
                    f = randrange(tupla[0],tupla[1])
                    c = randrange(ANCHO)  


                while l < len(lista_palabras[i]):
                    sopa[f][c] = lista_palabras[i][l]
                    f += s
                    l += 1
                    
            if direccion == 'horizontal':
                tupla = range_palabra(lista_palabras[i], ANCHO, sentido)
                c = randrange(tupla[0],tupla[1])
                f = randrange(ALTO)
                
                while not chequear_palabra(sopa, lista_palabras[i], c, f, s, direccion):
                    tupla = range_palabra(lista_palabras[i], ANCHO, sentido)
                    c = randrange(tupla[0],tupla[1])
                    f = randrange(ALTO)
                    
                while l < len(lista_palabras[i]):
                    sopa[f][c] = lista_palabras[i][l]
                    c += s
                    l += 1
                  
            if direccion == 'diagonal':
                tupla = range_palabra(lista_palabras[i], ALTO, sentido)
                f = randrange(tupla[0],tupla[1])
                
                tupla = range_palabra(lista_palabras[i], ANCHO, sentido)
                c = randrange(tupla[0], tupla[1])
                
                while not chequear_palabra(sopa, lista_palabras[i], c, f, s, direccion):
                    tupla = range_palabra(lista_palabras[i], ALTO, sentido)
                    f = randrange(tupla[0],tupla[1])
                
                    tupla = range_palabra(lista_palabras[i], ANCHO, sentido)
                    c = randrange(tupla[0], tupla[1])
                
                while l < len(lista_palabras[i]):
                    sopa[f][c] = lista_palabras[i][l]
                    c += s
                    f += s
                    l += 1
                    
            if direccion == 'anti-diagonal':
                if sentido == 'normal':
                    tupla1 = range_palabra(lista_palabras[i], ANCHO, sentido)  #intervalo de valores que puede tomar c
                    tupla2 = range_palabra(lista_palabras[i], ALTO, 'anti-normal')   #intervalo de valores que puede tomar f
                else:
                    tupla1 = tupla = range_palabra(lista_palabras[i], ANCHO, sentido)  #intervalo de valores que puede tomar c
                    tupla2 = range_palabra(lista_palabras[i], ALTO, 'normal')  #intervalo de valores que puede tomar f
                
                c = randrange(tupla1[0],tupla1[1])  
                f = randrange(tupla2[0],tupla2[1])

                while not chequear_palabra(sopa, lista_palabras[i], c, f, s, direccion):
                    if sentido == 'normal':
                        tupla1 = range_palabra(lista_palabras[i], ALTO, sentido)
                        tupla2 = range_palabra(lista_palabras[i], ALTO, 'anti-normal')
                        
                    else:
                        tupla1 = range_palabra(lista_palabras[i], ALTO, sentido)
                        tupla2 = range_palabra(lista_palabras[i], ALTO, 'normal')
                    c = randrange(tupla1[0],tupla1[1])
                    f = randrange(tupla2[0],tupla2[1])
                    
                while l < len(lista_palabras[i]):
                    sopa[f][c] = lista_palabras[i][l]
                    c += s
                    f -= s
                    l += 1
                   

            i += 1
        rellenar_sopa(sopa)
        tablero_pantalla(sopa)
        return sopa


# revisar_palabra: lista de listas de Srings, String, Numero, String, String, Numero, Numero, Numero, Numero, Numero, Numero, Numero) -> Tupla (String, Numero, Numero, String, String)
# Es la función auxiliar que esta llamada dentro de funciones:
# buscar_horizontal
# buscar_vertical
# buscar_diagonal
# buscar_anti_diagonal
# La funcion toma como entrada sopa de letras representada por lista de listas, una palabra (String), longitud de palabra (Numero),
# dirección ("horizontal", "vertical", "diagonal" (String)), sentido ("normal", "anti-normal" (String)),
# columna y fila de inicio y los limites derecho y inferior, que nos permiten evitar que la función busca la palabra en filas y columnas donde la palabra no puede entrar)
# s (-1 o 1, depende del sentido de búsqueda),
# x, y - los steps que hacemos cuando buscamos letra por letra en la sopa. 
#
# La función devuelve tupla con palabra (String), fila y columna de la sopa donde esta la primera letra de la palabra (Numeros),
# direccion (String) y sentido (String).

def revisar_palabra(sopa, palabra, longitud_palabra, direccion, sentido, columna_inicio, fila_inicio,
                    limite_derecho, limite_inferior, s, x, y):
    resultado = (palabra, -1, -1, direccion, sentido)
    encontro_palabra = False
    c = columna_inicio
    f = fila_inicio
    while (not encontro_palabra) and f < limite_inferior:
        l = 0 #letra de palabra

        while l < longitud_palabra and palabra[l] == sopa[f+l*y*s][c+l*x*s]:
            l += 1

        if l == longitud_palabra:
            resultado = (palabra, f, c, direccion, sentido)
            encontro_palabra = True

        c += 1

        if c >= limite_derecho:
            c = columna_inicio
            f += 1

    return resultado

# buscar_horizontal: lista de listas de Srings, String, String, Numero, Numero, Numero -> Tupla (String, Numero, Numero, String, String)

# La funcion recibe sopa de letras representada por lista de listas, una palabra (String), sentido (String),
# ancho y alto de la sopa (Numeros) y longitud de palabra (Numero)
# y devuelve tupla con palabra (String), fila y columna de la sopa donde esta la primera letra de la palabra (Numeros),
# direccion (String "horizontal") y sentido (String 'normal'/'anti-normal).

# La funcion busca palabra en la sopa horizontalmente en dos sentidos: desde la izquierda hacia la derecha (sentido 'normal')
# y desde la derecha hacia la izquierda (sentido 'anti-normal')
# En el caso si la funcion no encuentra la palabra en la sopa horizontalmente, los valores de fila y columna en la tupla devuelta son -1. 

def buscar_horizontal(sopa, palabra, sentido, ANCHO, ALTO, longitud_palabra):
    x = 1 #step columna
    y = 0 #step fila
    if sentido == 'normal':
        s = 1 
        columna_inicio = 0
        limite_derecho = ANCHO - longitud_palabra + 1
    if sentido == 'anti-normal':
        s = -1
        columna_inicio = longitud_palabra-1
        limite_derecho = ANCHO
        
    limite_inferior = ALTO
    fila_inicio = 0           

    return revisar_palabra (sopa, palabra, longitud_palabra, 'horizontal', sentido, columna_inicio, fila_inicio,
                    limite_derecho, limite_inferior, s, x, y)


# función para testear la función buscar_horizontal. 
# En el caso si la función no devuelve el resultado esperado, aparece un AssertionError
# y el mensaje que el test esta fallando (ejemplo "Test 'test', horizontal, 'normal' failed")
# En el caso contrario, no devuelve nada.

def test_buscar_horizontal(): 
    assert buscar_horizontal([['q','e','s','s','e','s'],['t','e','s','t','e','w']], 'test', 'normal', 6, 2, 4) == ('test', 1, 0, 'horizontal', 'normal'), "Test 'test', horizontal, 'normal' failed"
    assert buscar_horizontal([['q','e','s','s','e','s'],['t','e','s','t','e','w']], 'test', 'anti-normal', 6, 2, 4) == ('test', -1, -1, 'horizontal', 'anti-normal'), "Test 'test', horizontal, 'anti-normal' failed"
    

# buscar_vertical: lista de listas de Srings, String, String, Numero, Numero, Numero -> Tupla (String, Numero, Numero, String, String)

# La funcion recibe sopa de letras representada por lista de listas, una palabra (String), sentido (String),
# ancho y alto de la sopa (Numeros) y longitud de palabra (Numero)
# y devuelve tupla con palabra (String), fila y columna de la sopa donde esta la primera letra de la palabra (Numeros),
# direccion (String "vertical") y sentido (String 'normal'/'anti-normal).

# La funcion busca palabra en la sopa verticalmente en dos sentidos: desde arriba hacia abajo (sentido 'normal')
# y desde abajo hacia arriba (sentido 'anti-normal')
# En el caso si la funcion no encuentra la palabra en la sopa verticalmente, los valores de fila y columna en la tupla devuelta son -1. 


def buscar_vertical(sopa, palabra, sentido, ANCHO, ALTO, longitud_palabra):
    x = 0 #step columna
    y = 1 #step fila 
    columna_inicio = 0 
    if sentido == 'normal':
        s = 1 
        fila_inicio = 0
        limite_inferior = ALTO - longitud_palabra + 1
    if sentido == 'anti-normal':
        s = -1
        fila_inicio = longitud_palabra-1
        limite_inferior = ALTO

    limite_derecho = ANCHO                   

    return revisar_palabra (sopa, palabra, longitud_palabra, "vertical", sentido, columna_inicio, fila_inicio,
                    limite_derecho, limite_inferior, s, x, y)


# función para testear la función buscar_vertical. 

def test_buscar_vertical():
    assert buscar_vertical([['q','e','s','s','e','s'],
        ['t','e','s','t','e','w'],
        ['f','l','s','t','e','t'],
        ['t','e','e','e','t','s'],
        ['w','t','t','s','e','t']], 'set', 'normal', 6, 5, 3) == ('set', 2, 2, 'vertical', 'normal'), "Test 'set', vertical, 'normal' failed"
    assert buscar_vertical([['q','e','s','s','e','s'],
        ['t','e','s','t','e','w'],
        ['f','l','s','t','e','t'],
        ['t','e','e','e','t','s'],
        ['w','t','t','s','e','t']], 'hola', 'normal', 6, 5, 3) == ('hola', -1, -1, 'vertical', 'normal'), "Test 'hola', vertical, 'normal' failed"
    assert buscar_vertical([['q','e','s','s','e','l'],
        ['t','e','s','t','e','l'],
        ['f','l','s','t','e','o'],
        ['t','e','e','e','t','r'],
        ['w','t','t','s','e','t']], 'roll', 'anti-normal', 6, 5, 3) == ('roll', 3, 5, 'vertical', 'anti-normal'), "Test 'roll', vertical, 'anti-normal' failed"
    

# buscar_diagonal: lista de listas de Srings, String, String, Numero, Numero, Numero -> Tupla (String, Numero, Numero, String, String)

# La funcion recibe sopa de letras representada por lista de listas, una palabra (String), sentido (String),
# ancho y alto de la sopa (Numeros) y longitud de palabra (Numero)
# y devuelve tupla con palabra (String), fila y columna de la sopa donde esta la primera letra de la palabra (Numeros),
# direccion (String "diagonal") y sentido (String 'normal'/'anti-normal).

# La funcion busca palabra en la sopa diagonalmente en dos sentidos: desde izquierda hacia derecha desde arriba hacia abajo (sentido 'normal')
# y desde derecha hacia izquierda desde abajo hacia arriba (sentido 'anti-normal')
# En el caso si la funcion no encuentra la palabra en la sopa diagonalmente, los valores de fila y columna en la tupla devuelta son -1. 


def buscar_diagonal(sopa, palabra, sentido, ANCHO, ALTO, longitud_palabra):
    x = 1
    y = 1
    if sentido == 'normal':
        s = 1
        columna_inicio = 0
        fila_inicio = 0
        limite_derecho = ANCHO - longitud_palabra + 1
        limite_inferior = ALTO - longitud_palabra + 1
    if sentido == 'anti-normal':
        s = -1
        columna_inicio = longitud_palabra-1
        fila_inicio = longitud_palabra-1
        limite_derecho = ANCHO
        limite_inferior = ALTO

    return revisar_palabra (sopa, palabra, longitud_palabra, "diagonal", sentido, columna_inicio, fila_inicio,
                    limite_derecho, limite_inferior, s, x, y)


# función para testear la función buscar_diagonal. 

def test_buscar_diagonal():
    assert buscar_diagonal([['p','e','s','s','e','s'],
        ['t','e','s','t','e','w'],
        ['f','l','s','t','e','t'],
        ['t','e','e','o','t','s'],
        ['w','t','t','s','e','t']], 'peso', 'normal', 6, 5, 4) == ('peso', 0, 0, 'diagonal', 'normal'), "Test 'peso', diagonal, 'normal' failed"
    assert buscar_diagonal([['q','e','s','s','e','s'],
        ['t','e','s','t','e','w'],
        ['f','l','l','t','e','t'],
        ['t','e','e','o','t','s'],
        ['w','t','t','s','s','t']], 'sol', 'anti-normal', 6, 5, 3) == ('sol', 4, 4, 'diagonal', 'anti-normal'), "Test 'sol', diagonal, 'anti-normal' failed"
    assert buscar_diagonal([['q','e','s','s','e','l'],
        ['t','e','s','t','e','l'],
        ['f','l','s','t','e','o'],
        ['t','e','e','e','t','r'],
        ['w','t','t','s','e','t']], 'ibiza', 'anti-normal', 6, 5, 5) == ('ibiza', -1, -1, 'diagonal', 'anti-normal'), "Test 'ibiza', diagonal, 'anti-normal' failed"    



# buscar_anti_diagonal: lista de listas de Srings, String, String, Numero, Numero, Numero -> Tupla (String, Numero, Numero, String, String)

# La funcion recibe sopa de letras representada por lista de listas, una palabra (String), sentido (String),
# ancho y alto de la sopa (Numeros) y longitud de palabra (Numero)
# y devuelve tupla con palabra (String), fila y columna de la sopa donde esta la primera letra de la palabra (Numeros),
# direccion (String "anti-diagonal") y sentido (String 'normal'/'anti-normal).

# La funcion busca palabra en la sopa diagonalmente en dos sentidos: desde derecha hacia izquierda desde arriba hacia abajo (sentido 'normal')
# y desde izquierda hacia derecha desde abajo hacia arriba (sentido 'anti-normal')
# En el caso si la funcion no encuentra la palabra en la sopa, los valores de fila y columna en la tupla devuelta son -1. 

def buscar_anti_diagonal(sopa, palabra, sentido, ANCHO, ALTO, longitud_palabra):
    x = -1
    y = 1
    if sentido == 'normal':
        s = 1
        columna_inicio = longitud_palabra - 1
        fila_inicio = 0
        limite_derecho = ANCHO
        limite_inferior = ALTO - longitud_palabra + 1
    if sentido == 'anti-normal':
        s = -1
        columna_inicio = 0
        fila_inicio = longitud_palabra-1
        limite_derecho = ANCHO - longitud_palabra+1
        limite_inferior = ALTO
                
    return revisar_palabra (sopa, palabra, longitud_palabra, "anti-diagonal", sentido, columna_inicio, fila_inicio,
                    limite_derecho, limite_inferior, s, x, y)

# función para testear la función buscar_anti_diagonal. 

def test_buscar_anti_diagonal():
    assert buscar_anti_diagonal([['p','e','s','s','e','s'],
        ['t','e','s','t','e','w'],
        ['f','l','s','t','o','t'],
        ['t','e','e','w','t','s'],
        ['w','t','t','s','e','t']], 'wow', 'normal', 6, 5, 3) == ('wow', 1, 5, 'anti-diagonal', 'normal'), "Test 'wow', anti-diagonal, 'normal' failed"
    assert buscar_anti_diagonal([['q','e','s','s','e','s'],
        ['t','e','s','t','e','a'],
        ['f','l','l','t','p','t'],
        ['t','e','e','o','t','s'],
        ['w','t','s','s','s','t']], 'sopa', 'anti-normal', 6, 5, 4) == ('sopa', 4, 2, 'anti-diagonal', 'anti-normal'), "Test 'sopa', anti-diagonal, 'anti-normal' failed"
    assert buscar_anti_diagonal([['q','e','s','s','e','l'],
        ['t','e','s','t','e','l'],
        ['f','l','s','t','e','o'],
        ['t','e','e','e','t','r'],
        ['w','t','t','s','e','t']], 'viaje', 'anti-normal', 6, 5, 5) == ('viaje', -1, -1, 'anti-diagonal', 'anti-normal'), "Test 'viaje', diagonal, 'anti-normal' failed" 
	

# chequear: lista de listas de Srings, String -> Tupla (String, Numero, Numero, String, String) / Tupla (String, String)
#
# La función pasa la palabra y la sopa a cada de estos funciónes para hacer busqueda horizontal, vertical y diagonal:
# buscar_horizontal
# buscar_vertical
# buscar_diagonal
# buscar_anti_diagonal

# La fucnión chequear
# devuelve tupla con la información donde encotró la palabra en la sopa, con que dirección (horizontal, vertical, diagonal) y con que sentido (normal/anti-normal)
# En el caso que no encontró la palabram devuelve tupla (palabra "no encontrada")


def chequear(sopa, palabra):
    ANCHO = len(sopa[0])
    ALTO = len(sopa)
    longitud_palabra = len(palabra)
    rta = buscar_horizontal(sopa, palabra, 'normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    rta = buscar_horizontal(sopa, palabra, 'anti-normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    rta = buscar_vertical(sopa, palabra, 'normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    rta = buscar_vertical(sopa, palabra, 'anti-normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    rta = buscar_diagonal(sopa, palabra, 'normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    rta = buscar_diagonal(sopa, palabra, 'anti-normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    rta = buscar_anti_diagonal(sopa, palabra, 'normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    rta = buscar_anti_diagonal(sopa, palabra, 'anti-normal', ANCHO, ALTO, longitud_palabra)
    if rta[1] != -1:
        return rta
    
    return (palabra, "no encontrada")


# opcion_2: lista de listas de Srings, lista de Strings -> Lista de Tuplas 

# La función toma una sopa de letras y lista de palabras y realiza busqueda de cada palabra en la sopa. 
# Devuelve la lista de tuplas, cada tupla representa información sobre la palabra:
# si la palabra esta en la sopa: donde encotró la palabra en la sopa, con que dirección (horizontal, vertical, diagonal) y con que sentido (normal/anti-normal)
# si no la encontró la palabra devuelve tupla con 2 Strings: (palabra "no encontrada")

def opcion_2(sopa, lista_palabras):
    esta_en_sopa = []
    for i in lista_palabras:
        esta_en_sopa += [chequear(sopa, i)]
    return esta_en_sopa



def elegir_opcion():
    opcion = int(input("""Ingresé "1" para crear la sopa de letras 
    "2" para buscar palabras en la sopa: """))
    print(opcion)
    if opcion == 1:
        opcion_1()
    if opcion == 2:
        sopa = [['p','e','s','s','e','s'],
        ['t','e','s','t','e','w'],
        ['f','l','s','t','o','t'],
        ['t','e','e','w','t','s'],
        ['w','t','t','s','e','t']]
        print(sopa)
        lista_de_palabras = input("""Ingrese las palabras para encontrar en la sopa
dividiendolas con el space bar: """)
        print(opcion_2(sopa, lista_de_palabras.split()))
        
elegir_opcion()


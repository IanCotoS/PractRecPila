# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 23/10/2022 11:28 am
# Última modificación: 24/10/2022 10:10 pm
# Versión: 3.10.8

# Definir funciones auxiliares
def recurDivisores(num, div):
    """
    F: Función que se encarga de obtener la suma de los divisores de un número
    E:numero(int), div (int)
    S:Suma de los divisores
    """
    if div==num:
        return 0
    else:
        if num%div==0:
            return div+recurDivisores(num,div+1)
        else:
            return 0+recurDivisores(num, div+1)

def esPar (num):
    """
    Funcionalidad: Determina si un número es par
    Entradas: num (int)
    Salidas: True/False (bool)
    """
    if num%2==0:
        return True 
    else:
        return False

def esDigito(pDigito):
    """
    Funcionalidad: comprueba que sea un dígito, si lo es,
                   retorna Ture
    Entradas: pDigito (int)
    Salidas: True/False (bool)
    """
    if abs(pDigito) <= 9: # Acepta negativos
        return True
    return False

def esEnteroPositivo(pNum):
    """
    Funcionalidad: comprueba que sea entero positivo, si lo es,
                   retorna Ture
    Entradas: pNum (int)
    Salidas: True/False (bool)
    """
    try:
        pNum = int(pNum)
        if pNum <= 0:
            return False
    except:
        return False
    return True

def esBinario(pBinario):
    """
    Funcionalidad: comprueba que sea binario, si lo es,
                   retorna Ture
    Entradas: pBinario (int)
    Salidas: True/False (bool)
    """
    if pBinario == 0:
        return True
    else:
        if pBinario%10 not in [0,1]:
            return False
        return esBinario(pBinario//10)

def contarDigitos(pNum):
    """
    Funcionalidad: cuenta la cantidad de dígitos de la unidad
    Entradas: pNum (int)
    Salidas: cantidad de dígitos de pNum (int)
    """
    if pNum <= 9:
        return 1
    else:
        return 1 + contarDigitos(pNum//10)
    
def elevarNumero(pNum, pExponente):
    """
    Funcionalidad: eleva pNum al pExponente
    Entradas: pNum (int)
              pExponente (int)
    Salidas: número elevado (int)
    """
    if pExponente == 0:
        return 1
    else:
        return pNum * elevarNumero(pNum, pExponente-1)

def esPrimo(pNum, div=2):
    """
    Funcionalidad: comprueba que un número sea primo, si lo es,
                   retorna True
    Entradas: pNum (int)
              div (int): sirve como divisor y no se debe cambiar su valor
    Salidas: True/False (bool)
    """
    if (pNum//2)+1 == div:
        return True
    else:
        if pNum%div==0 or pNum == 1:
            return False
        return esPrimo(pNum, div+1)

# Definir funciones retos
'----------------- Reto 1 -------------------'
def digitoPosicion (posi, numero):
    """
    F:Deetrmina si el número en la posición escogida es par o impar.
    E:posi (int), numero(int)
    S:Devuelve un valor booleano (bool)
    """
    valor=False
    if posi==1:
        return esPar(numero%10)
    else:
        return digitoPosicion(posi-1, numero//10)

def digitoPosicionAux (posi, numero):
    """
    F:Valida las entradas
    E:posi (int), numero(int)
    S:Un string o el valor de la función digitoPosicion
    """
    try:
        numero=int(numero)
        posi=int(posi)
        if (posi<=contarDigitos(numero)) and (posi>=1):
            return digitoPosicion(posi,numero)
        else:
            return "El número no posee en índice solicitado o el indice es menor que 1"
    except:
        return "Debe digitar un número entero"

def digitoPosicionES(posi, numero):
    """
    F:Imprime las entradas y el valor de la función auxiliar
    E:posi (int), numero(int)
    S:Valor de digitoPosicionAux
    """
    print("Entradas:", posi, numero)
    return print(digitoPosicionAux(posi, numero))

'----------------- Reto 2 -------------------'

def sumaEnteroIndCero(pDigito, pNum, pos=0):
    """
    Funcionalidad: suma pDigito donde hay ceros en pNum
    Entradas: pDigito (int)
              pNum (int)
              pos (int): sirve como posición, dejarlo en 0
    Salidas: resultado de la suma donde hay ceros (int)
    """
    if pNum == 0:
        return 0
    else:
        if pNum%10 == 0:
            return pDigito*elevarNumero(10,pos) + sumaEnteroIndCero(pDigito, pNum//10, pos+1)
        return sumaEnteroIndCero(pDigito, pNum//10, pos+1)

def sumaEnteroInd(pDigito, pNum):
    """
    Funcionalidad: suma pDigito donde hay ceros en pNum
    Entradas: pDigito (int)
              pNum (int)
    Salidas: resultado de la suma (int)
    """
    if pNum == 0:
        return 0
    else:
        cantPos = elevarNumero(10, contarDigitos(pNum)-1)
        suma = pDigito + pNum//cantPos
        if suma > 9:
            if suma%10 == 0:
                suma = 0
            else:
                suma %= 10
        return suma*cantPos + sumaEnteroInd(pDigito, pNum%cantPos)

def sumaEnteros(pDigito, pNum):
    """
    Funcionalidad: suma los resultados de los ceros y los otros números
                   de pNum con pDigito
    Entradas: pDigito (int)
              pNum (int)
    Salidas: resultado de la suma de ambos (int)
    """
    return sumaEnteroIndCero(pDigito, pNum) + sumaEnteroInd(pDigito, pNum)

def sumaEnterosAux(pDigito, pNum):
    """
    Funcionalidad: verifica datos de entrada
    Entradas: pDigito (int)
              pNum (int)
    Salidas: resultado sumaEnteros(pDigito, pNum) (int)
    """
    if not(esEnteroPositivo(pDigito) and esDigito(pDigito)):
        return "Debe introducir un solo dígito entero positivo."
    elif not(esEnteroPositivo(pNum)):
        return "Debe introducir un número entero positivo."
    elif pDigito == 0:
        return pNum
    return sumaEnteros(pDigito, pNum)

'----------------- Reto 3 -------------------'

def binarioADecimal(pBinario):
    """
    Funcionalidad: convierte de binario a decimal
    Entradas: pBinario (int)
    Salidas: número en decimal (int)
    """
    if pBinario == 0:
        return 0
    else:
        exponente = contarDigitos(pBinario)-1
        return elevarNumero(2, exponente) + binarioADecimal(pBinario%elevarNumero(10, exponente))

def binarioADecimalAux(pBinario):
    """
    Funcionalidad: verifica datos de entrada
    Entradas: pBinario (int)
    Salidas: resultado binarioADecimal(pBinario) (int)
    """
    if not esEnteroPositivo(pBinario):
        return "Debe introducir un dígito numérico."
    elif not esBinario(pBinario):
        return "Debe introducir un número binario."
    return binarioADecimal(pBinario)

'----------------- Reto 4 -------------------'
def sumatoria(numero):
    """
    F:Determina la sumatoria del numero digitado
    E:numero(int)
    S:Devuelve la sumatoria del número (int)
    """
    if numero==0:
        return 0
    else:
        return numero + sumatoria(numero-1)
        
def sumatoriaAux(numero):
    """
    F:Valida las entradas
    E:numero(int)
    S:Un string o el valor de la función sumatoria
    """
    try:
        numero=int(numero)
        if numero>=0:
            return sumatoria(numero)
        else:
            return "El número tiene que ser mayor o igual a 0"
    except:
        return "Se excedió la cantidad máxima de recursión que es 99 o el número introducido no es entero"

def sumatoriaES(numero):
    """
    F:Imprime las entradas y el valor de la función auxiliar
    E:numero(int)
    S:Valor de sumatoriaAux
    """
    print("Entrada:", numero)
    return print(sumatoriaAux(numero))

'----------------- Reto 5 -------------------'

def cantidadPrimosRango(pNum, pNumUlt):
    """
    Funcionalidad: da la cantidad de primos en ese rango
    Entradas: pNum (int)
              pNumUlt (int)
    Salidas: cantidad de primos (int)
    """
    if pNum > pNumUlt:
        return 0
    else:
        if esPrimo(pNum):
            return 1 + cantidadPrimosRango(pNum+1, pNumUlt)
        return cantidadPrimosRango(pNum+1, pNumUlt)

def cantidadPrimosRangoAux(pNum, pNumUlt):
    """
    Funcionalidad: verifica datos de entrada
    Entradas: pNumUlt (int)
              pNum (int)
    Salidas: resultado cantidadPrimosRango(pNum, pNumUlt) (int)
    """
    if not (esEnteroPositivo(pNum) or esEnteroPositivo(pNumUlt)):
        return "Debe introducir número enteros positivos."
    elif pNum > pNumUlt:
        return "El primer número debe ser menor o igual al segundo."
    return cantidadPrimosRango(pNum, pNumUlt)

'----------------- Reto 6 -------------------'

def primoMenorCercano(pNum):
    """
    Funcionalidad: da el primo más cernano menos a pNum
    Entradas: pNum (int)
    Salidas: el primo más cercano menor (int)
    """
    if esPrimo(pNum):
        return pNum
    return primoMenorCercano(pNum-1)

def primoMenorCercanoAux(pNum):
    """
    Funcionalidad: verifica datos de entrada
    Entradas: pNum (int)
    Salidas: resultado primoMenorCercano(pNum) (int)
    """
    if not esEnteroPositivo(pNum):
        return "Debe introducir un número entero positivo."
    elif pNum == 1:
        return 1
    return primoMenorCercano(pNum)

'----------------- Reto 7 -------------------'

def numCercanos(num1, num2):
    """
    F: Determina si dos números son cercanos
    E: num1(int), num2 (int)
    S: Devuelve un valor True/False (bool)
    """
    div1=recurDivisores(num1, 1)
    div2=recurDivisores(num2, 1)
    if div1==div2:
        return True
    else:
        return False

def numCercanosAux(num1, num2):
    """
    F:Valida las entradas
    E:num1(int), num2 (int)
    S:Un string o el valor de la función numCercanos
    """
    try:
        num1=int(num1)   
        num2=int(num2)
        if (num1>=1) and (num2>=1):
            return numCercanos(num1, num2)
        else:
            return "Ambos números tienen que ser igual o mayores que 1"
    except:
        return "Los numeros tienen que ser enteros"
        
def numCercanosES(num1, num2):
    """
    F:Imprime las entradas y el valor de la función auxiliar
    E:num1 (int), num2 (int)
    S:Valor de numCercanosAux
    """
    print("Entradas: ", num1, num2)
    return print(numCercanosAux(num1, num2))
    
# Programa principal
'----------------- Reto 1 -------------------'

print('\n----------------- Reto 1 -------------------\n'+
'-------- Digito en posicion n es par --------')
digitoPosicionES(3, 6700)
digitoPosicionES(4, 92553)
digitoPosicionES(3, 80)
digitoPosicionES(1, 94)

'----------------- Reto 2 -------------------'

print('\n----------------- Reto 2 -------------------\n'+
'-------- Suma de enteros individual --------')
print("\nA. a=1 y b=1024")
print(sumaEnterosAux(1, 1024))
print("\nB. a=2 y b=14")
print(sumaEnterosAux(2, 14))
print("\nC. a=8 y b=1221")
print(sumaEnterosAux(8, 1221))
print("\nD. a=7 y b=1024")
print(sumaEnterosAux(7, 1024))
print("\nE. a=74 y b=421")
print(sumaEnterosAux(74, 421))

'----------------- Reto 3 -------------------'

print('\n----------------- Reto 3 -------------------\n' + 
'------------ Binario a decimal -------------')
print("\nA. n=1010")
print(binarioADecimalAux(1010))
print("\nB. n=101")
print(binarioADecimalAux(101))
print("\nC. n=10000000")
print(binarioADecimalAux(10000000))
print("\nD. n=110010")
print(binarioADecimalAux(110010))
print("\nE. n=234")
print(binarioADecimalAux(234))

'----------------- Reto 4 -------------------'
print('\n----------------- Reto 4 -------------------\n'+
'-------- Sumatoria de un número --------')
sumatoriaES(10)
sumatoriaES(1000)#Esta prueba va a dar error, ya que la cantidad máxima de recursión que permite python es 99
sumatoriaES(4)
sumatoriaES(100000)#Esta prueba va a dar error, ya que la cantidad máxima de recursión que permite python es 99
sumatoriaES(99)
sumatoriaES(89)
'----------------- Reto 5 -------------------'

print('\n----------------- Reto 5 -------------------\n' + 
'--------- Cantidad primos en rango ---------\n'+
"\nLos resultados son 1 número menos que las \ntiradas del documento porque 1 no es primo.")
print("\nA. a=1 y b=3")
print(cantidadPrimosRangoAux(1, 3))
print("\nB. a=1 y b=7")
print(cantidadPrimosRangoAux(1, 7))
print("\nC. a=1 y b=15")
print(cantidadPrimosRangoAux(1, 15))
print("\nD. a=19 y b=15")
print(cantidadPrimosRangoAux(19, 15))

'----------------- Reto 6 -------------------'

print('\n----------------- Reto 6 -------------------\n' + 
'------ Número primo menor más cercano ------')
print("\nA. n=10")
print(primoMenorCercanoAux(10))
print("\nB. n=11")
print(primoMenorCercanoAux(11))
print("\nC. n=20")
print(primoMenorCercanoAux(20))
print("\nD. n=65")
print(primoMenorCercanoAux(65))
print("\nE. n=-12")
print(primoMenorCercanoAux(-12))

'----------------- Reto 7 -------------------'
print('\n----------------- Reto 7 -------------------\n'+
'-------- Determinar si 2 números son cercanos --------')

numCercanosES(13, 7)
numCercanosES(18, 51)
numCercanosES(98, 175)
numCercanosES(220, 562)

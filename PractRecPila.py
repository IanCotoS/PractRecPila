# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 23/10/2022 11:28 am
# Última modificación: 23/10/2022 03:18 pm
# Versión: 3.10.8

# Definir funciones auxiliares

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

# Programa principal

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

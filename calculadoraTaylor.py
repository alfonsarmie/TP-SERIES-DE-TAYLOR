import math, os

global aprox
aprox = 0.0

# X: Es el numero que queremos calcular

def sen_taylor(x):

    global aprox

    aprox = 0.0

    for i in range(51):
        coef = (-1) ** i
        num = x ** ((2 * i) + 1)
        denom = math.factorial((2 * i) + 1)
        nume = (coef * num)
        aprox += nume / denom

        if i == 1 or 2 or 3 or 5 or 10 or 20 or 50:
             resultado(i)


def cos_taylor(x):

    global aprox

    aprox = 0.0

    for i in range(51):
        coef = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial((2*i))
        aprox += (coef * num) / denom

        if i == 1 or 2 or 3 or 5 or 10 or 20 or 50:
             resultado(i)

def e_taylor(x):

    global aprox
    aprox= 0.0

    for i in range(51):
        num = x ** i
        denom = math.factorial(i)
        aprox += (num) / denom

        if i == 1 or 2 or 3 or 5 or 10 or 20 or 50:
             resultado(i)
        

def resultado(v):
     
     global r1,r2,r3,r4,r5,r6,r7,r8

     match str(v):
          case "1": r1 = aprox
          case "2": r2 = aprox
          case "3": r3 = aprox
          case "5": r4 = aprox
          case "10": r5 = aprox
          case "20": r6 = aprox
          case "50": r7 = aprox


def MENUIN():
    print("\n       Bienvenido\n")
    print("1- Calcular e^x")
    print("2- Calcular senx")
    print("3- Calcular cosx")
    print("4- Salir")


def MENUINICIO():
     global tip
     global valor
     op = "1"
     while (op !="3"):
        os.system("cls")
        MENUIN()
        op = str(input("\n Ingrese su opcion: "))
        while (op < "1" or op > "3"):
                 os.system("cls")
                 MENUIN()
                 op = str(input("                   Ingreso Invalido - reintente: "))
        valor = float(input("Ingresa el valor de x: "))
        match op:
                case "1": 
                    tip = 1 
                    e_taylor(valor)
                case "2": 
                    tip = 2 
                    sen_taylor(valor)
                case "3": 
                    tip = 3 
                    cos_taylor(valor)
        MOSTRARRES()

def MOSTRARRES(): 
    os.system("cls")
    match tip:
         case 1: 
            op = "e^"
            res = math.exp(valor)
         case 2: 
              op = "sen"
              res = math.sin(valor)
         case 3: 
              op = "cos"
              res = math.cos(valor)
    print()
    print ("                           RESULTADOS          ")
    print ('--------------------------------------------------------------------------------------------------')
    print (' Resultado original de ', op, valor,': ', res)
    print ('--------------------------------------------------------------------------------------------------')
    print (' Resultado si n=1: ',r1)    
    print (' Resultado si n=2: ',r2) 
    print (' Resultado si n=3: ',r3)
    print (' Resultado si n=5: ',r4)
    print (' Resultado si n=10: ',r5)
    print (' Resultado si n=20: ',r6)
    print (' Resultado si n=50: ',r7)

    wait = input()

MENUINICIO()

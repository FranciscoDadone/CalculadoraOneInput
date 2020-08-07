def sumar(n1,n2):
    return n1+n2

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def calculate(var_entrada): # Definición de la función principal. Toma un argumento 'var_entrada'.
    while(var_entrada.count('+') or var_entrada.count('-') or var_entrada.count('*') or var_entrada.count('/') or var_entrada.count(')') or var_entrada.count('(')): # Si en la variable 'var_entrada' no hay alguno de esos símbolos, itera en el bucle 
        ############### Definición de variables del bucle while ###################
        primeraVez = False
        cachear = False
        cache = ""
        cacheMultiplicacion1 = ""
        cacheMultiplicacion2 = ""
        cacheDivision1 = ""
        cacheDivision2 = ""
        notContinue = False
        notContinueParentesis = False
        ############################################################################

        if((var_entrada.count('*') and var_entrada.count('(') and var_entrada.count(')')) and not (var_entrada.count('/') or (var_entrada.count('+') or var_entrada.count('-')))): # Remueve paréntesis innecesarios
            var_entrada = var_entrada.replace('(', '')
            var_entrada = var_entrada.replace(')', '')

        if(var_entrada.count(')') or var_entrada.count('(')): # Evalúa si hay paréntesis
            for i in var_entrada: # Itera por cada signo o número de la función
                if(cachear): # Evalúa si se tiene que almacenar lo que se está iterando
                    cache += i # almacena en la variable cache lo que se está iterando
                if(i == '(' and not primeraVez): #evalúa si lo que se está iterando es un signo de abrir paréntesis y no es la primera vez que se encuentra uno en el recorrido del bucle
                    cachear = True # setea el chacheo a verdadero para que se copie en una variable a parte (cache) lo que está dentro de los paréntesis
                elif(i == ')'): # si se encuentra un signo de cerrar paréntesis termina de copiar a la variable (cache), setea el cachear a falso y setea la primera vez a verdadero para que no se agregue el contenido de otro posible paréntesis dentro de la variable cache
                    cache += i
                    cachear = False
                    primeraVez = True
            
            res1 = var_entrada.split('(', 1) # Divide la cadena que ingresó el usuario en el signo de abrir paréntesis (solo el primero que se encuentre)
            res2 = var_entrada.split(')', 1)

            if(cache.count('+') or cache.count('-') or cache.count('*') or cache.count('/')): # Si dentro del paréntesis hay algún símbolo, se hace un callback a la función para calcular el paréntesis y almacenarlo en la variable cache1
                cache1 = calculate(cache.replace(')', ''))

            var_entrada = res1[0] + calculate(cache1.replace(')', '')) + res2[1] # reemplazar el resultado del paréntesis en la función

            notContinueParentesis = True

        elif(var_entrada.count('*') and (notContinueParentesis == False)): # Si hay un signo de multiplicación en la función y no hay más paréntesis...
            res = var_entrada.split('*') # Divide a la función por el signo *
            for i in res[0]: # Itera los caracteres de la izquierda de la cadena que ingresó el usuario partida por el signo de multiplicar
                cacheMultiplicacion1 += i # Copia en la variable 'cacheMultiplicacion1' lo que se está iterando
                if(i == '+' or i == '-'): # Evalúa si hay algún signo + o - en el transcurso del bucle para limpiar el contenido de la variable y cachear el siguiente hasta finalizar y tener el multiplicando almacenado en esa variable
                    cacheMultiplicacion1 = "" # limpia la variable
            for i in res[1]: # Itera sobre la parte de la derecha de la cadena que ingresó el usuario partida por el signo *
                if(i == '+' or i == '-'): # si encuentra un signo + o -, finaliza el bucle para terminar de almacenar lo iterado en la variable cacheMultiplicacion2
                    break
                cacheMultiplicacion2 += i
            
            res = var_entrada.split((str(cacheMultiplicacion1)+"*"+str(cacheMultiplicacion2))) # Separa la función en la multiplicación, concatenando el cache de multiplicación 1, un signo * y el cache de multiplicación 2 para eliminarlos de la variable con la cadena principal y en vez de la multiplicación, poner el resultado de la misma.
            var_entrada = res[0] + str(multiplicacion(float(cacheMultiplicacion1), float(cacheMultiplicacion2))) + res[1] # concatena el resultado de la multiplicación a la variable con la función
            
            notContinue = True
            notContinueParentesis = True

        elif(var_entrada.count('/') and (notContinueParentesis == False)): # evalúa si hay una división y si puede continuar
            res = var_entrada.split('/') # divide la variable entrada por el signo de división
            for i in res[0]: # Itera por los elementos de la izquierda de la división
                cacheDivision1 += i
                if(i == '+' or i == '-'): # Idem multiplicación
                    cacheDivision1 = ""
            for i in res[1]: # Idem multiplicación
                if(i == '+' or i == '-'):
                    break
                cacheDivision2 += i
            
            # Reemplaza el resultado de la división en la función
            res = var_entrada.split((str(cacheDivision1) + "/" + str(cacheDivision2)))
            var_entrada = res[0] + str(division(float(cacheDivision1), float(cacheDivision2))) + res[1]
            notContinue = True

        elif((var_entrada.count('+') or var_entrada.count('-')) and (notContinue == False) and (notContinueParentesis == False)): # Ultima fase de la resolución.. la suma algebráica
            delta = ""
            delta1 = ""
            vuelta = 0
            for i in var_entrada: # Itera sobre la cadena de la función...
                if(i == '-' and vuelta >= 1): # Si hay un signo menos y las vueltas son mayores o iguales a 1, se cambia ese signo por un +-
                    delta += '+-'
                else:
                    delta += i # Copia en la variable delta lo que se está iterando
                vuelta += 1 # suma 1 a las vueltas para llevar el conteo y no cambiar el signo menos (hitéticamente) del principio de la ecuación
            var_entrada = delta # asigna a 'var_entrada' el valor de delta

            for i in range(len(var_entrada)): # Itera por la longitud de la cadena de caracteres
                pasar = False
                if(var_entrada[i] == '+' and var_entrada[(i+1)] == '+'): # comprueba si hay un + en la posición del bucle que va recorriendo y si en la siguiente a esa también hay un +. Es para solucionar un bug raro.
                    pasar = True
                if(pasar == False): # Escribe en la variable delta1 si no tiene que saltar ese caracter porque es un +
                    delta1 += var_entrada[i]
            var_entrada = delta1 # Sobreescribe la variable 'var_entrada' por delta1
            
            splitSumas = var_entrada.split('+') # Separa toda la función (suma algebráica) por los signos +

            resultado = 0.0
            for i in splitSumas: # Recorre el array 
                resultado = sumar(float(resultado), float(i)) # Suma todos los elementos del array

            return str(resultado) # Retorna el resultado de la función
    return var_entrada

#Inicio
var_entrada = input("Ingrese una función: ") # Inicio del programa. Entrada de datos.
print(calculate(var_entrada)) # Llama a la función calcular, le pasa el dato que ingresó el usuario e imprime el resultado.
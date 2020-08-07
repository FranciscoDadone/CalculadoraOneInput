def sumar(n1,n2):
    return n1+n2

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def calculate(var_entrada):
    while(var_entrada.count('+') or var_entrada.count('-') or var_entrada.count('*') or var_entrada.count('/') or var_entrada.count(')') or var_entrada.count('(')):
        primeraVez = False
        cachear = False
        cache = ""
        cacheMultiplicacion1 = ""
        cacheMultiplicacion2 = ""
        cacheDivision1 = ""
        cacheDivision2 = ""
        notContinue = False
        notContinueParentesis = False

        if((var_entrada.count('*') and var_entrada.count('(') and var_entrada.count(')')) and not (var_entrada.count('/') or (var_entrada.count('+') or var_entrada.count('-')))):
            var_entrada = var_entrada.replace('(', '')
            var_entrada = var_entrada.replace(')', '')

        if(var_entrada.count(')') or var_entrada.count('(')): # si hay paréntesis
            for i in var_entrada:
                if(cachear):
                    cache += i
                if(i == '(' and not primeraVez):
                    cachear = True
                elif(i == ')'):
                    cache += i
                    cachear = False
                    primeraVez = True
            
            res1 = var_entrada.split('(', 1)
            res2 = var_entrada.split(')', 1)
            x = cache.split('/')
            if(cache.count('+') or cache.count('-') or cache.count('*')):
                var_entrada = res1[0] + calculate(cache.replace(')', '')) + res2[1]
            else:
                x = cache.split('/')
                x0 = x[0].replace('(', '')
                x1 = x[1].replace(')', '')
                var_entrada = res1[0] + str(division(int(x0), int(x1))) + res2[1]

            notContinueParentesis = True

        elif(var_entrada.count('*') and (notContinueParentesis == False)):
            res = var_entrada.split('*')
            for i in res[0]:
                cacheMultiplicacion1 += i
                if(i == '+'):
                    cacheMultiplicacion1 = ""
            for i in res[1]:
                if(i == '+'):
                    break
                cacheMultiplicacion2 += i
            
            res = var_entrada.split((str(cacheMultiplicacion1)+"*"+str(cacheMultiplicacion2)))
            var_entrada = res[0] + str(multiplicacion(float(cacheMultiplicacion1), float(cacheMultiplicacion2))) + res[1]
            notContinue = True
            notContinueParentesis = True

        elif(var_entrada.count('/') and (notContinueParentesis == False)):
            res = var_entrada.split('/')
            for i in res[0]:
                cacheDivision1 += i
                if(i == '+' or i == '-'):
                    cacheDivision1 = ""
            for i in res[1]:
                if(i == '+' or i == '-'):
                    break
                cacheDivision2 += i
            
            res = var_entrada.split((str(cacheDivision1)+"/"+str(cacheDivision2)))
            var_entrada = res[0] + str(division(float(cacheDivision1), float(cacheDivision2))) + res[1]
            notContinue = True

        elif((var_entrada.count('+') or var_entrada.count('-')) and (notContinue == False) and (notContinueParentesis == False)):
            delta = ""
            delta1 = ""
            vuelta = 0
            for i in var_entrada:
                if(i == '-' and vuelta > 1):
                    delta += '+-'
                else:
                    delta += i
                vuelta += 1
            var_entrada = delta

            for i in range(len(var_entrada)):
                pasar = False
                if(var_entrada[i] == '+' and var_entrada[(i+1)] == '+'):
                    pasar = True
                if(pasar == False):
                    delta1 += var_entrada[i]
            var_entrada = delta1
            
            splitSumas = var_entrada.split('+')

            resultado = 0.0
            for i in splitSumas:
                resultado = sumar(float(resultado), float(i))

            return str(resultado)
    return var_entrada

var_entrada = input("Ingrese una función: ") # start
print(calculate(var_entrada))

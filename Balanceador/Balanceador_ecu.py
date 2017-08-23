import functools
import re as regex
from fractions import Fraction
from math import gcd

import sympy
from sympy import *
from Exceptions import *

from tabla_periodica import *


class Balanceador:
    def __init__(self):
        self.set_elementos = set()
        self.variables = -1
        self.ecu1_token = []
        self.ecu2_token = []
        self.set_reactivos = set()
        self.set_productos = set()

    def parsear(self, ecu1, ecu2):
        '''
        :param ecu1: String de reactivos
        :param ecu2: String de productos
        :return: Tupla (reactivos, productos) en donde cada posicion tiene una lista de moleculas. Cada molecula es una
        tupla (elemento_molecula, cantidad)
        '''
        if '(' in ecu1 or '(' in ecu2:
            raise DatosIngresadosIncorrectosError('Revisar datos ingresados')
        ecu1_tokenizada = ecu1.replace(" ", "").split('+')
        ecu2_tokenizada = ecu2.replace(" ", "").split('+')
        ecu1_tokenizada = self.remover_coef_estequiometricos(ecu1_tokenizada)
        ecu2_tokenizada = self.remover_coef_estequiometricos(ecu2_tokenizada)
        self.ecu1_token = ecu1_tokenizada
        self.ecu2_token = ecu2_tokenizada
        parseo_reac = []
        parseo_prod = []
        for react in ecu1_tokenizada:
            match1 = regex.findall(r'([A-Z][a-z]*)(\d*)', react)
            parseo_reac.append(match1)
        for pro in ecu2_tokenizada:
            match2 = regex.findall(r'([A-Z][a-z]*)(\d*)', pro)
            parseo_prod.append(match2)
        parseo_reac = self.procesar_moleculas(parseo_reac)
        parseo_prod = self.procesar_moleculas(parseo_prod)
        self.chequear_ecuacion((parseo_reac, parseo_prod))
        return parseo_reac, parseo_prod

    def remover_coef_estequiometricos(self, ecu_parseada):
        nueva_ecu_parseada = []
        for molecula in ecu_parseada:
            if molecula[0].isdigit():
                molecula = molecula[1:]
            nueva_ecu_parseada.append(molecula)
        return nueva_ecu_parseada


    def chequear_ecuacion(self, parseo):
        ''' Devuelve error si hay distintos elementos en los productos y reactivos de la ecuacion. '''
        for molecula in parseo[0]:
            for elemento in molecula:
                self.set_reactivos.add(elemento[0])
        for molecula in parseo[1]:
            for elemento in molecula:
                self.set_productos.add(elemento[0])
        if self.set_reactivos - self.set_productos != set():
            raise EcuacionIncorrectaError('Ecuacion incorrecta')

    def procesar_moleculas(self, lista_elementos):
        '''
        :param lista_elementos: lista que contiene tuplas (elemento, cantidad)
        :return: lista donde se agregaron unos a los elementos sin coeficiente
        '''
        lista_moleculas = []
        for molecula in lista_elementos:
            lista_molecula = []
            for elemento in molecula:
                if elemento[1] == "":
                    lista_molecula.append((elemento[0], 1))
                else:
                    lista_molecula.append((elemento[0], elemento[1]))
            lista_moleculas.append(lista_molecula)
        return lista_moleculas

    def generar_set_elementos(self, tupla_elementos):
        ''' Genera un conjunto con todos los elementos que intervienen en la reaccion'''
        self.set_elementos = self.set_productos | self.set_reactivos

    def crear_matriz_sistema(self, tupla_elementos):
        '''
        :param tupla_elementos: Tupla (reactivos, productos) en donde cada posicion tiene una lista de moleculas. Cada
        molecula es una tupla (elemento_molecula, cantidad).
        :return: matriz que representa el sistema de ecuaciones.
        '''
        cant_variables = self.contar_terminos(tupla_elementos)

        # genera variables para cada termino
        self.variables = symbols('x0:%d' % cant_variables)

        matriz = []
        self.generar_set_elementos(tupla_elementos)

        for e in self.set_elementos:
            fila = []
            # armo ecuaciones del lado de los reactivos
            for i in tupla_elementos[0]:
                inserto = False
                for j in i:
                    if j[0] == e:
                        fila.append(float(j[1]))
                        inserto = True
                if not inserto:
                    fila.append(0)
                    inserto = True
            # armo ecuaciones del lado de los productos
            for i in tupla_elementos[1]:
                inserto = False
                for j in i:
                    if j[0] == e:
                        fila.append(-1 * float(j[1]))
                        inserto = True
                if not inserto:
                    fila.append(0)
                    inserto = True
            matriz.append(fila)
        return matriz

    def resolver_sistema(self, matriz):
        '''
        :param matriz: matriz que representa el sistema de ecuaciones.
        :return: solucion al sistema de ecuaciones que puede incluir variables libres
        '''
        vector_ceros = [0 for x in range(len(self.set_elementos))]
        solsym = sympy.linsolve((Matrix(matriz), Matrix(vector_ceros)), self.variables)
        return solsym

    def contar_terminos(self, tupla_elementos):
        '''
        Devuelve cantidad de terminos en total que intervienen en la ecuacion (reactivos+productos).
        Cada termino es una molecula.
        '''
        return len(tupla_elementos[0]) + len(tupla_elementos[1])

    def calcular_mcm_denominador(self, solucion):
        '''
        :param solucion: solucion al sistema de ecuaciones que puede incluir variables libres
        :return: minimo comun multiplo de los denominadores de las fracciones
        '''
        sol = list(solucion)
        lst = []
        for x in sol[0]:
            coef = float(x.as_coeff_Mul()[0])
            # Convierto la solucion, que viene dada con decimales, en una fraccion
            fracc = Fraction(coef).limit_denominator(10)
            lst.append(fracc.denominator)
        return functools.reduce(lcm, lst)

    def mcm(self, a, b):
        ''' Calculo el minimo comun multiplo entre dos enteros '''
        return a * b // gcd(a, b)

    def calcular_coeficientes_finales(self, solucion):
        '''
        :param solucion: solucion al sistema de ecuaciones que puede incluir variables libres
        :return: coeficientes enteros finales para el resultado
        '''
        mcm = self.calcular_mcm_denominador(solucion)
        lst_sol = list(solucion)
        lst = []
        for x in lst_sol[0]:
            coef = float(x.as_coeff_Mul()[0])
            lst.append(int(mcm * coef))
        return lst

    def devolver_ecuacion(self, coef_finales):
        '''
        :param coef_finales: coeficientes enteros finales para el resultado
        :return: String de ecuacion balanceada
        '''
        salida = ""
        long_ecu1 = len(self.ecu1_token)
        long_ecu2 = len(self.ecu2_token)
        for i in range(long_ecu1 - 1):
            salida += str(coef_finales[i]) + str(self.ecu1_token[i]) + " + "
        salida += str(coef_finales[long_ecu1 - 1]) + str(self.ecu1_token[long_ecu1 - 1]) + " = "
        for j in range(long_ecu2 - 1):
            salida += str(coef_finales[long_ecu1 + j]) + str(self.ecu2_token[j]) + " + "
        salida += str(coef_finales[long_ecu1 + long_ecu2 - 1]) + \
                  str(self.ecu2_token[long_ecu2 - 1])
        return salida

    def validar(self, parseadas):
        '''
        Valida si los datos estan ingresados de manera correcta por el usuario, caso contrario levanta una excepcion.
        '''
        for i in parseadas[0]:
            for j in i:
                if j[0] not in elementos or not str(j[1]).isdigit():
                    raise DatosIngresadosIncorrectosError('Chequear datos ingresados')
        for i in parseadas[1]:
            for j in i:
                if j[0] not in elementos or not str(j[1]).isdigit():
                    raise DatosIngresadosIncorrectosError('Chequear datos ingresados')

    def ejecutar(self, ecu1, ecu2):
        parseadas = self.parsear(ecu1, ecu2)
        self.validar(parseadas)
        matriz = self.crear_matriz_sistema(parseadas)
        solucion = self.resolver_sistema(matriz)
        coef_fin = self.calcular_coeficientes_finales(solucion)
        return self.devolver_ecuacion(coef_fin)

if __name__ == '__main__':
    b = Balanceador()
    b.parsear("Fe+O2","2FeO")

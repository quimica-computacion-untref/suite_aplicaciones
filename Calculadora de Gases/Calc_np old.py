import numpy as np
from sympy import Symbol
from sympy.solvers import solve

class CalculadoraGases:

    def calcular(self, presion_inicial, presion_final, temp_inicial, temp_final, vol_inicial, vol_final, cte, calcular):

        unidad = ""

        PI = presion_inicial
        PF = presion_final
        TI = temp_inicial
        TF = temp_final
        VI = vol_inicial
        VF = vol_final

        if cte =="presion":
            PI = PF = 1
        elif cte == "temperatura":
            TI = TF = 1
        elif cte == "volumen":
            VI = VF = 1

        x = Symbol("x")

        if calcular == "presion":
            PF = x
            unidad = "atm"
        elif calcular == "temperatura":
            TF = x
            unidad = "K"
        elif calcular == "volumen":
            VF = x
            unidad = "L"

        eq = ((PI*VI)/TI)-((PF*VF)/TF)
        resultado = solve(eq)
        #return "{0:.3f}".format(resultado[0]) + " " + unidad
        return [resultado[0],unidad]
        


if __name__ == '__main__':
    cal = CalculadoraGases()
    print(cal.calcular(0.8,0,0,0,1.25,0.45,"temperatura","presion"))


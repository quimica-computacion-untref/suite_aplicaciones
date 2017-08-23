import numpy as np
from sympy import Symbol
from sympy.solvers import solve

class CalculadoraGases:

    def calcular(self, presion_inicial, presion_final, temp_inicial, temp_final,
                 vol_inicial, vol_final, cte, calcular, unidadVol, unidadTemp, unidadPresion):

                
        unidad = ""

        
        PI=self.convPresAatm(presion_inicial,unidadPresion)
        PF=self.convPresAatm(presion_final,unidadPresion)
        TI=self.convTempAkelvin(temp_inicial,unidadTemp)
        TF=self.convTempAkelvin(temp_final,unidadTemp)
        VI=self.convVolAlitro(vol_inicial,unidadVol)
        VF=self.convVolAlitro(vol_final,unidadVol)

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
        
    def convPresAatm(self,presion,unidad):
        if unidad=="mmHg":
            return (presion/760)
        else:
            return presion
        

    def convTempAkelvin(self,temperatura,unidad):
        if unidad=="C":
            return (temperatura+273)
        else:
            return temperatura

    def convVolAlitro(self,volumen,unidad):        
        if unidad =="cm3":
            return (volumen/1000)
        else:
            return volumen

if __name__ == '__main__':
    cal = CalculadoraGases()
    print(cal.calcular(0.8,0,0,0,18000,20000,"temperatura","presion","l","C","atm"))


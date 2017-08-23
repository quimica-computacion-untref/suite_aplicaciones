class llenadoOrbitales:

    confElNumeros = [1,2,2,3,3,4,3,4,5,4,5,6,4,5,6,7,5,6,7]
    confElLetras = ["s","s","p","s","p","s","d","p","s","d","p","s","f","d","p","s","f","d","p"]
    limites = {"s":2, "p":6, "d": 10, "f":14}
    
    def calcularOrbitales(self, numero_atomico):
        orbitales = []
        lista_niveles = []
        electrones_ult_nivel = 0
        salida = ""
        cee = ""
        i = 0
        while numero_atomico>0:
            limite = self.limites[self.confElLetras[i]]
            orbitales.append(0)
            while limite >0 and numero_atomico>0:   
                orbitales[i]+=1
                limite -=1
                numero_atomico -=1
            i+=1
        for j in range(len(orbitales)):
            salida+=str(self.confElNumeros[j])+str(self.confElLetras[j])+str(orbitales[j])+" "
            lista_niveles.append(self.confElNumeros[j])
        periodo = max(lista_niveles)
        for k in range(len(orbitales)):
            if self.confElNumeros[k] == periodo:
                electrones_ult_nivel += orbitales[k]
                cee += str(self.confElNumeros[k]) + str(self.confElLetras[k]) + str(orbitales[k]) + " "
        grupo = electrones_ult_nivel
    
        return [salida, cee, periodo, grupo]


if __name__ == "__main__":
    llenado = llenadoOrbitales()
    print(llenado.calcularOrbitales(18))
        

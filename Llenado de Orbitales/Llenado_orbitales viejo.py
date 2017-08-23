
class llenadoOrbitales(object):

    def calcularOrbitales(self,  numAtomico):
        orbitales = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        confElNumeros = [1,2,2,3,3,4,3,4,5,4,5,6,4,5,6,7,5,6,7]
        confElLetras = ["s","s","p","s","p","s","d","p","s","d","p","s","f","d","p","s","f","d","p"]
        
        confElectExterna = ""                             
        
        
        resultado=""
        
        aux=1
        while aux<=numAtomico:
                        
            
            if orbitales[0]<2:
                orbitales[0]+=1              
            elif orbitales[1]<2:
                orbitales[1]+=1              
            elif orbitales[2]<6:
                orbitales[2]+=1              
            elif orbitales[3]<2:
                orbitales[3]+=1               
            elif orbitales[4]<6:
                orbitales[4]+=1                
            elif orbitales[5]<2:
                orbitales[5]+=1          
            elif orbitales[6]<10:
                orbitales[6]+=1               
            elif orbitales[7]<6:
                orbitales[7]+=1               
            elif orbitales[8]<2:
                orbitales[8]+=1                
            elif orbitales[9]<10:
                orbitales[9]+=1
            elif orbitales[10]<6:
                orbitales[10]+=1
            elif orbitales[11]<2:
                orbitales[11]+=1
            elif orbitales[12]<14:
                orbitales[12]+=1
            elif orbitales[13]<10:
                orbitales[13]+=1
            elif orbitales[14]<6:
                orbitales[14]+=1
            elif orbitales[15]<2:
                orbitales[15]+=1
            elif orbitales[16]<14:
                orbitales[16]+=1
            elif orbitales[17]<10:
                orbitales[17]+=1
            elif orbitales[18]<6:
                orbitales[18]+=1
                
            aux+=1
            
        aux=0
        for x in orbitales:
            
            if x>0:                
                          
                resultado+=str(confElNumeros[aux])+confElLetras[aux]+str(x)+" "    
                
            aux+=1
        
        
        aux=0
        ceeMax=0
        periodo=0
        grupo=0
        while aux < len(confElNumeros):
            
            if ceeMax==confElNumeros[aux] and orbitales[aux]!=0:
                
                confElectExterna+= " "+str(confElNumeros[aux]) + confElLetras[aux] + str(orbitales[aux])
                grupo+=orbitales[aux]
                
            
            elif ceeMax<confElNumeros[aux] and orbitales[aux]!=0:                
                
                confElectExterna= str(confElNumeros[aux]) + confElLetras[aux] + str(orbitales[aux]) 
                ceeMax=confElNumeros[aux]
                periodo=ceeMax
                grupo=orbitales[aux]
                
                
                
            aux+=1
        
            

        return [resultado, confElectExterna,periodo,grupo]
        
        
        
            
        
        

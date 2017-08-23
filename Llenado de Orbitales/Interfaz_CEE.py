from tkinter import *
import tkinter.messagebox
from Llenado_orbitales import *



class CEE_Interfaz:

    def __init__(self):

        self.llenadorOrbitales=llenadoOrbitales()

        #ACA VA TODO LO RELACIONADO CON LA VENTANA PRINCIPAL
        self.ventana=Tk()
        self.ventana.title("Llenador de Orbitales")
        self.ventana.geometry("650x210")
        self.ventana.resizable(width=False, height=False)

        #BOTON CALCULAR
        self.botonCalcular=Button(self.ventana,width = 18, height = 1,text="Calcular",
                             font=13,command=self.calcular)       
        

        #ETIQUETAS DE ORIENTACION (NO SE ASIGNAN)
        
        etiquetaNumAtomico=LabelFrame(self.ventana,text="Numero de Electrones",width = 150, height = 45)
        etiquetaNumAtomico.propagate(False)
        
        etiquetaConfigElect=LabelFrame(self.ventana,text="Configuracion Electronica",width = 640, height = 50)
        etiquetaConfigElect.propagate(False)
        
        etiquetaConfigElectExt=LabelFrame(self.ventana,text="Configuracion Electronica Externa",width = 640, height = 50)
        etiquetaConfigElectExt.propagate(False)

        etiquetaPeriodo=LabelFrame(self.ventana,text="Periodo",width = 80, height = 50)
        etiquetaPeriodo.propagate(False)

        etiquetaGrupo=LabelFrame(self.ventana,text="Grupo",width = 80, height = 50)
        etiquetaGrupo.propagate(False)

        #ENTRADAS DE TEXTO
        self.textBoxNumAtomico=Entry(etiquetaNumAtomico)
        
        #ETIQUETAS DE RESULTADOS
        self.etiquetaResCE=Label(etiquetaConfigElect,text="Complete los campos para poder calcular.",font=10)
        self.etiquetaResCEE=Label(etiquetaConfigElectExt,text="",font=13)
        self.etiquetaResPeriodo=Label(etiquetaPeriodo,text="",font=13)
        self.etiquetaResGrupo=Label(etiquetaGrupo,text="",font=13)

               
        #COLOCAMOS EN PANTALLA LOS RECUADROS DE ETIQUETAS DE ORIENTACION   
        etiquetaNumAtomico.place(x=30,y=25) 
        etiquetaConfigElect.place(x=5,y=80)
        etiquetaConfigElectExt.place(x=5,y=150)
        etiquetaPeriodo.place(x=450,y=25)
        etiquetaGrupo.place(x=550,y=25)

        #COLOCACION EN PANTALLA DE LAS ENTRADAS DE TEXTO Y EL BOTON
        self.textBoxNumAtomico.pack()
        self.botonCalcular.place(x=200,y=33)
        

        #COLOCAMOS EN PANTALLA LAS ETIQUETAS DE RESULTADO        
        self.etiquetaResCE.pack()
        self.etiquetaResCEE.pack()
        self.etiquetaResPeriodo.pack()        
        self.etiquetaResGrupo.pack()        
        self.ventana.mainloop()

    def calcular(self):

        #LEVANTA LOS ERRORES SI ESTAN MAL LOS CAMPOS
        
        
        if not(self.textBoxNumAtomico.get().isdigit()):
            tkinter.messagebox.showerror(title = "Error de Numero Atomico", message = "Debe escibir un Numero Atomico valido!")
            return
        
        resultadoTotal = self.llenadorOrbitales.calcularOrbitales(int(self.textBoxNumAtomico.get()))

        
        self.etiquetaResCE.config(text=resultadoTotal[0])
        self.etiquetaResCEE.config(text=resultadoTotal[1])
        self.etiquetaResPeriodo.config(text=resultadoTotal[2])
        self.etiquetaResGrupo.config(text=resultadoTotal[3])



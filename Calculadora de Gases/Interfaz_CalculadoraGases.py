from Calc_np import *
from tkinter import *
import tkinter.messagebox


class Interfaz_CalculadoraGases():
    
    def  __init__(self):

        self.atribConstante = "ninguno"
        
        self.aCalcular= "presion"

        self.resultado= []

        self.calculadora=CalculadoraGases()
               
        #CREAMOS LA VENTANA
        self.ventana=Tk()
        self.ventana.title("Calculadora de Gases Ideales")
        self.ventana.geometry("450x480")
        self.ventana.resizable(width=False, height=False)


        #ETIQUETAS DE ORIENTACION (NO SE ASIGNAN)
        etiquetaPi=LabelFrame(self.ventana,text="Presion Inicial",width = 150, height = 45)
        etiquetaPi.propagate(False)
        
        etiquetaVi=LabelFrame(self.ventana,text="Volumen Inicial",width = 150, height = 45)
        etiquetaVi.propagate(False)
        
        etiquetaTi=LabelFrame(self.ventana,text="Temperatura Inicial",width = 150, height = 45)
        etiquetaTi.propagate(False)

        etiquetaPf=LabelFrame(self.ventana,text="Presion Final",width = 150, height = 45)
        etiquetaPf.propagate(False)
        
        etiquetaVf=LabelFrame(self.ventana,text="Volumen Final",width = 150, height = 45)
        etiquetaVf.propagate(False)
        
        etiquetaTf=LabelFrame(self.ventana,text="Temperatura Final",width = 150, height = 45)
        etiquetaTf.propagate(False)

        etiquetaRadioConst=LabelFrame(self.ventana,text="Condicion Constante",width = 125, height = 120)
        etiquetaRadioConst.propagate(False)

        etiquetaRadioCalc=LabelFrame(self.ventana,text="Calcular",width = 120, height = 100)
        etiquetaRadioCalc.propagate(False)

        etiquetaResultadoFrame=LabelFrame(self.ventana,text="Resultado",width = 390, height = 50)
        etiquetaResultadoFrame.propagate(False)

        #UNIDADES
        self.uPresion = StringVar(self.ventana)
        self.uPresion.set("atm") # default value

        self.uTemp = StringVar(self.ventana)
        self.uTemp.set("K") # default value

        self.uVol = StringVar(self.ventana)
        self.uVol.set("l") # default value

        unidadesPresion = OptionMenu(self.ventana, self.uPresion, "atm","mmHg")
        unidadesVol = OptionMenu(self.ventana, self.uVol, "l","cm3")
        unidadesTemp = OptionMenu(self.ventana, self.uTemp, "K","C")


        #CREAMOS INPUTS DE TEXTO
        self.textBoxPi=Entry(etiquetaPi)
        self.textBoxVi=Entry(etiquetaVi)
        self.textBoxTi=Entry(etiquetaTi)
        self.textBoxPf=Entry(etiquetaPf)
        self.textBoxTf=Entry(etiquetaTf)
        self.textBoxVf=Entry(etiquetaVf)

        #LABEL RESULTADO
        self.etiquetaResultado=Label(etiquetaResultadoFrame,font=40)
        

        #CREAMOS EL BOTON CALCULAR
        self.botonCalcular=Button(self.ventana,width = 30, height = 1,text="Calcular",
                             font=13,command=self.calcular)      

        #CREAMOS EL GRUPO DE RADIO BUTTONS DE EL VALOR CONSTANTE
        self.radioPconst=Radiobutton(etiquetaRadioConst,text="Presion",variable= "group1",value = "Presion",command= self.constPresion)
        self.radioVconst=Radiobutton(etiquetaRadioConst,text="Volumen",variable= "group1",value = "Volumen",command= self.constVolumen)
        self.radioTconst=Radiobutton(etiquetaRadioConst,text="Temperatura",variable= "group1",value = "Temperatura",command= self.constTemperatura)
        self.radioNingunoConst=Radiobutton(etiquetaRadioConst,text="Ninguno",variable= "group1",value = "Ninguno",command= self.constNinguno)

        #CREAMOS EL GRUPO DE RADIO BUTTONS DE LO QUE QUEREMOS CALCULAR
        self.radioPcalc=Radiobutton(etiquetaRadioCalc,text="Presion",variable= "group2",value = "Presion",command= self.calcPresion)
        self.radioVcalc=Radiobutton(etiquetaRadioCalc,text="Volumen",variable= "group2",value = "Volumen",command= self.calcVolumen)
        self.radioTcalc=Radiobutton(etiquetaRadioCalc,text="Temperatura",variable= "group2",value = "Temperatura",command= self.calcTemperatura)

        #COLOCACION EN PANTALLA DE LOS RECUADROS DE ETIQUETAS
        etiquetaPi.place(x=30,y=25)
        etiquetaVi.place(x=30,y=70)
        etiquetaTi.place(x=30,y=115)
        etiquetaPf.place(x=200,y=25)
        etiquetaVf.place(x=200,y=70)
        etiquetaTf.place(x=200,y=115)
        
        etiquetaRadioConst.place(x=200,y=180)
        etiquetaRadioCalc.place(x=30,y=180)

        etiquetaResultadoFrame.place(x=30,y=400)

        #COLOCACION EN PANTALLA DE LOS INPUTS DE TEXTO
        self.textBoxPi.pack()
        self.textBoxVi.pack()
        self.textBoxTi.pack()
        self.textBoxPf.pack()
        self.textBoxTf.pack()
        self.textBoxVf.pack()

        #COLOCAMOS EN PANTALLA LA ETIQUETA RESULTADO
        self.etiquetaResultado.pack()

        #COLOCACION EN PANTALLA DEL BOTON CALCULAR
        self.botonCalcular.place(x=50,y=340)

        #COLOCACION EN PANTALLA DE LOS RADIO BUTTONS CONSTANTE Y CORRECCION DE SELECTEDS
        self.radioNingunoConst.pack(anchor=W)
        self.radioPconst.pack(anchor=W)
        self.radioVconst.pack(anchor=W)
        self.radioTconst.pack(anchor=W)

        self.radioNingunoConst.select()
        self.radioPconst.deselect()
        self.radioVconst.deselect()
        self.radioTconst.deselect()

        #COLOCACION EN PANTALLA DE LOS RADIO BUTTONS A CALCULAR Y CORRECCION DE SELECTEDS
        self.radioPcalc.pack(anchor=W)
        self.radioVcalc.pack(anchor=W)
        self.radioTcalc.pack(anchor=W)

        self.radioPcalc.select()
        self.radioVcalc.deselect()
        self.radioTcalc.deselect()

        self.textBoxPf.config(state=DISABLED) #BLOQUEA LA TEXT ENTRY DE PRESION FINAL AL INICIO DEL PROGRAMA (SOLUCIONA ERROR DE CARGA DE COMPONENTES)
        
        #COLOCAMOS EN PANTALLA LOS SELECTORES DE UNIDADES
        unidadesPresion.place(x=355,y=35)
        unidadesVol.place(x=355,y=80)
        unidadesTemp.place(x=355,y=125)

        
        self.ventana.mainloop()        

   
    
    #FUNCION CALCULAR DEL BOTON
    def calcular(self):

        #INICIALIZAMOS LOS PARAMETROS QUE RECIBE EL METODO A CALCULAR. EN CASO DE QUE SEAN VACIOS SE CONSIDERA EL VALOR COMO "1"
        presionI=1
        presionF=1
        volI=1
        volF=1
        tempI=1
        tempF=1


        #EXCEPCIONES EN CASO DE QUE ALGUN CAMPO DE TEXTO NO SE ESCRIBA O SE ESCRIBA CON CARACTERES INCORRECTOS
        try:        
            presionI=float(self.textBoxPi.get())
            if presionI<0:
                tkinter.messagebox.showerror(title = "Error de Presion Inicial", message = "Asegurese de que las presiones sean positivas!")
                return
        except (ValueError):
            pass
        try:
            presionF=float(self.textBoxPf.get())
            if presionF<0:
                tkinter.messagebox.showerror(title = "Error de Presion Final", message = "Asegurese de que las presiones sean positivas!")
                return
        except (ValueError):
            pass
        try:
            volI=float(self.textBoxVi.get())
            if volI<0:
                tkinter.messagebox.showerror(title = "Error de Volumen Inicial", message = "Asegurese de que los volumenes sean positivos!")
                return
        except (ValueError):
            pass
        try:
            volF=float(self.textBoxVf.get())
            if volF<0:
                tkinter.messagebox.showerror(title = "Error de Volumen Final", message = "Asegurese de que los volumenes sean positivos!")
                return
        except (ValueError):
            pass
        try:
            tempI=float(self.textBoxTi.get())
        except (ValueError):
            pass
        try:
            tempF=float(self.textBoxTf.get())
        except (ValueError):
            pass

        if self.aCalcular==self.atribConstante:
            tkinter.messagebox.showerror(title = "Error al Calcular", message = "Asegurese de no poner como constante el parametro a calcular!")
            return
        
        
        self.resultado = self.calculadora.calcular(presionI,presionF,tempI,tempF,volI,volF,self.atribConstante,
                                                   self.aCalcular,self.uVol.get(),self.uTemp.get(),self.uPresion.get())

        self.etiquetaResultado.config(text=str(self.resultado[0])+" "+self.resultado[1])
        
    #FUNCIONES DE BLOQUEO DE TEXTO POR CONSTANTE
    def constPresion(self):
        self.atribConstante = "presion"
        
        self.textBoxPi.config(state=DISABLED)
        self.textBoxPf.config(state=DISABLED)
        
        self.textBoxVi.config(state=NORMAL)        
        self.textBoxTi.config(state=NORMAL)
        
        if not self.aCalcular=="volumen":
            self.textBoxVf.config(state=NORMAL)  
        if not self.aCalcular=="temperatura":
            self.textBoxTf.config(state=NORMAL)            
            
    def constVolumen(self):
        self.atribConstante = "volumen"
        
        self.textBoxPi.config(state=NORMAL)
        self.textBoxTi.config(state=NORMAL)
        
        self.textBoxVi.config(state=DISABLED)
        self.textBoxVf.config(state=DISABLED)       
        
        if not self.aCalcular=="presion":
            self.textBoxPf.config(state=NORMAL)  
        if not self.aCalcular=="temperatura":
            self.textBoxTf.config(state=NORMAL)
            
    def constTemperatura(self):
        self.atribConstante = "temperatura"
        
        self.textBoxPi.config(state=NORMAL)                    
        self.textBoxVi.config(state=NORMAL)
        
        self.textBoxTi.config(state=DISABLED)
        self.textBoxTf.config(state=DISABLED)
        
        if not self.aCalcular=="volumen":
            self.textBoxVf.config(state=NORMAL)  
        if not self.aCalcular=="presion":
            self.textBoxPf.config(state=NORMAL)

    def constNinguno(self):
        self.atribConstante = "ninguno"
        
        self.textBoxPi.config(state=NORMAL)                    
        self.textBoxVi.config(state=NORMAL)        
        self.textBoxTi.config(state=NORMAL)
        
        if not self.aCalcular=="volumen":
            self.textBoxVf.config(state=NORMAL)  
        if not self.aCalcular=="temperatura":
            self.textBoxTf.config(state=NORMAL)
        if not self.aCalcular=="presion":
            self.textBoxPf.config(state=NORMAL)

    #FUNCIONES DE BLOQUEO DE TEXTO POR SELECCION DE RESULTADO
    def calcPresion(self):
        self.aCalcular = "presion"
        
        self.textBoxPf.config(state=DISABLED)
        
        if not self.atribConstante=="volumen":
            self.textBoxVf.config(state=NORMAL)
        if not self.atribConstante=="temperatura":    
            self.textBoxTf.config(state=NORMAL)
        
    def calcVolumen(self):
        self.aCalcular = "volumen"

        self.textBoxVf.config(state=DISABLED)
        
        if not self.atribConstante=="presion":
            self.textBoxPf.config(state=NORMAL)
        
        if not self.atribConstante=="temperatura":
            self.textBoxTf.config(state=NORMAL)  
        
    def calcTemperatura(self):
        self.aCalcular = "temperatura"
            
        self.textBoxTf.config(state=DISABLED)
        
        if not self.atribConstante=="presion":
            self.textBoxPf.config(state=NORMAL)
        if not self.atribConstante=="volumen": 
            self.textBoxVf.config(state=NORMAL)
         

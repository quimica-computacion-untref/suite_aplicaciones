from tkinter import *
import tkinter.messagebox
from Balanceador_ecu import *
from Exceptions import *


class Balanceador_Interfaz:

    def __init__(self):
        self.balanceador = Balanceador()

        # ACA VA T0DO LO RELACIONADO CON LA VENTANA PRINCIPAL
        self.ventana = Tk()
        self.ventana.title("Balanceador de ecuaciones")
        self.ventana.geometry("650x250")
        self.ventana.resizable(width=False, height=False)

        # BOTON CALCULAR
        self.botonBalancear = Button(self.ventana, width=15, height=2, text="Balancear",
                                     font=13, command=self.calcular)

        # ETIQUETAS DE ORIENTACION (NO SE ASIGNAN)
        etiqueta_reactivos = LabelFrame(self.ventana, text="Reactivos", width=150, height=45)
        etiqueta_reactivos.propagate(False)

        etiqueta_productos = LabelFrame(self.ventana, text="Productos", width=150, height=45)
        etiqueta_productos.propagate(False)

        etiqueta_ecuacion_balanceada = LabelFrame(self.ventana, text="Ecuacion balanceada", width=640, height=50)
        etiqueta_ecuacion_balanceada.propagate(False)

        etiqueta_flecha = Label(self.ventana, text="→", font=30)
        etiqueta_flecha.propagate(False)

        # etiquetaConfigElectExt = LabelFrame(self.ventana, text="Configuracion Electronica Externa", width=640,
        #                                     height=50)
        # etiquetaConfigElectExt.propagate(False)

        # ENTRADAS DE TEXTO
        self.textBoxReactivos = Entry(etiqueta_reactivos)
        self.textBoxProductos = Entry(etiqueta_productos)

        # ETIQUETAS DE RESULTADOS
        self.etiquetaRes = Label(etiqueta_ecuacion_balanceada, text="Complete los campos para poder calcular.", font=10)
        # self.etiquetaResCEE = Label(etiquetaConfigElectExt, text="", font=13)

        # COLOCAMOS EN PANTALLA LOS RECUADROS DE ETIQUETAS DE ORIENTACION
        etiqueta_reactivos.place(x=110, y=25)
        etiqueta_productos.place(x=380, y=25)
        etiqueta_ecuacion_balanceada.place(x=5, y=150)
        etiqueta_flecha.place(x=310, y = 45)
        # etiquetaConfigElectExt.place(x=5, y=230)

        # COLOCACION EN PANTALLA DE LAS ENTRADAS DE TEXTO Y EL BOTON

        self.textBoxReactivos.pack()
        self.textBoxProductos.pack()
        self.botonBalancear.place(x=242, y=80)

        # COLOCAMOS EN PANTALLA LAS ETIQUETAS DE RESULTADO
        self.etiquetaRes.pack()
        # self.etiquetaResCEE.pack()
        self.ventana.mainloop()

    def calcular(self):

        try:
            resultado = self.balanceador.ejecutar(self.textBoxReactivos.get(), self.textBoxProductos.get())
            self.etiquetaRes.config(text=resultado)
        except (EcuacionIncorrectaError, DatosIngresadosIncorrectosError):
            tkinter.messagebox.showerror(title = 'Validar datos ingresados', message = 'Chequear valores ingresados. El programa soporta elementos de la tabla periodica sin parentesis y con coeficientes enteros')
            return

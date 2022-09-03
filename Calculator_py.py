from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

indice = 0

#Entrada de texto
entrada_txt = Entry(ventana, font=("Verdana 20"))
entrada_txt.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#Funciones
def btn_click(valor):
    global indice
    entrada_txt.insert(indice, valor)
    indice += 1

def borrar():
    entrada_txt.delete(0,END)
    indice = 0
    
def ejecutar_operacion():
    operacion = entrada_txt.get()
    resultado = eval(operacion)
    entrada_txt.delete(0,END)
    entrada_txt.insert(0, resultado)
    indice = 0

#Botones
btn1 = Button(ventana, text = "1", width = 5 , height = 2, command= lambda: btn_click(1))
btn2 = Button(ventana, text = "2", width = 5 , height = 2, command= lambda: btn_click(2))
btn3 = Button(ventana, text = "3", width = 5 , height = 2, command= lambda: btn_click(3))
btn4 = Button(ventana, text = "4", width = 5 , height = 2, command= lambda: btn_click(4))
btn5 = Button(ventana, text = "5", width = 5 , height = 2, command= lambda: btn_click(5))
btn6 = Button(ventana, text = "6", width = 5 , height = 2, command= lambda: btn_click(6))
btn7 = Button(ventana, text = "7", width = 5 , height = 2, command= lambda: btn_click(7))
btn8 = Button(ventana, text = "8", width = 5 , height = 2, command= lambda: btn_click(8))
btn9 = Button(ventana, text = "9", width = 5 , height = 2, command= lambda: btn_click(9))
btn0 = Button(ventana, text = "0", width = 13 , height = 2, command= lambda: btn_click(0))

btn_borrar = Button(ventana, text = "C", width = 5 , height = 2, command= lambda: borrar())
btn_abrirParentesis = Button(ventana, text = "(", width = 5 , height = 2, command= lambda: btn_click("("))
btn_cerrarParentesis = Button(ventana, text = ")", width = 5 , height = 2, command= lambda: btn_click(")"))
btn_punto = Button(ventana, text = ".", width = 5 , height = 2, command= lambda: btn_click("."))

btn_division = Button(ventana, text = "/", width = 5 , height = 2, command= lambda: btn_click("/"))
btn_multiplicacion = Button(ventana, text = "x", width = 5 , height = 2, command= lambda: btn_click("*"))
btn_suma = Button(ventana, text = "+", width = 5 , height = 2, command= lambda: btn_click("+"))
btn_resta = Button(ventana, text = "-", width = 5 , height = 2, command= lambda: btn_click("-"))
btn_igual = Button(ventana, text = "=", width = 5 , height = 2, command= lambda: ejecutar_operacion())

#Enviar botones a interfaz 
# (fila 1)
btn_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
btn_abrirParentesis.grid(row = 1, column = 1, padx = 5, pady = 5)
btn_cerrarParentesis.grid(row = 1, column = 2, padx = 5, pady = 5)
btn_division.grid(row =1, column = 3, padx = 5, pady = 5)
# (fila 2)
btn7.grid(row = 2, column = 0, padx = 5, pady = 5)
btn8.grid(row = 2, column = 1, padx = 5, pady = 5)
btn9.grid(row = 2, column = 2, padx = 5, pady = 5)
btn_multiplicacion.grid(row =2, column = 3, padx = 5, pady = 5)
# (fila 3)
btn4.grid(row = 3, column = 0, padx = 5, pady = 5)
btn5.grid(row = 3, column = 1, padx = 5, pady = 5)
btn6.grid(row = 3, column = 2, padx = 5, pady = 5)
btn_suma.grid(row = 3, column = 3, padx = 5, pady = 5)
# (fila 4)
btn1.grid(row = 4, column = 0, padx = 5, pady = 5)
btn2.grid(row = 4, column = 1, padx = 5, pady = 5)
btn3.grid(row = 4, column = 2, padx = 5, pady = 5)
btn_resta.grid(row = 4, column = 3, padx = 5, pady = 5)
# (fila 5)
btn0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
btn_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
btn_igual.grid(row = 5, column = 3, padx = 5, pady = 5)


ventana.mainloop()
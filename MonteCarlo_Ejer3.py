from tkinter import *
import tkinter as tk
from tkinter import ttk
import math
from random import uniform

#Jose Estefania Estrada Aguilar
#Elizabeth Lucas García
#Inés del Carmen Gonzaléz Gonzaléz
#Yamileth García Perez

v = Tk()
v.title("MONTECARLO - EJERCICIO3")
v.geometry("700x400+300+10")
v.configure(background="hotpink4")
probabilidades = [0.10, 0.40, 0.35, 0.15]
camiones = [0, 1, 2, 3]
intervalos = []

headers = ('Iteración')
t1 = ttk.Treeview(v, height=4, columns=headers)
t1.place(x=10, y=10)
t1.heading('#0', text='Probabilidad', anchor='center')
t1.heading('#1', text='No. camiones', anchor='center',)
t1.column('#0', width=120, anchor='center')
t1.column('#1', width=120, anchor='center')
for i in range(len(probabilidades)):
    t1.insert('', i, text=str(probabilidades[i]), values=str(camiones[i]))

headers2 = ('Iteración', 'uno')
t2 = ttk.Treeview(height=4, columns=headers2)
t2.place(x=280, y=10)
t2.heading('#0', text='Lm', anchor='center')
t2.heading('#1', text='Ls', anchor='center')
t2.heading('#2', text='No. camiones',  anchor='center')
t2.column('#0', width=80, anchor='center')
t2.column('#1', width=80, anchor='center')
t2.column('#2', width=80, anchor='center')

def calcular():
        headers3 = ('ALEATORIO', 'NO. CAMIONES', 'CAM. ALQUILADOS', 'RESULTADO')
        t3 = ttk.Treeview(v, height = 5, columns = headers3)
        t3.place(x=10, y=150)
        
            
        t3.heading('#0', text = 'Día', anchor = 'center')
        t3.heading('#1', text = 'Valor aleatorio', anchor = 'center')
        t3.heading('#2', text = 'No. camiones', anchor = 'center')
        t3.heading('#3', text = 'No. camiones alquilados', anchor = 'center')
        t3.heading('#4', text = "resultado", anchor = 'center')
        t3.column('#0', width = 50, anchor = 'center')
        t3.column('#1', width = 100, anchor = 'center')
        t3.column('#2', width = 100, anchor = 'center')
        t3.column('#3', width = 170, anchor = 'center')
        t3.column('#4', width = 250, anchor = 'center')  
        #print(semilla)
        i=0
        aleatorios=[]
        camiones1 = [0, 1, 2, 3]
        acumulador = 0
        for i in range(len(probabilidades)):
            t2.insert('', i, text=str(acumulador), values=[str(acumulador + probabilidades[i]), camiones1[i]])
            acumulador = acumulador + probabilidades[i]
            intervalos.insert(i, acumulador)
        #print(intervalos)
        while(i<10):
            aleatorios.append(uniform(0,1))
            i+=1
        
        for i in range(len(aleatorios)):
            camiones = 0
            for k in range(len(intervalos)):
                if aleatorios[i]< intervalos[k]:
                    camiones = camiones1[k]
                    break
            unCamion = 0
            dosCamiones = 0
            resultado = ""
            if camiones <= 1:
                unCamion = 150
            else:
                unCamion = 150 + (camiones - 1) * 250

            if camiones <= 2:
                dosCamiones = 150 + 175
            else:
                dosCamiones = 150 + 175 + (camiones - 2) * 250
            if(dosCamiones > unCamion):
                resultado = "Es preferible seguir como hasta la fecha"
            else:
                resultado = "Si conviene comprar otro camión"
            t3.insert('', i, text=i + 1, values=[str(aleatorios[i]), camiones, camiones - 1, resultado])
      
cal = Button(v, text="Calcular", width=50, bg="black",fg="white", command=calcular)
cal.place(x=10,y=300)
v.mainloop()

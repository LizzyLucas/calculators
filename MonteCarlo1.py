from tkinter import *
from random import uniform 
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("MÉTODO MONTECARLO: EJERCICIO 2")
root.geometry('790x680+400+5')
#root.resizable(False, True)
root.configure(background="hotpink4")


lbl1=tk.Label(root,text='La evolución del valor de unas acciones \n varia diariamente siguiendo el siguiente esquema', background="gold")
lbl1.place(x=25,y=10)

area=('Cambio de la cotización', 'Probabilidad')

ac=('all','n')
sales_data=[('-1/8','3/36'),
            ('sin cambios','7/36'),
            ('+1/8','16/36'),
            ('+1/2','7/36'),
            ('+1','3/36')
            ]

tv=ttk.Treeview(root,columns=ac,show='headings',height=5)
for i in range(2):
    tv.column(ac[i],width=140,anchor='center', stretch=tk.NO)
    tv.heading(ac[i],text=area[i])
tv.place(x=20,y=60)

for i in range(5):
    tv.insert('','end',values=sales_data[i])
    

def intervalos():
    a4=[]
    a5=[]
    i=0
    sum=0
    while(i<len(sales_data)):
        a=sales_data[i][1].split('/')
        int(a.pop())
        a4.append(a)
        i+=1
    i=0
    while(i<len(a4)):
       sum+=int(a4[i][0])
       a5.append(sum)
       i+=1
    return(a5)

def simIntervalos():
     i=0
     a1=[]
     a2=[]
     a=intervalos()
     while(i<len(sales_data)):
          if(i==0):
              a1.append(0)
              a1.append(f"{a[i]}/36")
              a1.append(sales_data[i][0])
              
          else:
              a1.append(f"{a[i-1]}/36")
              a1.append(f"{a[i]}/36")
              a1.append(sales_data[i][0])
          b=tuple(a1)
          a2.append(b)
          a1.clear()
          i+=1         
     return a2

def interPorcentajes():
    a=intervalos()
    b=[]
    c=[]
    e=[]
    i=0
    while(i<len(a)):
        if(i==0):
            b.append(0)
        b.append(float((a[i])/36)*100)
        i+=1
    i=0
    while(i<len(b)-1):
        c.append(b[i])
        c.append(b[i+1])
        d=tuple(c)
        e.append(d)
        c.clear();
        i+=1
    return e

def simulacion():
    b=[]
    d=[]
    a=interPorcentajes()
    j=0
    accion=100
    while(j<31):
        na=uniform(0,1)
        na=na*100
        if(j==0):
            b.append(j)
            b.append("-")
            b.append("inicial")
            b.append(accion)
            c=tuple(b)
        elif(na>a[1][0] and na<a[1][1]):
            accion=accion-(accion/8)
            b.append(j)
            b.append(na)
            b.append("-1/8")
            b.append(accion)
            c=tuple(b)
        elif(na>a[2][0] and na<a[2][1]):
            accion=accion
            b.append(j)
            b.append(na)
            b.append("n/a")
            b.append(accion)
            c=tuple(b)
        elif(na>a[3][0] and na<a[3][1]):
            accion=accion+(accion/8)
            b.append(j)
            b.append(na)
            b.append("+1/8")
            b.append(accion)
            c=tuple(b)
        elif(na>a[4][0] and na<a[4][1]):
            accion=accion+(accion/2)
            b.append(j)
            b.append(na)
            b.append("+1/2")
            b.append(accion)
            c=tuple(b)
        else:
            accion=2*accion
            b.append(j)
            b.append(na)
            b.append("+1")
            b.append(accion)
            c=tuple(b)
        j+=1
        d.append(c)
        b.clear()
    return d

#print(len(simulacion()))                
#print(interPorcentajes())
#intervalos()
tk.Label(root,text='Probabilidades acumuladas', background="gold").place(x=90, y=200)
area1=('Li', 'Ls', 'Cambio')
ac1=('all','n', 'e')
sales_data1=simIntervalos()
#print(sales_data1)
tv1=ttk.Treeview(root,columns=ac1,show='headings',height=5)
for i in range(3):
    tv1.column(ac1[i],width=80,anchor='center', stretch=tk.NO)
    tv1.heading(ac1[i],text=area1[i])
tv1.place(x=40, y=235)

for i in range(5):
    tv1.insert('','end',values=sales_data1[i])

####################
tk.Label(root,text='Simulación de la evolución de las acciones a lo largo del mes.', background="gold").place(x=385,y=10)
tk.Label(root,text='CONCLUSIÓN DE LA SIMULACIÓN', background="gold").place(x=70,y=440)



def tabla():
    area2=('Día', 'Aleatorio', 'Cambio', 'Acción')
    ac2=('all','n', 'e', 's')
    sales_data2=simulacion()
    
    tv2=ttk.Treeview(root,columns=ac2,show='headings',height=len(sales_data2))
    for i in range(4):
        tv2.column(ac2[i],width=110,anchor='center', stretch=tk.NO)
        tv2.heading(ac2[i],text=area2[i])
    tv2.place(x=320,y=30)
    
    for i in range(31):
        tv2.insert('','end',values=sales_data2[i])
    #print(sales_data2[len(sales_data2)-1][3])
    tk.Label(root, fg="black", text=f"Valor de la acción al final de mes:\n {sales_data2[len(sales_data2)-1][3]}", background="SkyBlue2",  font = ("centuri gothic", 14)).place(x=15,y=480)
    
    

#mb.showinfo("CONCLUSIÓN DE LA SIMULACIÓN", f"Valor de la acción al final de mes: {sales_data2[len(sales_data2)-1][3]}")
tk.Button(root,fg="white", text="Resultado", bg="purple3", width=33, height=1, command=tabla).place(x=40,y=400)


root.mainloop()

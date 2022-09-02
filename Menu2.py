# IMPORTAR
from tkinter import *
import math
import statistics
import scipy.stats as ss
from tkinter import messagebox as mb

# FUNCIONES

        
def medias(ls, a):
    media=sum(ls)/int(len(ls))
    pe=1-(a/2)
    #pe=probabilidad estadistica# 
    Z=statistics.NormalDist().inv_cdf(pe)
    Li=(1/2)-Z*(1/(math.sqrt(12*(int(len(ls))))))
    Ls=(1/2)+Z*(1/(math.sqrt(12*int((len(ls))))))
    # print(f"Media: {media} \nProb Est: {pa} \nZ: {Z} \nLi: {Li} \nLs: {Ls}")
    if(media>=Li and media<=Ls):
        mb.showinfo("Prueba de Media", "La media SÍ está en el rango de confianza")
    else:
        mb.showwarning("Prueba de Media", "La media NO está en el rango de confianza")

def varianza(ls, a): #Definimos la función recibiendo la lista de las semillas y el nivel de confianza
    n=len(ls) #n: cantidad de semillas
    v=statistics.variance(ls) #Calcular varianza de las semillas
    a2=a/2 #salcar alfa medios
    Li=(ss.chi2.isf(1-a2,n-1))/(12*(n-1)) #desarrollamos toda la formula en cuestión para Li siendo Xi2(1-a2,n-1)/(12*(n-1))
    Ls=(ss.chi2.isf(a2,n-1))/(12*(n-1)) #Sacamos Ls, quitando el 1-
    #print(f"Var= {v} \nLi={Li} \nLs={Ls}")
    if(v>=Li and v<=Ls): #verificamos si está en el intervalo
        mb.showinfo("Prueba de Varianza","La varianza SÍ está en el rango de confianza")
    else:
        mb.showwarning("Prueba de Varianza","La varianza NO está en el rango de confianza")

def chiCuadrada(ls, alfa):
    
    n=len(ls) #n=tamaño de la lista
    m=int(math.sqrt(n)) #Raiz cuadrada de n que nos define cuantos intervalos vamos a tener
    a=m/n #a= amplitud del intervalo
    Ei=n/m #Valor de Frecuencia 
    oi=0; #Numero de semillas que se encuentran en los intervalos
    l=0 #Limite debe estar en 0 y debe llegar a 1
    intervalos =[] #Creación de array para los inetrvalos
    i=0 #Inicializador del while
    f=0 #Donde se guardaron los valores finales LA SUMA
    #j=0
    #print(f"n:{n}\nm:{m}\na:{a}\n")
    try:
        while(l<=1): #Cuando el limite llegue a 1 debe parar ya que se debe evaluar entre 0 y 1
            intervalos.append(l) #Vamos a añadir los intervalos
            l=round(l+a, 1) #El intervalo debe ir creciendo conforme a la amplitud
        #print(intervalos)
        #print(len(intervalos))
        while(i<m): #Recorrer los intervalos#
            #print(i)
            if(i!=m):
                    #print("ENtra")
                for sem in range(len(ls)): #Recorremos las smeilas de la lista
                    #j+=1
                    #print(j)
                    if(ls[sem]>intervalos[i] and ls[sem]<intervalos[i+1]): #Evaluamos si los numeros en cuestios estan entre los intervalos#
                        #print()
                        #print(f"a: {intervalos[i]} b: {intervalos[i+1]}")
                        oi+=1#Guardamos el numeor de veces que aparecen las smeillas en el intervalo#
            #print(f"Oi:{oi}")
            #j=0
            f+=(math.pow((Ei-oi),2))/Ei#Aplicamos esta formula y lo vamos umando todo
            oi=0 #regresamos a 0 para la siguiente vuelta
            i+=1
        if(ss.chi2.isf(alfa,m-1)>f):
            mb.showinfo("Prueba de Chi-Cuadrada","Los números SÍ se aceptan pues son uniformes")
        else:
            mb.showwarning("Prueba de Chi-Cuadrada","Los números NO se aceptan pues no son uniformes")

    except:
        mb.showwarning("Prueba de Chi-Cuadrada","Los números NO se aceptan pues no son uniformes")
    #print(ss.chi2.isf(alfa,m-1))
   
def es_flotante(v):
	try:
		float(v)
		return True
	except:
		return False
    
def validarAlpha(txtA, lp, btn, op):
    if(txtA.get()=="" or es_flotante(txtA.get())==False):
        mb.showwarning("Advertencia", "Rellene el campo de ALPHA con un valor FLOTANTE")
    elif(len(lp)==0):
        mb.showwarning("Advertencia", "La lista de semillas nuevas está vacía")
    else:
        try:
            #txtA=float(txtA.get())
            if(op=="m"):
                btn["command"]=lambda:medias(lp, float(txtA.get()))
                
            elif(op=="v"):
                btn["command"]=lambda:varianza(lp, float(txtA.get()))
            elif(op=="c"):
                    btn["command"]=lambda:chiCuadrada(lp, float(txtA.get()))
        except:
             mb.showerror("Error", "Intentelo de nuevo" )

#FUNCIONE MÉTODOS NUMEROS

def algoritmoLineal():
    
    #variables
    global vA_Lineal
    global calcular
    global txtX0
    #ventana
    vA_Lineal = Toplevel(ventana)
    vA_Lineal.title("ALGORITMO LINEAL")
    vA_Lineal.geometry("650x400+400+100")
    vA_Lineal.resizable(False, True)
    vA_Lineal.configure(background="gray19")    
    #widgets de entrada
    lblAlpha = Label(vA_Lineal, text="α: ")
    lblAlpha.place(x=242, y=2)
    txtAlpha = Entry(vA_Lineal)
    txtAlpha.place(x=270, y=2)
    txtAlpha.config(justify="center")
    
    lblX0 = Label(vA_Lineal, text="Valor de la semilla (X0): ")
    lblX0.place(x=130, y=30)
    txtX0 = Entry(vA_Lineal)
    txtX0.place(x=270, y=30)
    txtX0.config(justify="center")

    lblA = Label(vA_Lineal, text="Constante multiplicativa (a): ")
    lblA.place(x=103, y=60)
    txtA = Entry(vA_Lineal)
    txtA.place(x=270, y=60)
    txtA.config(justify="center")

    lblC = Label(vA_Lineal, text="Constante aditiva (c): ")
    lblC.place(x=141, y=90)
    txtC = Entry(vA_Lineal)
    txtC.place(x=270, y=90)
    txtC.config(justify="center")

    lblM = Label(vA_Lineal, text="Valor del modulo(m): ")
    lblM.place(x=140, y=120)
    txtM = Entry(vA_Lineal)
    txtM.place(x=270, y=120)
    txtM.config(justify="center")
    
     #listas de resultados
    lblItera = Label(vA_Lineal, fg="yellow", background="maroon4", font=(
        "centuri gothic", 10), text="Item:")
    lblItera.place(x=30, y=150)
        
    lstItera = Listbox(vA_Lineal, width=8)
    lstItera.place(x=30, y=170)
    lstItera.yview()

    lblRes = Label(vA_Lineal, fg="yellow", background="maroon4", font=(
        "centuri gothic", 10), text="Resultado:")
    lblRes.place(x=120, y=150)
    lstRes = Listbox(vA_Lineal, width=20)
    lstRes.place(x=120, y=170)
    lstRes.yview()

    lblModulo = Label(vA_Lineal, fg="yellow", background="maroon4", font=(
        "centuri gothic", 10), text="Módulo:")
    lblModulo.place(x=275, y=150)
    lstModulo = Listbox(vA_Lineal, width=20)
    lstModulo.place(x=275, y=170)
    lstModulo.yview()

    lblPorcentaje = Label(vA_Lineal, fg="yellow", font=("centuri gothic", 10),
                      background="maroon4", text="Porcentaje: %")
    lblPorcentaje.place(x=430, y=150)
    lstPorcentaje = Listbox(vA_Lineal, width=20)
    lstPorcentaje.place(x=430, y=170)
    lstPorcentaje.yview()

    lblIter = Label(vA_Lineal, fg="yellow", background="maroon4", font=(
        "centuri gothic", 10), text="Total de iteraciones:")
    lblIter.place(x=30, y=350)
    listaPorcentaje=[]
    def alF():
    #FUNCIÓN
        # btnJi["state"]="active"
        # btnVarianza["state"]= "active"
        # btnMedia["state"]="active"
        listaProducto=[]
        listaResiduo=[]
       
        X0 = txtX0.get()
        a = txtA.get()
        c = txtC.get()
        m = txtM.get()
        X0 = int(X0)
        a = int(a)
        c = int(c)
        m = int(m)
        res = 0
        x = X0
        i = 0
    
        while(x != res):
            prod = (a*X0+c)
            res = prod % m
            porc = res/(m-1)
            listaProducto.append(prod)  # Resultado
            listaResiduo.append(res)  # Modulo
            listaPorcentaje.append(porc)  # Porcentaje
            lstRes.insert(i, listaProducto[i])
            lstModulo.insert(i, listaResiduo[i])
            lstPorcentaje.insert(i, listaPorcentaje[i])
            lstItera.insert(i, i+1)
            X0 = res
            i += 1
            lblIter1 = Label(vA_Lineal, fg="yellow", background="maroon4", font=(
            "centuri gothic", 10), text=str(i))
            lblIter1.place(x=160, y=350)

    #botones
    calcular = Button(vA_Lineal, fg="yellow", text="Calcular", font=("centuri gothic", 10,
                                                                 "bold"), bg="purple3", width=8, height=1, command=alF)
    calcular.place(x=410, y=50)
    btnMedia = Button(vA_Lineal, fg="yellow", text="Media", font=(
        "centuri gothic", 10, "bold"), bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha, listaPorcentaje, btnMedia,"m")).place(x=570, y=50)
    btnVarianza = Button(vA_Lineal, fg="yellow", text="Varianza", font=(
        "centuri gothic", 10, "bold"), bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnVarianza,"v")).place(x=490, y=50)
    btnJi = Button(vA_Lineal, fg="yellow", text="JiCuadrada", font=(
        "centuri gothic", 10, "bold"), bg="purple3",  width=10, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnJi,"c") ).place(x=485, y=85)
       
def c_Aditivo():
    vc_Aditivo = Tk()
    vc_Aditivo.title("CONGRUENCIAL ADITIVO")
    vc_Aditivo.geometry("670x400")
    vc_Aditivo.resizable(False, True)
    vc_Aditivo.configure(background="gray19")

    listaSumas = []
    listaPorcentajes = []
    listaResiduos = []
    listaSemillas = []
    # WIDGETS
    # Ns numeros de las semilla
    lblNs = Label(vc_Aditivo, text="¿Cuántas semillas desea ingresar?: ")
    lblNs.place(x=50, y=30)
    txtNs = Entry(vc_Aditivo)
    txtNs.place(x=270, y=30)
    txtNs.config(justify="center")
    
    lblMod = Label(vc_Aditivo, text="Módulo: ")
    lblMod.place(x=206, y=60)
    txtMod = Entry(vc_Aditivo)
    txtMod.place(x=270, y=60)
    txtMod.config(justify="center")
    
    lblNp = Label(vc_Aditivo, text="Cantidad de números pseudoaltatorios: ")
    lblNp.place(x=43, y=90)
    txtNp = Entry(vc_Aditivo)
    txtNp.place(x=270, y=90)
    txtNp.config(justify="center")
    
    lblAlpha = Label(vc_Aditivo, text="α: ")
    lblAlpha.place(x=240, y=120)
    txtAlpha = Entry(vc_Aditivo)
    txtAlpha.place(x=270, y=120)
    txtAlpha.config(justify="center")
    
    
    lblSemilla = Label(vc_Aditivo, background="maroon4", font=(
        "centuri gothic", 10), text="Semillas:")
    lblSemilla.place(x=40, y=150)
    lstSemilla = Listbox(vc_Aditivo, width=20)
    lstSemilla.place(x=40, y=170)
    lstSemilla.yview()
    
    lblSumas = Label(vc_Aditivo, background="maroon4", font=(
        "centuri gothic", 10), text="Sumas:")
    lblSumas.place(x=175, y=150)
    lstSumas = Listbox(vc_Aditivo, width=20)
    lstSumas.place(x=175, y=170)
    lstSumas.yview()
    
    lblResiduo = Label(vc_Aditivo, background="maroon4", font=(
        "centuri gothic", 10), text="Residuos:")
    lblResiduo.place(x=310, y=150)
    lstResiduo = Listbox(vc_Aditivo, width=20)
    lstResiduo.place(x=310, y=170)
    lstResiduo.yview()
    
    lblPorcentaje = Label(vc_Aditivo, font=("centuri gothic", 10),
                          background="maroon4", text="Porcentajes: %")
    lblPorcentaje.place(x=445, y=150)
    lstPorcentaje = Listbox(vc_Aditivo, width=20)
    lstPorcentaje.place(x=445, y=170)
    lstPorcentaje.yview()
    
    lblIter = Label(vc_Aditivo, background="maroon4", font=(
        "centuri gothic", 10), text="Total de iteraciones:")
    lblIter.place(x=30, y=350)
    lblIter1 = Label(vc_Aditivo, background="maroon4", font=(
        "centuri gothic", 10), text="0")
    lblIter1.place(x=160, y=350)
    
    def congAditivo():
        ns= txtNs.get()
        m= txtMod.get()
        n=txtNp.get()
        
        ns=int(ns)
        m= int(m)
        n= int(n)  
        i=0
        mod=m-1
        k=0
        vn= Toplevel(vc_Aditivo)
        while(k < ns):
            vn.withdraw()
            vn.resizable(False, True)
            semilla = simpledialog.askstring(title="SEMILLAS",prompt="Ingresa el valor de la semilla: " + str(k+1))
            listaSemillas.append(int(semilla))
            k+=1
        #vn.resizable(False, False)
    # check it out
            #print("Hello", semilla)
        print("salió")
        while(i<n):
            e=len(listaSemillas)-1
            suma=listaSemillas[e]+listaSemillas[i]
            resi=suma%m
            listaSemillas.append(resi)
            listaSumas.append(suma)
            listaResiduos.append(resi)
            porc=resi/mod
            listaPorcentajes.append(porc)
            lstSemilla.insert(i, resi)
            lstSumas.insert(i, suma)
            lstResiduo.insert(i, resi)
            lstPorcentaje.insert(i, porc)
            #print("Semillas ", listaSemillas[ns:], "Sumas ", listaSumas, "Residuos", listaResiduos, "Porcentajes", listaPorcentajes)
            i=i+1
            lblIter1["text"]=str(i)
        
    calcular = Button(vc_Aditivo,fg="yellow", text="Calcular", font=("centuri gothic",10,"bold"),bg="purple3", width=8,height=1, command=congAditivo).place(x=410, y=50)
    btnVarianza= Button(vc_Aditivo,fg="yellow", text="Varianza", font=("centuri gothic",10,"bold"),bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentajes, btnVarianza,"v")).place(x=490, y=50)
    btnMedia= Button(vc_Aditivo, fg="yellow",text="Media", font=("centuri gothic",10,"bold"),bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha, listaPorcentajes, btnMedia,"m")).place(x=570, y=50)
    btnJi= Button(vc_Aditivo, fg="yellow", text="JiCuadrada", font=("centuri gothic",10,"bold"), bg="purple3",  width=10, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentajes, btnJi,"c")).place(x=485, y=85)
    

def congMultiplicativo_vm():
    global v_Cmulti
    v_Cmulti= Toplevel(ventana)
    v_Cmulti.title("CONGRUENCIAL MULTIPLICATIVO")
    v_Cmulti.geometry("600x400+400+100")
    v_Cmulti.resizable(False, True)
    v_Cmulti.configure(background="gray19")
    # variables
    listaProducto=[]
    listaResiduo=[]
    listaPorcentaje=[]
    # wigets
    lblT = Label(v_Cmulti, font = ("centuri gothic", 12), fg="yellow",text="Considere que la semilla debe ser > 0 y debe ser impar.")
    lblT.place(x=100, y=10)
    lblT.config(background="maroon4", justify="center",)

    lblSem = Label(v_Cmulti,font="bold", text="Semilla: ")
    lblSem.place(x=116, y=25)
    txtSem = Entry(v_Cmulti)
    txtSem.place(x=195, y=25)
    txtSem.config(justify="center")
    
    lblAlpha = Label(v_Cmulti,font="blod", text="α: ")
    lblAlpha.place(x=160, y=52)
    txtAlpha = Entry(v_Cmulti)
    txtAlpha.place(x=195, y=52)
    txtAlpha.config(justify="center")

    lblk = Label(v_Cmulti, font="bold",text="k: ")
    lblk.place(x=160, y=82)
    txtk = Entry(v_Cmulti)
    txtk.place(x=195, y=82)
    txtk.config(justify="center")

    lblG = Label(v_Cmulti,font="bold", text="g: ")
    lblG.place(x=160, y=112)
    txtG = Entry(v_Cmulti)
    txtG.place(x=195, y=112)
    txtG.config(justify="center")

    lblItera = Label(v_Cmulti, fg="yellow",background="maroon4", font = ("centuri gothic", 10), text="Item:")
    lblItera.place(x=30, y=140)
    lstItera = Listbox(v_Cmulti, width=8)
    lstItera.place(x=30, y=160)
    lstItera.yview()

    lblRes = Label(v_Cmulti, fg="yellow",background="maroon4", font = ("centuri gothic", 10), text="Resultado:")
    lblRes.place(x=120, y=140)
    lstRes = Listbox(v_Cmulti, width=20)
    lstRes.place(x=120, y=160)
    lstRes.yview()

    lblMod = Label(v_Cmulti,fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Mod:")
    lblMod.place(x=275, y=140)
    lstMod = Listbox(v_Cmulti, width=20)
    lstMod.place(x=275, y=160)
    lstMod.yview()

    lblPorcentaje = Label(v_Cmulti,fg="yellow", font = ("centuri gothic", 10), background="maroon4",text="Porcentaje: %")
    lblPorcentaje.place(x=430, y=140)
    lstPorcentaje = Listbox(v_Cmulti, width=20)
    lstPorcentaje.place(x=430, y=160)
    lstPorcentaje.yview()

    lblIter1 = Label(v_Cmulti, fg="yellow",background="maroon4", font = ("centuri gothic", 10), text="Total de iteraciones:")
    lblIter1.place(x=30, y=340)

    def cmF():
        X0= txtSem.get()
        k=txtk.get()
        g=txtG.get()
        X0=int(X0)
        k=int(k)
        g=int(g)
        x=X0
        res=0
        i=0
        while(x!=res):
            a=5+(8*k)
            m=pow(2,g)
            prod=a*X0
            res=prod%m
            porc=res/(m-1)
            listaProducto.append(prod)
            listaResiduo.append(res)
            listaPorcentaje.append(porc)
            lstRes.insert(i, listaProducto[i])
            lstMod.insert(i, listaResiduo[i])
            lstPorcentaje.insert(END, listaPorcentaje[i])
            lstItera.insert(i, i+1)
            X0=res
            i += 1
            lblIter2 = Label(v_Cmulti, background="maroon4", font = ("centuri gothic", 10),fg="yellow", text=str(i))
            lblIter2.place(x=160, y=340)
            
    calcular = Button(v_Cmulti,fg="yellow", text="Calcular", font=("centuri gothic",10,"bold"),bg="purple3", width=8,height=1, command=cmF).place(x= 330, y=55)
    btnVarianza= Button(v_Cmulti,fg="yellow", text="Varianza", font=("centuri gothic",10,"bold"),bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnVarianza,"v")).place(x=410, y=55)
    btnMedia= Button(v_Cmulti, fg="yellow",text="Media", font=("centuri gothic",10,"bold"),bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha, listaPorcentaje, btnMedia,"m")).place(x=490, y=55)
    btnJi= Button(v_Cmulti, fg="yellow", text="JiCuadrada", font=("centuri gothic",10,"bold"), bg="purple3",  width=10, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnJi,"c")).place(x=405, y=95)

def congCuadratico_vm():
    # ventana
    v = Tk()
    v.title("CONGRUENCIAL CUADRÁTICO")
    v.geometry("600x400+400+100")
    v.resizable(False, True)
    v.configure(background="gray19")
    
    lblX0 = Label(v, text="X0: ")
    lblX0.place(x=57, y=70)
    txtX0 = Entry(v)
    txtX0.place(x=90, y=70)
    txtX0.config(justify="center")
    
    lblM = Label(v, text="m: ")
    lblM.place(x=60, y=100)
    txtM = Entry(v)
    txtM.place(x=90, y=100)
    txtM.config(justify="center")
    
    lblA = Label(v, text="a: ")
    lblA.place(x=230, y=70)
    txtA = Entry(v)
    txtA.place(x=255, y=70)
    txtA.config(justify="center")
    
    lblB = Label(v, text="b: ")
    lblB.place(x=230, y=100)
    txtB = Entry(v)
    txtB.place(x=255, y=100)
    txtB.config(justify="center")
    
    lblC = Label(v, text="c: ")
    lblC.place(x=400, y=70)
    txtC = Entry(v)
    txtC.place(x=425, y=70)
    txtC.config(justify="center")
    
    lblAlpha = Label(v, text="α: ")
    lblAlpha.place(x=400, y=100)
    txtAlpha = Entry(v)
    txtAlpha.place(x=425, y=100)
    txtAlpha.config(justify="center")
    
    
    lblSemilla = Label(v,fg="yellow",  background="maroon4", font=(
        "centuri gothic", 10), text="Semillas:")
    lblSemilla.place(x=120, y=150)
    lstSemilla = Listbox(v, width=20)
    lstSemilla.place(x=120, y=170)
    lstSemilla.yview()
    
    lblSumas = Label(v,fg="yellow",  background="maroon4", font=(
        "centuri gothic", 10), text="Considere las siguientes condiciones: m<29, 'a' debe ser par, 'c' debe ser impar \ntodos deben ser enteros")
    lblSumas.place(x=70, y=10)
   
    
    lblPorcentaje = Label(v,fg="yellow",  font=("centuri gothic", 10),
                          background="maroon4", text="Semillas nuevas: " )
    lblPorcentaje.place(x=270, y=150)
    lstPorcentaje = Listbox(v, width=20)
    lstPorcentaje.place(x=270, y=170)
    lstPorcentaje.yview()
    
    lblIter = Label(v,fg="yellow",  background="maroon4", font=(
        "centuri gothic", 10), text="Total de iteraciones:")
    lblIter.place(x=60, y=350)
    lblIter1 = Label(v, fg="yellow", background="maroon4", font=(
        "centuri gothic", 10), text="0")
    lblIter1.place(x=190, y=350)
    
    
    Semillas=[]
    def congC():
        btnJi["state"]="active"
        btnVarianza["state"]= "active"
        btnMedia["state"]="active"
        X0=int(txtX0.get())
        m=int(txtM.get())
        a=int(txtA.get())
        b=int(txtB.get())
        c=int(txtC.get())
        i=0
        while(i<m):
            ax2=(a*(math.pow(X0,2)))
            bx=b*X0
            op=(ax2+bx+c)%m
            Semillas.append(op)
            lstSemilla.insert(i, X0)
            lstPorcentaje.insert(i, op)
            X0=op
            i+=1
            lblIter1["text"]=str(i)
       
    
    calcular = Button(v, fg="yellow", text="Calcular", bg="purple3", width=12, height=1, command=congC)
    calcular.place(x=420, y=170)
    
    btnMedia = Button(v, fg="yellow", text="Media", bg="purple3", width=12, height=1, command=lambda:validarAlpha(txtAlpha,Semillas, btnMedia,"m"))
    btnMedia.place(x=420, y=210)
    
    btnVarianza = Button(v, fg="yellow", text="Varianza", bg="purple3", width=12, height=1, command=lambda:validarAlpha(txtAlpha, Semillas, btnVarianza,"v"))
    btnVarianza.place(x=420, y=250)
    
    btnJi = Button(v, fg="yellow", text="JiCuadrada", bg="purple3", width=12, height=1, command=lambda:validarAlpha(txtAlpha, Semillas, btnJi,"c"))
    btnJi.place(x=420, y=290)

def cuadradosMedios():
    global vCuadrados
    vCuadrados= Toplevel(ventana)
    vCuadrados.title("CUADRADOS MEDIOS")
    vCuadrados.geometry("610x400+400+100")
    vCuadrados.resizable(False, False)
    vCuadrados.configure(background="gray19")
    # variables
    listaPotencia=[ ]
    listaNewSemilla=[ ]
    listaPorcentaje=[ ]

    lblT = Label(vCuadrados, fg="yellow",font = ("centuri gothic", 11), text="Considere que el número de digitos de la semilla (X0) debe ser > a 3 y con una longitud par")
    lblT.place(x=5, y=10)
    lblT.config(background="maroon4", justify="center")

    lblCant = Label(vCuadrados, font="bold",text="Cantidad: ")
    lblCant.place(x=105, y=50)
    txtCant = Entry(vCuadrados)
    txtCant.place(x=195, y=50)
    txtCant.config(justify="center")

    lblAlpha = Label(vCuadrados, font="bold", text="α: ")
    lblAlpha.place(x=160, y=80)
    txtAlpha = Entry(vCuadrados)
    txtAlpha.place(x=195, y=80)
    txtAlpha.config(justify="center")

    lblItera = Label(vCuadrados,fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Item:")
    lblItera.place(x=30, y=130)
    lstItera = Listbox(vCuadrados, width=8)
    lstItera.place(x=30, y=150)
    lstItera.yview()

    lblPotencia = Label(vCuadrados, fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Potencia:")
    lblPotencia.place(x=120, y=130)
    lstPotencia = Listbox(vCuadrados, width=20)
    lstPotencia.place(x=120, y=150)
    lstPotencia.yview()

    lblSemilla = Label(vCuadrados, fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Semilla:")
    lblSemilla.place(x=275, y=130)
    lstSemilla = Listbox(vCuadrados, width=20)
    lstSemilla.place(x=275, y=150)
    lstSemilla.yview()

    lblPorcentaje = Label(vCuadrados,fg="yellow", font = ("centuri gothic", 10), background="maroon4",text="Porcentaje: %")
    lblPorcentaje.place(x=430, y=130)
    lstPorcentaje = Listbox(vCuadrados, width=20)
    lstPorcentaje.place(x=430, y=150)
    lstPorcentaje.yview()

    lblIera1 = Label(vCuadrados,fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Total de iteraciones:")
    lblIera1.place(x=30, y=330) 
    
    listaPotencia=[]
    listaNewSemilla=[]
    listaPorcentaje=[]
    def cumF():
       
        X0=int(txtCant.get())
        dig=len(str(X0))
        totaldig=2*dig   
        porc=float
        i=0
        while(porc!=0):
            if(i==100):
                break
            else:
                potcant=int(math.pow(X0,2))
                relleno=str(potcant).zfill(8)
                index=int(dig/2)
                X0=int(relleno[index:dig+index])
                porc=X0/10000
                listaPotencia.append(relleno)
                listaNewSemilla.append(str(X0).zfill(4))
                listaPorcentaje.append(porc)
                lstPotencia.insert(i, listaPotencia[i])
                lstSemilla.insert(i, listaNewSemilla[i])
                lstPorcentaje.insert(i,listaPorcentaje[i])
                lstItera.insert(i, i+1)
                i+=1
                lblItera2 = Label(vCuadrados, background="maroon4", font = ("centuri gothic", 10), text=str(i))
                lblItera2.place(x=160, y=330)
        
    
    calcular = Button(vCuadrados, fg="yellow", text="Calcular", bg="purple3", width=8, height=1, command=cumF)
    calcular.place(x=340, y=50)

    btnMedia = Button(vCuadrados, fg="yellow", text="Media", bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha, listaPorcentaje, btnMedia,"m"))
    btnMedia.place(x=410, y=50)

    btnVarianza = Button(vCuadrados, fg="yellow", text="Varianza", bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnVarianza,"v"))
    btnVarianza.place(x=480, y=50)

    btnJi = Button(vCuadrados, fg="yellow", text="JiCuadrada", bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnJi,"c"))
    btnJi.place(x=410, y=80)

def multiplicadorConstante():
    global vm_Constante
    vm_Constante= Toplevel(ventana)
    vm_Constante.title("MULTIPLICADOR CONSTANTE")
    vm_Constante.geometry("600x400+400+100")
    vm_Constante.resizable(False, False)
    vm_Constante.configure(background="gray19")
    
    lblX0= Label(vm_Constante, text="Semilla (X0): ")
    lblX0.place(x=82, y=30)
    txtX0 = Entry(vm_Constante)
    txtX0.place(x=170, y=30)
    txtX0.config(justify="center")

    lblA = Label(vm_Constante, text="Constante (a):")
    lblA.place(x=76, y=60)
    txtA = Entry(vm_Constante)
    txtA.place(x=170, y=60)
    txtA.config(justify="center")
    
    lblAlpha = Label(vm_Constante, text="α: ")
    lblAlpha.place(x=138, y=90)
    txtAlpha = Entry(vm_Constante)
    txtAlpha.place(x=170, y=90)
    txtAlpha.config(justify="center")
    
    lblProd = Label(vm_Constante, fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Productos:")
    lblProd.place(x=40, y=130)
    lstProd = Listbox(vm_Constante, width=20)
    lstProd.place(x=40, y=150)
    lstProd.yview()

    lblSem1 = Label(vm_Constante, fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Semilla 1:")
    lblSem1.place(x=175, y=130)
    lstSem1 = Listbox(vm_Constante, width=20)
    lstSem1.place(x=175, y=150)
    lstSem1.yview()

    lblSem2 = Label(vm_Constante, fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Semilla 2:")
    lblSem2.place(x=310, y=130)
    lstSem2 = Listbox(vm_Constante, width=20)
    lstSem2.place(x=310, y=150)
    lstSem2.yview()

    lblPorcentaje = Label(vm_Constante, fg="yellow", font = ("centuri gothic", 10), background="maroon4",text="Porcentajes: %")
    lblPorcentaje.place(x=445, y=130)
    lstPorcentaje = Listbox(vm_Constante, width=20)
    lstPorcentaje.place(x=445, y=150)
    lstPorcentaje.yview()

    lblIter = Label(vm_Constante, fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Total de iteraciones:")
    lblIter.place(x=30, y=330)
    listaPorcentaje = []
    
    def multcF():
        listaRes = []
        listaNewSemilla1 = []
        listaNewSemilla2 = []
        
        X0= txtX0.get()
        a= txtA.get()
        X0=int(X0)
        a=int(a)
        dig=len(str(X0))    
        porc = float
        i = 0
        while(porc != 0):
            if(i == 100):
                break
            else:
                res = a*X0
                listaRes.append(res)
                listaNewSemilla1.append(a)
                cadres = str(res)
                lonres = int(len(cadres))
                index = int((lonres-dig)/2)
                X0 = int(cadres[index:dig+index])
                porc = X0/10000
                listaNewSemilla2.append(X0)
                listaPorcentaje.append(porc)
                lstProd.insert(i,listaRes[i])
                lstSem1.insert(i,listaNewSemilla1[i])
                lstSem2.insert(i,listaNewSemilla2[i])
                lstPorcentaje.insert(i, listaPorcentaje[i])
                i += 1
                lblIter1 = Label(vm_Constante,fg="yellow",  background="maroon4", font = ("centuri gothic", 10), text=str(i))
                lblIter1.place(x=160, y=330)       
                
    calcular = Button(vm_Constante,fg="yellow", text="Calcular", font=("centuri gothic",10,"bold"),bg="purple3", width=8,height=1, command=multcF).place(x=310, y=50)
    btnVarianza= Button(vm_Constante,fg="yellow", text="Varianza", font=("centuri gothic",10,"bold"),bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnVarianza,"v")).place(x=390, y=50)
    btnMedia= Button(vm_Constante, fg="yellow",text="Media", font=("centuri gothic",10,"bold"),bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha, listaPorcentaje, btnMedia,"m")).place(x=470, y=50)
    btnJi= Button(vm_Constante, fg="yellow", text="JiCuadrada", font=("centuri gothic",10,"bold"), bg="purple3",  width=10, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnJi,"c")).place(x=385, y=85)

def productosMedios():
    global vp_Medios
    vp_Medios=Toplevel(ventana)
    vp_Medios.title("PRODUCTOS MEDIOS")
    vp_Medios.geometry("650x400")
    vp_Medios.resizable(False, True)
    vp_Medios.configure(background="gray19")
    
    lblT = Label(vp_Medios, fg="yellow",font = ("centuri gothic", 12), text="Considere que el número óptimo de dígitos debe ser > 3 y debe ser par.")
    lblT.place(x=75, y=3)
    lblT.config(background="maroon4", justify="center",)

    lblX1 = Label(vp_Medios, font="bold", text="Semilla 1: ")
    lblX1.place(x=180, y=35)
    txtX1 = Entry(vp_Medios)
    txtX1.place(x=270, y=35)
    txtX1.config(justify="center")

    lblX2 = Label(vp_Medios, font="bold", text="Semilla 2:")
    lblX2.place(x=184, y=65)
    txtX2 = Entry(vp_Medios)
    txtX2.place(x=270, y=65)
    txtX2.config(justify="center")

    lblAlpha = Label(vp_Medios, font="bold", text="α: ")
    lblAlpha.place(x=235, y=95)
    txtAlpha = Entry(vp_Medios)
    txtAlpha.place(x=270, y=95)
    txtAlpha.config(justify="center")
   
    lblProd = Label(vp_Medios,fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Productos:")
    lblProd.place(x=40, y=130)
    lstProd = Listbox(vp_Medios, width=20)
    lstProd.place(x=40, y=150)
    lstProd.yview()

    lblSem1 = Label(vp_Medios,fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Semilla 1:")
    lblSem1.place(x=175, y=130)
    lstSem1 = Listbox(vp_Medios, width=20)
    lstSem1.place(x=175, y=150)
    lstSem1.yview()

    lblSem2 = Label(vp_Medios,fg="yellow", background="maroon4", font = ("centuri gothic", 10), text="Semilla 2:")
    lblSem2.place(x=310, y=130)
    lstSem2 = Listbox(vp_Medios, width=20)
    lstSem2.place(x=310, y=150)
    lstSem2.yview()

    lblPorcentaje = Label(vp_Medios, fg="yellow",font = ("centuri gothic", 10), background="maroon4",text="Porcentaje: %")
    lblPorcentaje.place(x=445, y=130)
    lstPorcentaje = Listbox(vp_Medios, width=20)
    lstPorcentaje.place(x=445, y=150)
    lstPorcentaje.yview()

    lblIter = Label(vp_Medios, fg="yellow",background="maroon4", font = ("centuri gothic", 10), text="Total de iteraciones:")
    lblIter.place(x=30, y=330)
    listaPorcentaje = []
    def pmF():
        listaProducto = []
        listaNewSemilla1 = []
        listaNewSemilla2 = []
       
        X0= txtX1.get()
        X1= txtX2.get()
        X0=int(X0)
        X1=int(X1)
        dig=len(str(X0))   
        porc = float
        i = 0
        while(porc != 0):
            if(i == 100):
                break
            else:
                producto = X0*X1
                listaProducto.append(producto)
                listaNewSemilla1.append(X0)
                listaNewSemilla2.append(X1)
                cadproducto = str(producto)
                lonproducto = int(len(cadproducto))
                index = int((lonproducto-dig)/2)
                X0 = X1
                X1 = int(cadproducto[index:dig+index])
                porc = X1/10000
                listaPorcentaje.append(porc)
                lstProd.insert(i,listaProducto[i])
                lstSem1.insert(i,listaNewSemilla1[i])
                lstSem2.insert(i,listaNewSemilla2[i])
                lstPorcentaje.insert(i, listaPorcentaje[i])
                i += 1
                lblIter1 = Label(vp_Medios,fg="yellow", background="maroon4", font = ("centuri gothic", 10), text=str(i))
                lblIter1.place(x=160, y=330)    
                
    calcular = Button(vp_Medios,fg="yellow", text="Calcular", font=("centuri gothic",10,"bold"), bg="purple3", width=8,height=1, command=pmF).place(x=410, y=50)
    btnVarianza= Button(vp_Medios,fg="yellow", text="Varianza", font=("centuri gothic",10,"bold"), bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha, listaPorcentaje, btnVarianza,"v")).place(x=490, y=50)
    btnMedia= Button(vp_Medios, fg="yellow",text="Media", font=("centuri gothic",10,"bold"), bg="purple3", width=8, height=1, command=lambda:validarAlpha(txtAlpha, listaPorcentaje, btnMedia,"m")).place(x=570, y=50)
    btnJi= Button(vp_Medios, fg="yellow", text="JiCuadrada", font=("centuri gothic",10,"bold"), bg="purple3",  width=10, height=1, command=lambda:validarAlpha(txtAlpha,listaPorcentaje, btnJi,"c")).place(x=485, y=85)

def instruc():

    global vinstruc

    vinstruc = Toplevel(ventana)
    vinstruc.title("INSTRUCCIONES")
    vinstruc.geometry("620x430+400+120")
    vinstruc.configure(background="gray19")
    Label(vinstruc, text="Para desplazarte por el menú deberás dar click en alguna de las \n diferentes pestañas que se muestran en la parte superior de la \n ventana. Estas pestañas contienen a su vez diferentes opciones \n tales como métodos vistos en la materia de SIMULACIÓN,\n instrucciones, informes de contacto, etc.",
          fg="white", bg="gray19", font=("centuri gothic", 14)).place(x=20, y=20)
    Label(vinstruc, text="Dentro de cada método encontrarás cajas de texto que te pemitirán \n ingresar diferentes valores por lo que te pedimos atiendas a \n las instrucciones que la mayoría de métodos traen consigo para \n que los resultados sean los correctos. Finalmente,\n notarás que los resultados se muestran de una forma bastante visual \n por lo que esperamos tengas una buena experiencia.",
          fg="white", bg="gray19", font=("centuri gothic", 14)).place(x=20, y=150)
    Label(vinstruc, text="\n NOTA: \n Para corroborar que los datos arrojados seans los correctos \n utilizamos los datos proporcionados en el documento PDF, así \n que recomendamos usar los mismos.",
          fg="white", bg="gray19", font=("centuri gothic", 14)).place(x=20, y=280)


def presen():
    global vpresen
    global fan
    global liz
    global nes
    global yam

    vpresen = Toplevel(ventana)
    vpresen.title("PRESENTACIÓN")
    vpresen.geometry("450x380+530+120")
    vpresen.resizable(False, False)
    vpresen.configure(background="gray19")

    fan = PhotoImage(file="Fany.png")
    btnFan = Label(vpresen, image=fan, height=100, width=100).place(x=80, y=10)
    lblFan1 = Label(vpresen, fg="magenta4", bg="light sea green",font=("centuri gothic", 10, "bold"),
                    text="Estrada Aguilar Jose Estefania \n  18TE0258").place(x=30, y=130)
    liz = PhotoImage(file="Lizzie.png")
    btnLiz = Label(vpresen, image=liz, height=100,
                   width=100).place(x=280, y=10)
    lblLiz = Label(vpresen, fg="magenta4", bg="light sea green",font=("centuri gothic", 10, "bold"),
                   text="Lucas Garcia Elizabeth \n  18TE0171").place(x=260, y=130)
    nes = PhotoImage(file="Ines.png")
    btnNes = Label(vpresen, image=nes, height=100,
                   width=100).place(x=80, y=200)
    lblNes = Label(vpresen,fg="magenta4", bg="light sea green",font=("centuri gothic", 10, "bold"),
                   text="Gonzalez Glz. Inés del Carmen\n  18TE0195").place(x=30, y=320)
    yam = PhotoImage(file="Yami.png")
    btnYam = Label(vpresen, image=yam, height=100,
                   width=100).place(x=280, y=200)
    lblYam = Label(vpresen,fg="magenta4", bg="light sea green",font=("centuri gothic", 10, "bold"),
                   text="Garcia Perez Yamileth \n  18TE0416").place(x=260, y=320)

    #salir = Button(vpresen, bg="purple3", text="Salir",  height=1,
     #              width=30, command=vpresen.quit).place(x=120, y=385)

def contacto():

    global vcontacto
    global fondoCon

    vcontacto = Toplevel(ventana)
    vcontacto.title("CONTÁCTOS")
    vcontacto.geometry("590x340+400+120")
    vcontacto.resizable(False, False)
    vcontacto.configure(background="gray19")
    fondoCon= PhotoImage(file="sociales.png")
    lblCon = Label(vcontacto, image=fondoCon).place(x=0,y=0)
    lblFan = Label(vcontacto, bg="indian red", font=(
        "centuri gothic", 18, "bold"), text="FANY").place(x=50, y=40)
    lblFan2 = Label(vcontacto, bg="gray19",fg="light gray", font=("centuri gothic", 12),
                    text=" Facebook: Fany Estrada \n  WhatsApp: 231-144-8380 \n Instagram: fany.estralar").place(x=50, y=70)

    lblLiz = Label(vcontacto, bg="indian red", font=(
        "centuri gothic", 18, "bold"), text="LIZZY").place(x=340, y=40)
    lblLiz2 = Label(vcontacto,  bg="gray19",fg="light gray", font=("centuri gothic", 12),
                    text=" Facebook: Lizzie Lucas \n  WhatsApp: 231-153-0044 \n  Instagram: lizzie_lucas1503").place(x=340, y=70)

    lblNes = Label(vcontacto, bg="indian red", font=(
        "centuri gothic", 18, "bold"), text="INÉS").place(x=50, y=170)
    lblNes2 = Label(vcontacto, bg="gray19",fg="light gray",  font=("centuri gothic", 12),
                    text=" Facebook: Nes Gonzalez \n  WhatsApp: 231-151-1171 \n ").place(x=50, y=200)

    lblYam = Label(vcontacto, bg="indian red", font=(
        "centuri gothic", 18, "bold"), text="YAMI").place(x=340, y=170)
    lblYam2 = Label(vcontacto, bg="gray19",fg="light gray",  font=("centuri gothic", 12),
                    text=" Facebook: Yam Peréz \n  WhatsApp: 231-187-8510 \n Instagram: yamperez18").place(x=340, y=200)

    #salir = Button(vcontacto, bg="purple3", text="OK",  height=1,
                  # width=30, command=vcontacto.quit).place(x=200, y=290)

def main_ventana():
    # VENTANA
    global ventana
    ventana = Tk()
    ventana.title("MENÚ PRINCIPAL")  # nombre de ventana
    ventana.geometry("500x300+500+100")  # tamaño de ventana
    ventana.resizable(False, False)  # Mantener medidas estáticas
    ventana.configure(background="light sea green")  # color de fondo
    fondo = PhotoImage(file="pseudoaleatorios.png")
    lblFondo = Label(ventana, image=fondo).place(x=0, y=0)

# BARRA DE MENÚS
    menubar = Menu(ventana)
# MENÚS
    metodo = Menu(menubar, tearoff=0)  # tearoff crea menús flotantes
    ayuda = Menu(menubar, tearoff=0)
    des = Menu(menubar, tearoff=0)
# COMANDOS DE MENÚS
# Agregar los menús a la barra, en forma de cascada
    menubar.add_cascade(label="MÉTODOS", menu=metodo)
    metodo.add_command(label="Algoritmo lineal", command=algoritmoLineal)
    metodo.add_command(label="Congruencial aditivo", command=c_Aditivo)
    metodo.add_command(label="Congruecial multiplicativo", command=congMultiplicativo_vm)
    metodo.add_command(label="Congruecial cuadrático", command=congCuadratico_vm)
    metodo.add_command(label="Cuadrados medios", command=cuadradosMedios)
    metodo.add_command(label="Multiplicador constante", command=multiplicadorConstante)
    metodo.add_command(label="Productos medios", command=productosMedios)
    metodo.add_separator()  # Hace una linea sobre el texto para separar
    # Cierra la ventana
    metodo.add_command(label="Cerrar", command=ventana.quit)

    menubar.add_cascade(label="AYUDA", menu=ayuda)
    ayuda.add_command(label="Instrucciones", command=instruc)

    menubar.add_cascade(label="DESARROLLADORAS", menu=des)
    des.add_command(label="Presentación", command=presen)
    des.add_separator()
    des.add_command(label="Contáctos", command=contacto)
# Indica que la barra de menús estará en la ventana
    ventana.config(menu=menubar)
    unidad= Label(ventana, fg="magenta4", bg="light sea green", font=("centuri gothic", 22, "bold"), text="U.2").place(x=5,y=30)
    nom= Label(ventana, fg="magenta4", bg="light sea green", font=("centuri gothic", 28, "bold"), text="Números Pseudoaleatorios").place(x=5,y=100)
    fecha= Label(ventana, fg="magenta4", bg="light sea green", font=("centuri gothic", 20), text="Octubre, 2020").place(x=300,y=250)
    

    ventana.mainloop()

main_ventana()
from tkinter import Tk, Entry, Button, StringVar, Label

digito= ''

#toma los digitos y los toma en el calculo "digito"
def tomar_digito(n):
    global digito
    digito= digito+ str(n)
    calculo.set(digito)

#eval evalua expreciones basicas de matematicas y las resuelve,para calculadoras mas avanzadas deberiamos usar libreria math
def resultado():
    try:
        global digito
        total = str(eval(digito))
        calculo.set(total)
        digito=''
    except:
        calculo.set("ERROR")

def limpiar_completo():
    global digito
    calculo.set("")
    digito=''

ventana = Tk()
ventana.configure(background='#16A085')
ventana.title ('Calculadora Basica')
ventana.geometry('280x280')
ventana.resizable(0,0)
#llamamos a la funcion 
calculo= StringVar()

#es el imput
datos = Entry(ventana, textvariable=calculo)
datos.grid (row=0, column=0,columnspan=7, ipadx=60, ipady=14,)

texto = "CALCULADORA"

# Insertar saltos de línea entre cada letra
texto_vertical = "\n".join(texto)

label = Label(ventana, text=texto_vertical, font=("Arial", 12),bg='#16A085',fg='#F2F4F4')
label.grid(row=1, column=5,rowspan=6)


#primera fila
btn1=Button(ventana, text='1',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(1))
btn1.grid(row=1,column=0)

btn2=Button(ventana, text='2',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(2))
btn2.grid(row=1,column=1)

btn3=Button(ventana, text='3',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(3))
btn3.grid(row=1,column=3)

btn4=Button(ventana, text='+',bg='#34495E',fg='#F2F4F4',width=5,height=2,command=lambda: tomar_digito('+'))
btn4.grid(row=1,column=4)

#segunda fila
btn5=Button(ventana, text='4',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(4))
btn5.grid(row=2,column=0)

btn6=Button(ventana, text='5',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(5))
btn6.grid(row=2,column=1)

btn7=Button(ventana, text='6',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(6))
btn7.grid(row=2,column=3)

btn8=Button(ventana, text='-',bg='#34495E',fg='#F2F4F4',width=5,height=2,command=lambda: tomar_digito('-'))
btn8.grid(row=2,column=4)
#tercera fila
btn9=Button(ventana, text='7',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(7))
btn9.grid(row=3,column=0)

btn10=Button(ventana, text='8',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(8))
btn10.grid(row=3,column=1)

btn11=Button(ventana, text='9',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(9))
btn11.grid(row=3,column=3)

btn12=Button(ventana, text='*',bg='#34495E',fg='#F2F4F4',width=5,height=2,command=lambda: tomar_digito('*'))
btn12.grid(row=3,column=4)
#cuarta fila
btn13=Button(ventana, text='0',bg='#F5B041',fg='#1D8348',width=5,height=2,command=lambda: tomar_digito(0))
btn13.grid(row=4,column=0)

btn14=Button(ventana, text='.',bg='#34495E',fg='#F2F4F4',width=5,height=2,command=lambda: tomar_digito('.'))
btn14.grid(row=4,column=1)

btn15=Button(ventana, text='Limpiar',bg='blue',fg='red',width=5,height=2,command=limpiar_completo)
btn15.grid(row=4,column=3)

btn16=Button(ventana, text='/',bg='#2E4053',fg='#F2F4F4',width=5,height=2,command=lambda: tomar_digito('/'))
btn16.grid(row=4,column=4)
#quita fila
btn17=Button(ventana, text='(',bg='#2E4053',fg='#F2F4F4',width=5,height=2,command=lambda: tomar_digito('('))
btn17.grid(row=5,column=0)

btn18=Button(ventana, text='=',bg='#2E4053',fg='#F2F4F4',width=5,height=2,command= resultado)
btn18.grid(row=5,column=1,columnspan=3,ipadx=32,ipady=0)

btn19=Button(ventana, text=')',bg='#2E4053',fg='#F2F4F4',width=5,height=2,command=lambda: tomar_digito(')'))
btn19.grid(row=5,column=4,columnspan=1,ipadx=0,ipady=0)

ventana.mainloop ()

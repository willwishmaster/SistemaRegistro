from tkinter import *

def main():
    dialogo = Tk();
    dialogo.geometry("300x250")
    
    dialogo.title("Sistema de Registro")
    Label(text="Sistema de Registro",bg="grey", width="300", height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Iniciar sesion", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Registrar", height="2", width="30").pack()
    
    dialogo.mainloop()
    
main()

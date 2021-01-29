from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

window=Tk()
window.geometry("300x300")
window.title('WhatList')



class App:
    def __init__(self,window):
        self.window = window

        barra_Menu = Menu(self.window)

        barra_Menu.add_command(label="Página Inicial", command = self.home)
        barra_Menu.add_command(label="Notificações", command = self.notif)
        barra_Menu.add_command(label="Conta", command = self.conta)

        barra_Menu.add_command(label="Sair", command = window.quit)
        window.configure(menu=barra_Menu)

        lb1 = Label(window, text = "Login", font = ("Arial", 20))
        lb1.pack(side=TOP)

        idNome = Label(window, text="Nome", font =("Arial", 10))
        idNome.pack(side=TOP)
        txt_idNome = Entry(window, width=20)
        txt_idNome.pack(side=TOP)

        email = Label(window, text="Email", font =("Arial", 10))
        email.pack(side=TOP)
        txt_email = Entry(window, width=20)
        txt_email.pack(side=TOP)

        password = Label(window, text="Password", font =("Arial", 10))
        password.pack(side=TOP)
        txt_pass = Entry(window, width=20, show="*")
        txt_pass.pack(side=TOP)


        btn_auten = Button(window, text="Autenticar", command=self.home)
        btn_auten.pack(side=TOP)


    #cria uma janela para a Página inicial
    def home(self):

        def inserir():
            if vtask.get()=="" or vcontent.get()=="" or vrank.get()=="":
                messagebox.showinfo(title="ERRO", message="Todos os dados")
                return
            tv.insert("","end", values=(vtask.get(),vcontent.get(),vrank.get()))
            vtask.delete(0,END)
            vcontent.delete(0,END)
            vrank.delete(0,END)
            vtask.focus()
        
        def delete():
            try:
                itemSelecionado=tv.selection()[0]
                tv.delete(itemSelecionado)
            except:
                messagebox.showinfo(title="ERROR",message="Selecione um elemento a ser deletado")

        

        task= Tk()
        task.title("Caixa de Entrada")
        task.geometry("500x350")

        lbtask=Label(task,text="Tarefa")
        vtask=Entry(task)

        lbcontent=Label(task,text="Coisas a fazer")
        vcontent=Entry(task)

        lista=["Não realizado", "Importante", "Em progresso"]
        lbrank=Label(task, text="Rank")
        vrank=Combobox(task,values=lista)

        tv=ttk.Treeview(task,columns=('tarefa','coisas a fazer','rank'),show='headings')
        tv.column('tarefa',minwidth=0,width=50)
        tv.column('coisas a fazer',minwidth=0,width=250)
        tv.column('rank',minwidth=0,width=100)
        tv.heading('tarefa',text='Tarefa')
        tv.heading('coisas a fazer',text='Coisas a fazer')
        tv.heading('rank',text="Rank")

        btn_inserir=Button(task,text="Inserir",command=inserir)
        btn_deletar=Button(task,text="Deletar",command=delete)

        lbtask.grid(column=0,row=0,stick='w')
        vtask.grid(column=0,row=1)

        lbcontent.grid(column=1,row=0,stick='w')
        vcontent.grid(column=1,row=1)

        lbrank.grid(column=2,row=0,stick='w')
        vrank.grid(column=2,row=1,stick='w')

        tv.grid(column=0,row=3,columnspan=3,pady=5)

        btn_inserir.grid(column=0,row=4)
        btn_deletar.grid(column=1,row=4)

        lista=["Não realizado", "Importante", "Em progresso"]
        btn_rank = Combobox(task, values=lista)
        btn_rank.grid(column=2,row=4)

    #Cria uma janela para as notificações
    def notif(self):
        notifwindow =Toplevel()
        notifwindow.geometry("400x500")
        notifwindow.title("Notificações")
        notifwindow.focus_force()
        notifwindow.grab_set()

        lb3 = Label(notifwindow, text="Notificações", font = ("Arial", 20))
        lb3.pack(side=TOP)
    
    #Cria uma janela para a conta do utilizador
    def conta(self):
        contawin =Tk()
        contawin.geometry("500x300")
        contawin.title("WhatList-Conta do Usuário")
        
        c=Canvas(contawin,bg="blue", height=150, width=200)
        c.grid(column=0,row=0)

        lbname_user=Label(contawin, text="Max Stirner")
        lbname_user.grid(column=1, row=0)

        lbemail_user=Label(contawin, text="maxstirner_milk@email.com")
        lbemail_user.grid(column=1, row=1)
    

App(window)

window.mainloop()
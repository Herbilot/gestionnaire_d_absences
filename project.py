from tkinter import *
from tkinter import ttk, messagebox
import psycopg2
from subprocess import call
from datetime import datetime
#database connection
conn = psycopg2.connect( host="localhost", database="gestion_absence",user="herbilot",password="123db")


#Connect fonction
def connexion():
    utilisatuer = matriculeEntry.get()
    motDePasse = entryMdp.get()
    curr = conn.cursor()
    sql = "SELECT role FROM utilisateur where matricule=%s and mot_de_passe=%s"
    curr.execute(sql, (utilisatuer, motDePasse))
    res = curr.fetchone()
    #controle de sasie
    if(utilisatuer == "" and motDePasse == ""):
        messagebox.showerror("", "Veillez remplir tous les champs")
        matriculeEntry.delete("0", "end")
        entryMdp.delete("0", "end")
    elif(res):
        role = res[0]
        if role =="professeur":
            messagebox.showinfo("", "Bienvenue")
            matriculeEntry.delete("0", "end")
            entryMdp.delete("0", "end")
            root.destroy()
            professeur()

        elif role =="etudiant":
            messagebox.showinfo("", "Bienvenue")
            matricule = utilisatuer
            matriculeEntry.delete("0", "end")
            entryMdp.delete("0", "end")
            root.destroy()
            etudiant()
            print(matricule)
    else:
        messagebox.showerror("", "nom d'utilisateur ou mot de passe incorrect")
        matriculeEntry.delete("0", "end")
        entryMdp.delete("0", "end")
    






#creation fenetre 
root = Tk()
root.title("Gestionnaire d'absences")
root.geometry("720x380+350+150")
root.config(background="#ECE8DD")


lbltitre = Label(root, borderwidth=3, text="Page de connexion", relief=SUNKEN, font=("Montserrat", 25), bg="#579BB1", fg="White")
lbltitre.pack(fill=X)

lblmatricule = Label(root, text="Matricule", font=("Ubuntu", 16), bg="#ECE8DD", fg="#222222")
lblmatricule.place(x=200, y=100)
matriculeEntry = Entry(root, bd=4, font=("Ubuntu", 14))
matriculeEntry.place(x=200, y=130, width=350)

lblMdp = Label(root, text="Mot de passe", font=("Ubuntu", 16), bg="#ECE8DD", fg="#222222")
lblMdp.place(x=200, y=180)
entryMdp = Entry(root, show="*", bd=4, font=("Ubuntu", 14))
entryMdp.place(x=200, y=210, width=350)

btnConnexion = Button(root, text="Se connecter", font=("Montserrat", 18), bg="#579BB1", fg="#FFF", command=connexion)
btnConnexion.place(x=275, y=290, width=200)






def professeur():
    #create cursor
    def currentMat():
        mat_entry.config(state=NORMAL)
        mat_entry.delete(0, END)
        mat_entry.insert(0, "Etu" + datetime.now().strftime("%d%m%Y%H%M%S"))
        mat_entry.configure(state=DISABLED)

    def lire():
        conn = psycopg2.connect( host="localhost", database="gestion_absence",user="herbilot",password="123db")
        #create cursor
        curr = conn.cursor()
        global count 
        count = 0
        curr.execute("SELECT matricule, nom, prenom, nombre_absence from utilisateur where role='etudiant'")
        res = curr.fetchall()
        curr.close()
        conn.close()

        for row in res:
            if count % 2 == 0:
                table.insert(parent='', index='end', iid=count, values=row, tags=('evenrow',))
            else:
                table.insert(parent='', index='end', iid=count, values=row, tags=('oddrow',))
            count +=1


    root = Tk()
    root.title("Gestionnaire d'absence")
    root.geometry("1000x500")

    #Add some style
    style = ttk.Style()

    #Pick A theme
    style.theme_use('default')

    #Configure the Treeview Colors
    style.configure("Treeview",
        background="#D3D3D3",
        forground="black",
        rowheight=25,
        fieldbackground="#D3D3D3")

    #Change Selected Colors
    style.map(['selected', '#347083'])

    #Create a Treeview Frame 
    treeview_frame = Frame(root)
    treeview_frame.pack(padx=10)

    #Create A Treeview Scrollbar
    treeview_scroll = Scrollbar(treeview_frame)
    treeview_scroll.pack(side=RIGHT, fill=Y)

    #Create The Treeview
    table = ttk.Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended")
    table.pack()

    #configure the scrollbar
    treeview_scroll.config(command=table.yview)
    #define columns
    table['columns'] = ("Matricule", "Nom", "Prenom", "Absence")

    #format columns
    table.column("#0", width=0, stretch=NO)
    table.column("Matricule", anchor=W, width=245)
    table.column("Nom", anchor=W, width=245)
    table.column("Prenom", anchor=W, width=245)
    table.column("Absence", anchor=W, width=245)
    #create headings
    table.heading("#0", text="")
    table.heading("Matricule", text="Matricule", anchor=W)
    table.heading("Nom", text="Nom", anchor=W)
    table.heading("Prenom", text="Prénom", anchor=W)
    table.heading("Absence", text="Nombre d'absence", anchor=W)

    #Create stripped row
    table.tag_configure('oddrow', background="#FFF")
    table.tag_configure('evenrow', background="lightblue")

    #Add data
    lire()

    #Add fields
    data_frame = LabelFrame(root, text="Enregistrement")
    data_frame.pack(fill="x", expand=YES, padx=20)

    mat_label = Label(data_frame, text="Matricule", font=("Montserrat",12))
    mat_label.grid(row=0, column=0, padx=10, pady=10)
    mat_entry = Entry(data_frame)
    mat_entry.insert(0, "Etu" + datetime.now().strftime("%d%m%Y%H%M%S"))
    mat_entry.config(state=DISABLED)
    mat_entry.grid(row=0, column=1 , padx=10, pady=10)

    role_label = Label(data_frame, text="Role", font=("Montserrat",12))
    role_label.grid(row=0, column=2, padx=10, pady=10)
    role_entry = Entry(data_frame)
    role_entry.insert(0,"etudiant")
    role_entry.config(state=DISABLED)
    role_entry.grid(row=0, column=3 , padx=10, pady=10)

    nom_label = Label(data_frame, text="Nom", font=("Montserrat",12))
    nom_label.grid(row=1, column=0, padx=10, pady=10)
    nom_entry = Entry(data_frame)
    nom_entry.grid(row=1, column=1 , padx=10, pady=10)

    pren_label = Label(data_frame, text="Prénom", font=("Montserrat",12))
    pren_label.grid(row=1, column=2, padx=10, pady=10)
    pren_entry = Entry(data_frame)
    pren_entry.grid(row=1, column=3 , padx=10, pady=10)

    mdp_label = Label(data_frame, text="Mot de passe", font=("Montserrat",12))
    mdp_label.grid(row=1, column=4, padx=10, pady=10)
    mdp_entry = Entry(data_frame)
    mdp_entry.insert(0, "P@sser")
    mdp_entry.config(state=DISABLED)
    mdp_entry.grid(row=1, column=5 , padx=10, pady=10)


    #Methods for buttons
    #add record
    def ajouter():
        conn = psycopg2.connect( host="localhost", database="gestion_absence",user="herbilot",password="123db")
        matricule = mat_entry.get()
        role = role_entry.get()
        nom = nom_entry.get()
        prenom = pren_entry.get()
        mdp = mdp_entry.get()
        curr = conn.cursor()
        try:
            sql = "insert into utilisateur (matricule, nom, role, prenom, mot_de_passe) values (%s,%s,%s,%s,%s)"
            curr.execute(sql, (matricule, nom, role, prenom, mdp))
            conn.commit()
            messagebox.showinfo("Ajout", "Etudiant(e) ajouté(e) avec succèes !")
            curr.close()
            conn.close()
            mat_entry.delete(0, END)
            nom_entry.delete(0, END)
            pren_entry.delete(0, END)
            currentMat()
            table.delete(*table.get_children())
            lire()
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()

    #update record
    def modifier():
        conn = psycopg2.connect( host="localhost", database="gestion_absence",user="herbilot",password="123db")
        #get data
        matricule = mat_entry.get()
        role = role_entry.get()
        nom = nom_entry.get()
        prenom = pren_entry.get()
        mdp = mdp_entry.get()
        curr = conn.cursor()
        #update data
        try:
            sql = "update utilisateur set matricule=%s, role=%s, nom=%s, prenom=%s, mot_de_passe=%s where matricule=%s"
            curr.execute(sql,(matricule, role, nom, prenom, mdp, matricule,))
            conn.commit()
            messagebox.showinfo("Modification", "Etudiant(e) modifié(e) avec succès !")
            mat_entry.delete(0, END)
            nom_entry.delete(0, END)
            pren_entry.delete(0, END)
            currentMat()
            table.delete(*table.get_children())
            lire()
            curr.close()
            conn.close()

        except Exception as e:
            print(e)
            conn.rollback()
            conn.close

    #delete record
    def supprimer():
        conn = psycopg2.connect( host="localhost", database="gestion_absence",user="herbilot",password="123db")
        matricule = mat_entry.get()
        curr = conn.cursor()
        sql = "delete from utilisateur where matricule=%s"
        curr.execute(sql, (matricule,))
        conn.commit()
        messagebox.showinfo("Suppression", "Etudiant(e) supprimé avec succès !")
        mat_entry.delete(0, END)
        nom_entry.delete(0, END)
        pren_entry.delete(0, END)
        currentMat()
        table.delete(*table.get_children())
        lire()
        curr.close()
        conn.close()



    def historique():
        matricule = mat_entry.get()
        def lire():
         conn = psycopg2.connect( host="localhost", database="gestion_absence",user="herbilot",password="123db")
         #create cursor
         curr = conn.cursor()
         global count 
         count = 0
         sql = "SELECT id, date_debut, date_fin, raison from historique_absence where etudiant_id=%s"
         curr.execute(sql, (matricule,))
         res = curr.fetchall()
         curr.close()
         conn.close()

         for row in res:
             if count % 2 == 0:
                 table.insert(parent='', index='end', iid=count, values=row, tags=('evenrow',))
             else:
                 table.insert(parent='', index='end', iid=count, values=row, tags=('oddrow',))
             count +=1

        historique = Toplevel(root)
        historique.title("Historique d'absences")
        historique.geometry("1000x500")

        #Add some style
        style = ttk.Style()

        #Pick A theme
        style.theme_use('default')

        #Configure the Treeview Colors
        style.configure("Treeview",
            background="#D3D3D3",
            forground="black",
            rowheight=25,
            fieldbackground="#D3D3D3")

        #Change Selected Colors
        style.map(['selected', '#347083'])

        #Create a Treeview Frame 
        treeview_frame = Frame(historique)
        treeview_frame.pack(padx=10)

        #Create A Treeview Scrollbar
        treeview_scroll = Scrollbar(treeview_frame)
        treeview_scroll.pack(side=RIGHT, fill=Y)

        #Create The Treeview
        table = ttk.Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended")
        table.pack()

        #configure the scrollbar
        treeview_scroll.config(command=table.yview)
        #define columns
        table['columns'] = ("ID", "Debut", "Fin", "Raison")

        #format columns
        table.column("#0", width=0, stretch=NO)
        table.column("ID", anchor=W, width=245)
        table.column("Debut", anchor=W, width=245)
        table.column("Fin", anchor=W, width=245)
        table.column("Raison", anchor=W, width=245)
        #create headings
        table.heading("#0", text="")
        table.heading("ID", text="ID Absence", anchor=W)
        table.heading("Debut", text="Date De Début", anchor=W)
        table.heading("Fin", text="Date De Fin", anchor=W)
        table.heading("Raison", text="Raison", anchor=W)

        #Create stripped row
        table.tag_configure('oddrow', background="#FFF")
        table.tag_configure('evenrow', background="lightblue")

        lire()





















    #select record from the treeview
    def selectionner():
        mat_entry.config(state=NORMAL)
        #Clear the entry boxes
        mat_entry.delete(0, END)
        nom_entry.delete(0, END)
        pren_entry.delete(0, END)

        #Grab record number
        selected = table.focus()
        #Grab record values
        values = table.item(selected, 'values')
        mat_entry.insert(0, values[0])
        mat_entry.config(state=DISABLED)
        nom_entry.insert(0, values[1])
        pren_entry.insert(0, values[2])

    #Add  buttons
    button_frame = LabelFrame(root, text="Actions")
    button_frame.pack(fill="x", expand=YES, padx=20)

    btn_ajouter = Button(button_frame, text="Ajouter", command=ajouter)
    btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

    btn_modifier = Button(button_frame, text="Modifier",command=modifier)
    btn_modifier.grid(row=0, column=1, padx=10, pady=10)

    btn_supprimer = Button(button_frame, text="Supprimer", command=supprimer)
    btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

    btn_absence = Button(button_frame, text="Ajouter une absence")
    btn_absence.grid(row=0, column=3, padx=10, pady=10)

    btn_historique = Button(button_frame, text="Voir l'historique des absences", command=historique)
    btn_historique.grid(row=0, column=4, padx=10, pady=10)

    btn_select = Button(button_frame, text="Selectionner", command=selectionner)
    btn_select.grid(row=0, column=5, padx=10, pady=10)



def etudiant():
    

    def lire():
         conn = psycopg2.connect( host="localhost", database="gestion_absence",user="herbilot",password="123db")
         #create cursor
         curr = conn.cursor()
         global count 
         count = 0
         sql = "SELECT id, date_debut, date_fin, raison from historique_absence where etudiant_id=%s"
         curr.execute(sql, matricule)
         res = curr.fetchall()
         curr.close()
         conn.close()

         for row in res:
             if count % 2 == 0:
                 table.insert(parent='', index='end', iid=count, values=row, tags=('evenrow',))
             else:
                 table.insert(parent='', index='end', iid=count, values=row, tags=('oddrow',))
             count +=1


    root = Tk()
    root.title("Historique d'absences")
    root.geometry("1000x500")

    #Add some style
    style = ttk.Style()

    #Pick A theme
    style.theme_use('default')

    #Configure the Treeview Colors
    style.configure("Treeview",
        background="#D3D3D3",
        forground="black",
        rowheight=25,
        fieldbackground="#D3D3D3")

    #Change Selected Colors
    style.map(['selected', '#347083'])

    #Create a Treeview Frame 
    treeview_frame = Frame(root)
    treeview_frame.pack(padx=10)

    #Create A Treeview Scrollbar
    treeview_scroll = Scrollbar(treeview_frame)
    treeview_scroll.pack(side=RIGHT, fill=Y)

    #Create The Treeview
    table = ttk.Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended")
    table.pack()

    #configure the scrollbar
    treeview_scroll.config(command=table.yview)
    #define columns
    table['columns'] = ("ID", "Debut", "Fin", "Raison")

    #format columns
    table.column("#0", width=0, stretch=NO)
    table.column("ID", anchor=W, width=245)
    table.column("Debut", anchor=W, width=245)
    table.column("Fin", anchor=W, width=245)
    table.column("Raison", anchor=W, width=245)
    #create headings
    table.heading("#0", text="")
    table.heading("ID", text="ID Absence", anchor=W)
    table.heading("Debut", text="Date De Début", anchor=W)
    table.heading("Fin", text="Date De Fin", anchor=W)
    table.heading("Raison", text="Raison", anchor=W)

    #Create stripped row
    table.tag_configure('oddrow', background="#FFF")
    table.tag_configure('evenrow', background="lightblue")

    #Add data
    lire()





mainloop()



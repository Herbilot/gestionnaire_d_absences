from app import * 

#generation matricule
matricule = "Etu" + datetime.now().strftime("%d%m%Y%H%M%S")


#methode enregistrer 
def enregistrer():
    matricule = matriculeEntry.get()
    nom = nomEntry.get()
    prenom = prenomEntry.get()
    role = roleEntry.get()
    mdp = mdpEntry.get()

    curr = conn.cursor()
    
    try:
        sql = "insert into utilisateur (matricule, nom, role, prenom, mot_de_passe) values(%s, %s, %s, %s, %s)"
        curr.execute(sql, (matricule, nom, role, prenom, mdp))
        conn.commit()
        curr.close()
        conn.close()
        messagebox.showinfo("", "Etudiant(e) ajouté(e) avec succes !")
        matriculeEntry.delete("0", "end")
        nomEntry.delete("0", "end")
        prenomEntry.delete("0", "end")
        roleEntry.delete("0", "end")
        mdpEntry.delete("0", "end")
    except Exception as e:
        print(e)

root = Tk()
root.title("Ajouter un(e) étudiant(e)")
root.geometry("500x550+450+100")
root.resizable(False, False)
root.config(background="#ECE8DD")

lbltitre = Label(root, borderwidth=3, text="Page d'enregistrement", relief=SUNKEN, font=("Montserrat", 25), bg="#579BB1", fg="White")
lbltitre.pack(fill=X)


lblMatricule = Label(root, text="Matricule", font=("Ubuntu", 16), bg="#ECE8DD", fg="#222222")
lblMatricule.place(x=100, y=100)
matriculeEntry = Entry(root, bd=4, font=("Ubuntu", 14))
matriculeEntry.insert(0, matricule)
matriculeEntry.config(state=DISABLED)
matriculeEntry.place(x=100, y=130, width=250)

lblnom = Label(root, text="Nom", font=("Ubuntu", 16), bg="#ECE8DD", fg="#222222")
lblnom.place(x=100, y=170)
nomEntry = Entry(root, bd=4, font=("Ubuntu", 14))
nomEntry.place(x=100, y=200, width=250)

lblprenom = Label(root, text="Prénom", font=("Ubuntu", 16), bg="#ECE8DD", fg="#222222")
lblprenom.place(x=100, y=240)
prenomEntry = Entry(root, bd=4, font=("Ubuntu", 14))
prenomEntry.place(x=100, y=270, width=250)

lblmdp = Label(root, text="Mot de passe", font=("Ubuntu", 16), bg="#ECE8DD", fg="#222222")
lblmdp.place(x=100, y=310)
mdpEntry = Entry(root, bd=4, font=("Ubuntu", 14))
mdpEntry.insert(0,"p@sser")
mdpEntry.config(state=DISABLED)
mdpEntry.place(x=100, y=340, width=250)

lblrole = Label(root, text="Role", font=("Ubuntu", 16), bg="#ECE8DD", fg="#222222")
lblrole.place(x=100, y=390)
roleEntry = Entry(root, bd=4, font=("Ubuntu", 14))
roleEntry.insert(0,"etudiant")
roleEntry.config(state=DISABLED)
roleEntry.place(x=100, y=420, width=250)

btnEnregistrer = Button(root, text="Enregistrer", font=("Montserrat", 16), bg="#579BB1", fg="#FFF", command=enregistrer)
btnEnregistrer.place(x=100, y=480, width=150)

mainloop()
from app import *



#fonction de connexion 
def connexion():
    import psycopg2
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
            call(['python', 'professeur.py'])

        elif role =="etudiant":
            messagebox.showinfo("", "Bienvenue")
            matriculeEntry.delete("0", "end")
            entryMdp.delete("0", "end")
            root.destroy()
            #call(['python', 'etudiant.py'])
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

mainloop()
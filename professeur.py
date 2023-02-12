from app import *

#focntions pour les bouttons

def ajouter():
    call(['python', 'ajoutEtudiant.py'])

def modifier():
    pass

def supprimer():
    pass

def historique():
    pass


root = Tk()
root.title("Gestionnaire d'absences")
root.geometry("1366x768+0+0")
root.config(background="#434242")

#titre
lbltitre = Label(root, borderwidth=3, relief=SUNKEN, text="Gestionnaire d'absences", font=("Montserrat-bold",30),bg="#222222", fg="#FFF")
lbltitre.pack(fill=X )

#table de données
table = ttk.Treeview(root)
#colonnes de la table
table['columns'] = ("matricule", "nom", "prenom", "nombreAbsence")
#dimension des colonnes
table.column("#0", width=10, minwidth=10)
table.column("matricule", width=50, minwidth=25)
table.column("nom", width=100, minwidth=25)
table.column("prenom", width=100, minwidth=25)
table.column("nombreAbsence", width=20, minwidth=25)

#titre des colonnes 
table.heading("#0",anchor=W, text="ID")
table.heading("matricule", anchor=W, text="Matricule")
table.heading("nom", anchor=W, text="Nom")
table.heading("prenom", anchor=W, text="Prénom")
table.heading("nombreAbsence", anchor=W, text="Nomde d'absences")
table.place(x=26, y=100, width=1000, height=568)

#recuperer les données dans la base et les afficher dans table
curr = conn.cursor()
curr.execute("SELECT matricule, nom, prenom, nombre_absence from utilisateur where role='etudiant'")
res = curr.fetchall()

for row in res:
    table.insert('', END, value=row)

curr.close()
conn.close()

#button
btnAjouter = Button(root, text="Ajouter", font=("Montserrat", 15), fg="#FFF", bg="#54B435", command=ajouter)
btnAjouter.place(x=1050, y=100)
btnAjouter = Button(root, text="Modifier", font=("Montserrat", 15), fg="#FFF", bg="#31C6D4", command=modifier)
btnAjouter.place(x=1050, y=200)
btnAjouter = Button(root, text="Supprimer", font=("Montserrat", 15), fg="#FFF", bg="#FF1E1E", command=supprimer)
btnAjouter.place(x=1050, y=300)
btnAjouter = Button(root, text="Voir l'historique", font=("Montserrat", 15), fg="#FFF", bg="#FFDE00", command=historique)
btnAjouter.place(x=1050, y=400)


mainloop()
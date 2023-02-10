import tkinter as tk
from tkinter import messagebox
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="students",
    user="herbilot",
    password="123db"
)

nom_utilisateur_entry = None
password_entry = None

def verify_login():
    global nom_utilisateur_entry
    global password_entry

    nom_utilisateur = nom_utilisateur_entry.get()
    password = password_entry.get()

    cursor = conn.cursor()
    query = "SELECT role FROM utilisateur WHERE nom_utilisateur=%s AND mot_de_passe=%s"
    cursor.execute(query, (nom_utilisateur, password))
    result = cursor.fetchone()

    if result:
        role = result[0]
        if role == "étudiant":
            show_student_page()
        else:
            show_professor_page()
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe est incorrect")

def show_student_page():
    global nom_utilisateur_entry

    student_page = tk.Toplevel(root)
    student_page.title("Page Étudiant")
    student_absence_label = tk.Label(student_page, text="Vos Absences:")
    student_absence_label.pack()

    cursor = conn.cursor()
    query = "SELECT * FROM absences WHERE id_etudiant=%s"
    cursor.execute(query, (nom_utilisateur_entry.get()))
    absences = cursor.fetchall()

    for absence in absences:
        absence_label = tk.Label(student_page, text=absence)
        absence_label.pack()

def show_professor_page():
    professor_page = tk.Toplevel(root)
    professor_page.title("Page Professeur")
    professor_absence_label = tk.Label(professor_page, text="Toutes les Absences:")


root = tk.Tk()
root.title("Gestion des Absences")
root.geometry("500x420")

username_label = tk.Label(root, text="Nom d'utilisateur:")
username_label.pack()

nom_utilisateur_entry = tk.Entry(root)
nom_utilisateur_entry.pack()

password_label = tk.Label(root, text="Mot de passe:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Connexion", command=verify_login)
login_button.pack()

root.mainloop()

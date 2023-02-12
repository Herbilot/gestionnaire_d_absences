from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox
from subprocess import call
from datetime import datetime
import psycopg2


#here are my database connection I was obliged to delete the lines as I did not use a .env file
conn = psycopg2.connect(
    host="localhost",
    database="gestion_absence",
    user="herbilot",
    password="123db"
)



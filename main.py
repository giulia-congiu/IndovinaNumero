import flet as ft
from controller import Controller
from view import View

def main(page: ft.Page):
    v = View(page) #crea un oggetto di tipo view
    c = Controller(v) #creo controller
    v.setController(c) #faccio parlare view e controller
    v.caricaInterfaccia() #qui dentro scriverò i metodi della mia interfaccia grafica

ft.app(target=main)
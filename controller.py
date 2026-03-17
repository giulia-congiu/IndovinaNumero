from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    # METODI CHIAMATI DAI PULSANTI
    def reset(self):
        self._model.reset() #resetto lo stato del gioco lato modello
        self._view._txtT.value= self._model.T #INTERFACCIA TRA VIEW E MODELLO:
        #chiedo al modello il suo valore di tentativi rimanenti e lo vado a scrivere nella view
        self._view._lvOut.controls.clear() #per svuotare il listview
        self._view._lvOut.controls.append(
            ft.Text("Inizia il gioco! Indovina a quale numero sto pensando")
        )

    def play(self):
        pass

    def getNmax(self):
        return self._model.Nmax #accedo a Nmax tramite la @property perchè aveva il "_" davanti

    def getTmax(self):
        return self._model.Tmax


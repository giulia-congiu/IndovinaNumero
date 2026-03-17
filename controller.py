from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    # METODI CHIAMATI DAI PULSANTI
    def reset(self, e):
        # e= evento che ha generato la pressione del pulsante
        #TUTTI I METODI DEL CONTROLLER ASSOCIATI A UN PUSLANTE HANNO e COME PARAMETRO
        self._model.reset() #resetto lo stato del gioco lato modello
        self._view._txtT.value= self._model.T #INTERFACCIA TRA VIEW E MODELLO:
        #chiedo al modello il suo valore di tentativi rimanenti e lo vado a scrivere nella view
        self._view._lvOut.controls.clear() #per svuotare il listview
        self._view._lvOut.controls.append(ft.Text("Inizia il gioco! Indovina a quale numero sto pensando"))
        self._view.update() #dice al modello di aggiornare quello che si sta visualizzando

    def play(self, e):
        """legge il tentativo del giocatore, lo passa al modello,
        rende il valore return del metodo play del modello e aggiorna l'interfaccia grafica"""
        tentativoStr = self._view._txtInTentativo.value #è una stringa
        try:
            tentativo = int(tentativoStr) #prendo l'input e provo a convertirlo in intero
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore, devi inserire un valore numerico"))
            self._view.update()  #ricorda di aggiornare l'interfaccia
            return

        #se supero il try vuol dire che è tutto ok e posso giocare
        res = self._model.play(tentativo) #chiedo al modello come giocare e prendo l'uscita del metodo

        if res == 0:
            """Ho vinto"""
            self._view._lvOut.controls.append(
                ft.Text(f"Bravo hai vinto :) ! Il valore corretto era: {tentativo}",
                                              color="green"))
            self._view.update()
            return #ho vinto e posso uscire dal modello

        elif res == 2:
            """Non ho più vite"""
            self._view._lvOut.controls.append(ft.Text(f"Hai perso :( ! Il valore corretto era {self._model.segreto}"))
            self._view.update()
            return

        elif res == -1:
            """Allora il segreto < tentativo"""
            self._view._lvOut.controls.append(ft.Text(f"Ritenta! Il segreto è più piccolo di {tentativo}"))
            self._view.update()
            return

        else:
            """Alora segreto > tentativo"""
            self._view._lvOut.controls.append(ft.Text(f"Ritenta! Il segreto è più grande di {tentativo}"))
            self._view.update()
            return


    def getNmax(self):
        return self._model.Nmax #accedo a Nmax tramite la @property perchè aveva il "_" davanti

    def getTmax(self):
        return self._model.Tmax


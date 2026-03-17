import random

class Model(object):
    def __init__(self):
        self._Nmax= 100 #devo indovinare un numero da 0 a 100
        self._Tmax= 6 #numero di tentativi massimi
        self._T = self._Tmax #numero di tentativi rimanenti
        self._segreto = None #numero randomico da indovinare che setto quando inizia il gioco

    def reset(self):
        """Questo metodo resetta lo stato del gioco. Imposta il numero segreto a un valore random
        e ripristina i tentativi rimanenti"""
        self._segreto = random.randint(0,self._Nmax)
        self._T = self._Tmax #riinizinializzo il numero di vite che ho
        print(self._segreto)

    def play(self, tentativo):
        """Riceve come argomento un valore intero che sarà il
        tentativo del giocatore e lo confronta con il segreto
        :return
        -1: segreto + piccolo del numero immesso
        0 numero azzeccato: vittoria
        1 segreto + grande
        2 ho sbagliato e non ho più vite
        """
        self._T-= 1 #tolgo 1 dal num di tentativi che mi restano
        if tentativo == self._segreto:
            """ho vinto"""
            return 0
        #se devo continuare a giocare controllo se ho ancora vite
        if self._T == 0:
            """non ho più vite"""
            return 2
        if tentativo > self._segreto:
            """tentativo + grande del segreto"""
            return -1
        else:
            return 1

    @property
    def Nmax(self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(40))
    print(m.play(60))


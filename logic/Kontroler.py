#!/usr/bin/env python3

from threading import Thread
from Model import Model
from Zdarzenie import ZdarzenieKoniec, ZdarzenieOblicz
from Strategia import StrategiaKoniec, StrategiaOblicz

class Kontroler(Thread):
    def __init__(self, kolejka_zdarzen, kolejka_makiet):
        Thread.__init__(self)
        self._kolejka_zdarzen = kolejka_zdarzen
        self.kolejka_makiet = kolejka_makiet
        self._model = Model()
        self._stworz_mape_dzialania()

    def _stworz_mape_dzialania(self):
        self._zdarzenie2strategia = {
            type( ZdarzenieKoniec() ) : StrategiaKoniec(self._model),
            type( ZdarzenieOblicz(None, None) ) : StrategiaOblicz(self._model),
        }

    def run(self):
        while True:
            zdarzenie = self._kolejka_zdarzen.get()
            strategia = self._zdarzenie2strategia[type(zdarzenie)]
            try:
                strategia.update(zdarzenie)
            except (Exception) as exc:
                print(exc)
                continue
            if self._model.koniec == True:
                return
            makieta = self._model.pobierz_makiete()
            print "utworzono makiete {0}".format(makieta.dane)
            self.kolejka_makiet.put(makieta)


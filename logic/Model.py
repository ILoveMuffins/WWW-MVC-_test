#!/usr/bin/env python3.4

from Makieta import Makieta

class Model(object):
    def __init__(self):
        self._wynik = None
        self.koniec = False

    def pobierz_makiete(self):
        makieta = Makieta(self._wynik)
        return makieta

    def oblicz(self, username, password):
        self._wynik = u"wynik obliczen {0}srodek{1}".format(username, password)


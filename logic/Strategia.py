#!/usr/bin/env python3.4

from abc import abstractmethod, ABCMeta

class Strategia:
    __metaclass__ = ABCMeta

    def __init__(self, model):
        self._model = model

    @abstractmethod
    def update(self, zdarzenie):
        pass

class StrategiaOblicz(Strategia):
    def update(self, zdarzenie):
        self._model.oblicz(zdarzenie.username, zdarzenie.password)

class StrategiaKoniec(Strategia):
    def update(self, zdarzenie):
        self._model.koniec = True


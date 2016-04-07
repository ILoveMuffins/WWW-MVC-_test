#!/usr/bin/env python3.4

from abc import ABCMeta

class Zdarzenie:
    __metaclass__ = ABCMeta

class ZdarzenieOblicz(Zdarzenie):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ZdarzenieKoniec(Zdarzenie):
    pass


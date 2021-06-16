# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:02:16 2021

@author: alvar
"""
class State:
    def __init__(self, *atomos):
        self.atomos = {}
        for atomo in atomos:
            for key, value in atomo.items():
                if key in self.atomos:
                    self.atomos[key] = self.atomos[key].union(value)
                else:
                    self.atomos[key] = value

    def __str__(self):
        return '\n'.join('{}({})'.format(key, ', '.join('{}'.format(arg)
                                                        for arg in valor))
                         for key, valores in self.atomos.items()
                         for valor in valores)

    def __eq__(self, otro):
        return self.atomos == otro.atomos

    def satisface_positivas(self, condiciones):
        return all(key in self.atomos.keys() and
                   value in self.atomos[key]
                   for key in condiciones.keys()
                   for value in condiciones[key])

    def satisface_negativas(self, condiciones):
        return all(key not in self.atomos.keys() or
                   value not in self.atomos[key]
                   for key in condiciones.keys()
                   for value in condiciones[key])
        
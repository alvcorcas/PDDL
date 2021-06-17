# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:47:05 2021

@author: alvar
"""

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def __repr__(self):
        return '\nName: ' + self.name + '\nPreconditions: ' + str(self.preconditions) + '\nEffects: ' + str(self.effects) + '\n'
        

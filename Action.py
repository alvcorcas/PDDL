# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:47:05 2021

@author: alvar
"""

class Action:
    def __init__(self, action, preconditions,effects):
        self.action = action
        self.preconditions = preconditions
        self.effects = effects

    def __repr__(self):
        return self.action
        

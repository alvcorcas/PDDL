# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:02:16 2021

@author: alvar
"""
class State:
    def __init__(self, literals):
        self.literals = literals

    def __str__(self):
        return self.literals

    def __eq__(self, other):
        return self.literals == other.literals

    def satisfy(self, conditions):
        for condition in conditions:
            if not(condition in self.literals):
                return False
        return True

'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
'''

class OutOfMovesError(Exception):
    
    def __init__(self, args="OutOfMovesError"):
        self.message = args

class IncorrectAttackerError(Exception):
    
    def __init__(self, args="IncorrectAttackerError"):
        self.message = args

class MaxHandSize(Exception):
    
    def __init__(self, args="MaxHandsize"):
        self.message = args
        
class CardNotInHand(Exception):
    
    def __init__(self, args="CardNotInHand"):
        self.message = args
        
class MaxVisibleHandSize(Exception):
    
    def __init__(self, args="MaxVisibleHandSize"):
        self.message = args
        

from flask import json


class AFD:
    def __init__(self, estados, alfabeto, estado_inicial, estados_finales, transiciones):
        self.data = {}
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales
        self.transiciones = transiciones
        
    def readJson(self, file_path):
        with open(file_path, 'r') as file:
            self.maquinas = json.load(file)["maquinas"]
            
    def loadNewAFN(self, number, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            maquina = data["maquinas"][number]
            self.estados = maquina['Q']
            self.alfabeto = maquina['M']
            self.estado_inicial = maquina['I']
            self.estados_finales = maquina['F']
            self.transiciones = maquina['T']
    
            
    def transition(self, estado, simbolo):
        return [t[2] for t in self.transiciones if t[0] == estado and t[1] == simbolo]
    
    def final_state(self, estado, cadena):
        for simbolo in cadena:
            estado = self.transition(estado, simbolo)
            if not estado:
                return False
            estado = estado[0]
        return estado

    def is_accepted(self, estado, cadena):
        estado_final = self.final_state(estado, cadena)
        return estado_final in self.estados_finales
    
    def derivation(self, estado, cadena):
        derivacion = []
        for simbolo in cadena:
            estado = self.transition(estado, simbolo)
            if not estado:
                return derivacion
            estado = estado[0]
            derivacion.append(estado)
        return derivacion

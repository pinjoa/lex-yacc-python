# -----------------------------------------------------------
# @file symbol_table.py
# @author Alberto Simões, solução inicial produzida em contexto de aula
# @author João Pinto (pinjoa@gmail.com)
# 
# @brief implementação de um dicionário de "arrays", uma vantagem desta abordagem permite a utilização de variáveis
# com o mesmo nome, com esta implementação é possivel criar funções recursivas...
# (desafio de PL-Processamento de linguagens)
# 
# @version 0.1
# @date 2022-01-07
# 
# @copyright Copyright (c) 2022, João Carlos Pinto
# -----------------------------------------------------------


class SymbolTable:
    # inicializar a classe
    def __init__(self):
        # dicionario de arrays (para cada "var", uma lista de valores)
        self._data = {}   

    # reset "value" para uma determinada "key"
    def re_set(self, key, value):
        if key in self._data:
            self._data[key].append(value)
        else:
            # utilizar o "setter" implementado mais abaixo...
            self[key] = value   

    # implementar comportamento "getter"
    # y = table["x"]
    def __getitem__(self, item):
        if item in self._data:
            return self._data[item][-1]
        else:
            raise Exception(f"Out of bounds: {item} not found")

    # implementar comportamento "setter"
    # table["x"] = 10
    def __setitem__(self, key, value):
        if key in self._data:
            # array existe, atualizar último layer
            self._data[key][-1] = value    
        else:
            # se o array não existe, adicionar
            self._data[key] = [value]      

    # implementar comportamento "del"
    # del table["x"]
    def __delitem__(self, key):
        # chave existe?
        if key in self._data:               
            if len(self._data[key]) == 1:
                # só tem um valor?
                # apaga completamente o elemento "key"
                del self._data[key]         
            else:                           
                # tem mais que um valor, remove ultimo inserido na stack
                self._data[key].pop()       
        else:
            raise Exception(f"Out of bounds: {key} not found")

    # implementar comportamento "in"
    # x in table
    def __contains__(self, item):
        return item in self._data


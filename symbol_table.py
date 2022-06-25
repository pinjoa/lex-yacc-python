# -----------------------------------------------------------
# @file symbol_table.py
# @author Alberto Simões, solução inicial produzida em contexto de aula
# @author João Pinto (pinjoa@gmail.com)
# 
# @brief implementação de um dicionário de "arrays"
# 
# @version 0.1
# @date 2022-01-07
# 
# @copyright Copyright (c) 2022, João Carlos Pinto
# -----------------------------------------------------------


class SymbolTable:
    def __init__(self):
        # dicionario de arrays (para cada var, uma lista de valores)
        self._data = {}   

    def re_set(self, key, value):
        if key in self._data:
            self._data[key].append(value)
        else:
            # uses the setitem below
            self[key] = value   

    # y = table["x"]
    def __getitem__(self, item):
        if item in self._data:
            return self._data[item][-1]
        else:
            raise Exception(f"Out of bounds: {item} not found")

    # table["x"] = 10
    def __setitem__(self, key, value):
        if key in self._data:
            # array existe, atualizar último layer
            self._data[key][-1] = value    
        else:
            # array não existe, adicionar
            self._data[key] = [value]      

    # del table["x"]
    def __delitem__(self, key):
        # chave existe?
        if key in self._data:               
            # só tem um valor
            if len(self._data[key]) == 1:   
                # apaga completamente
                del self._data[key]         
            else:                           
                # tem mais que um valor, remove ultimo da stack
                self._data[key].pop()       
        else:
            raise Exception(f"Out of bounds: {key} not found")

    # x in table
    def __contains__(self, item):
        return item in self._data

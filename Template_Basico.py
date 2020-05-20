# -*- coding: utf-8 -*-
"""
Modelo simples de Pesquisa Operacional
"""
# Importacao das bibliotecas
from pulp import *

# Criando o modelo
model = LpProblem("Modelo_basico", LpMaximize)

# Variaveis de Decisao
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# Declarando a Funcao Objetivo
model += 5*x + 4*y

# Declarando as restricoes 
model += 6*x + 4*y <= 24
model += x + 2*y <= 6

# Apresentando o Modelo
status = model.solve()
print(model)

# Apresentando as solucoes
print(value(x))
print(value(y))
print(value(model.objective))

# Verificando se a solucao eh Otima
print(LpStatus[status])
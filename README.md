# 55MQU

Problema do Múltiplo Caixieiro Viajante (multiple traveling salesman problem - mTSP)

No arquivo code\main.py é onde o projeto é executado.

Comando para execução das metaheuriísticas:

python3 main.py <Instância> <nome da metaheurística> <nome da metaheurística caso for usado busca local>

h1 - Heurística construtiva utilizando como método de seleção a menor soma das distâncias dos caixieiros. Utilizando método guloso.

h12 - Heurística construtiva utilizando como método de seleção a menor soma das distâncias dos caixieiros. Utilizando método alfa-guloso.

h2 - Heurística construtiva utilizando como método de seleção a menor sdistância para a próxima cidade. Utilizando método guloso.

h22 - Heurística construtiva utilizando como método de seleção a menor sdistância para a próxima cidade. Utilizando método alfa-guloso.

lsii - Busca local utilizando intra shift e inter shift.

lsia - Busca local utilizando intra shift.

lsie - Busca local utilizando inter shift.

grasp1 - GRASP utilizando a heurística h1 e a busca local intra shift.

grasp2 - GRASP utilizando a heurística h1 e a busca local inter shift.

grasp3 - GRASP utilizando a heurística h2 e a busca local intra shift.

grasp4 - GRASP utilizando a heurística h2 e a busca local inter shift.

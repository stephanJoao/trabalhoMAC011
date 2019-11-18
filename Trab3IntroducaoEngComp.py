''' 

Integrantes: Alexandre Vitor Silva Braga - 201965501B 

             Arthur Fernandes              

             Caio Cedrola Rocha - 201965503B 

             Gabriel Maciel Furlong -  

             João Stephan Silva Maurício - 201965505B  

             Marcelo Ian  


DESCRIÇÃO DO PROBLEMA: 

Deseja-se encontrar, dada determinada locadora de carros com sede em Juiz de Fora e em Belo Horizonte, 

a distribuição que melhor atenda à demanda de veículos em cada cidade, com base em registros históricos 

de aluguel e devolução de carros da empresa. Para tal, será utilizado o modelo da Cadeia de Markov 

para a resolução do problema proposto, a qual define que, dado qualquer evento passado e o estado presente, 

a probabilidade desse evento depende somente do estado presente, ou seja, independe de eventos passados. 


'''

P = [0.6, 0.4, 0.3, 0.7] #P representa uma matriz 2x2 

print("Probabilidade inicial:") 

print("P = [(", P[0], ",", P[1], "), ")

print("     (", P[2], ",", P[3], ")]")

''' 

O objetivo é encontrar um equilíbrio entre as probabilidades. 

Para isso, multiplica-se a matriz por ela mesma até que a matriz resultado não mude mais. 

P[índice] = P[B|A]: probabilidade do carro ser devolvido na cidade B dado que foi alugado na cidade A 

P[0] = P[JF|JF] 

P[1] = P[BH|JF] 

P[2] = P[JF|BH] 

P[3] = P[BH|BH] 

'''

 
dias = 14 


'''

Como o tempo é discreto, após uma certa quantidade de dias,

a saída será sempre a mesma para todo e qualquer caso na matriz de probabilidades,

pois essas aproximar-se-ão de um valor probabilístico fixo. 

'''


U = [0.6, 0.4, 0.3, 0.7] 
V = [0.0, 0.0, 0.0, 0.0]

for i  in range(dias): 

    V[0] = P[0] 

    V[1] = P[1] 

    V[2] = P[2] 

    V[3] = P[3] 

    P[0] = V[0]*U[0] + V[1]*U[2] 

    P[1] = V[0]*U[1] + V[1]*U[3] 

    P[2] = V[2]*U[0] + V[3]*U[2] 

    P[3] = V[2]*U[1] + V[3]*U[3] 

print("Probabilidade final:")

print("P = [(", P[0], ",", P[1], "), ")

print("     (", P[2], ",", P[3], ")]")
 

'''

Atualização da Matriz para a 14ª potência,

os valores matriciais probabilísticos aproximam-se de  [0.43, 0.57, 0.43, 0.57] 

'''

print("Eventos (estágio inicial): ")

print("A = [7000, 0]\nB = [5000, 2000]\nC = [2000, 5000]\nD = [0, 7000]")

print("Eventos (estágio final): ")


#Situação 1 - 7000 em JF e 0 em BH 

A = list() 

S = [7000, 0] 

A.append(S[0]*P[0]+S[1]*P[2]) 

A.append(S[0]*P[1]+S[1]*P[3]) 

print("A =", A) 
 

#Situação 2 - 5000 em JF e 2000 em BH 

B = list() 

S = [5000, 2000] 

B.append(S[0]*P[0]+S[1]*P[2]) 

B.append(S[0]*P[1]+S[1]*P[3]) 

print("B =", B) 
 

#Situação 3 - 2000 em JF e 5000 em BH 

C = list() 

S = [2000, 5000] 

C.append(S[0]*P[0]+S[1]*P[2]) 

C.append(S[0]*P[1]+S[1]*P[3]) 

print("C =", C) 
 

#Situação 4 - 0 em JF e 7000 em BH 

D = list() 

S = [0, 7000] 

D.append(S[0]*P[0]+S[1]*P[2]) 

D.append(S[0]*P[1]+S[1]*P[3]) 

print("D =", D) 
 

''' 

Como observado na execução do código, o ponto de equilíbrio encontrado é,

respectivamente, a presença de 3000 carros em JF e 4000 carros em BH, 

números nos quais as probabilidades atreladas à matriz tenderão a resultar.

Por conseguinte, essa se mostra a melhor distribuição de carros entre as cidades. 

'''


print("Verifica-se que a soma das probabilidades em cada caso é constante, como o esperado:") 

print("Soma(A) =", A[0]+A[1]) 

print("Soma(B) =", B[0]+B[1]) 

print("Soma(C) =", C[0]+C[1]) 

print("Soma(D) =", D[0]+D[1])

 
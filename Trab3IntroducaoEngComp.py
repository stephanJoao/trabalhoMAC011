''' 

Integrantes: Alexandre Vitor Silva Braga - 201965501B 

             Arthur Fernandes              

             Caio Cedrola Rocha - 201965503B 

             Gabriel Maciel Furlong -  

             João Stephan Silva Maurício - 201965505B  

             Marcelo Ian  

'''
import matplotlib.pyplot as plt

x = [0]

yA1 = [7000]
yA2 = [0]

yB1 = [5000]
yB2 = [2000]

yC1 = [2000]
yC2 = [5000]

yD1 = [0]
yD2 = [7000]

P = [0.6, 0.4, 0.3, 0.7] #P representa uma matriz 2x2 

print("Probabilidade inicial:") 

print("P = [(", P[0], ",", P[1], "), ")

print("     (", P[2], ",", P[3], ")]")

print("\nEventos iniciais: ")

print("A = [7000, 0]\nB = [5000, 2000]\nC = [2000, 5000]\nD = [0, 7000]")

dias = 14 

U = [0.6, 0.4, 0.3, 0.7] 
V = [0.0, 0.0, 0.0, 0.0]

for i  in range(dias): 
    
    x.append(i + 1)
        
    V[0] = P[0] 

    V[1] = P[1] 

    V[2] = P[2] 

    V[3] = P[3] 

    P[0] = V[0]*U[0] + V[1]*U[2] 

    P[1] = V[0]*U[1] + V[1]*U[3] 

    P[2] = V[2]*U[0] + V[3]*U[2] 

    P[3] = V[2]*U[1] + V[3]*U[3] 

    print("\n\nProbabilidade no dia",i + 1,":")
    
    print("P = [(", P[0], ",", P[1], "), ")
    
    print("     (", P[2], ",", P[3], ")]\n")

    #Situação 1 - 7000 em JF e 0 em BH 
    
    S = [7000, 0] 
    
    A = [S[0]*P[0]+S[1]*P[2], S[0]*P[1]+S[1]*P[3]] 
    
    yA1.append(A[0])
    
    yA2.append(A[1])
    
    print("Carros no dia", i + 1,": ")
    
    print("A =", A) 
     
    #Situação 2 - 5000 em JF e 2000 em BH 
    
    S = [5000, 2000] 
    
    B = [S[0]*P[0]+S[1]*P[2], S[0]*P[1]+S[1]*P[3]] 
    
    yB1.append(B[0])
    
    yB2.append(B[1])
    
    print("B =", B) 
    
    #Situação 3 - 2000 em JF e 5000 em BH 
    
    S = [2000, 5000] 
    
    C = [S[0]*P[0]+S[1]*P[2], S[0]*P[1]+S[1]*P[3]] 
    
    yC1.append(C[0])
    
    yC2.append(C[1])
    
    print("C =", C) 
    
    #Situação 4 - 0 em JF e 7000 em BH 
    
    S = [0, 7000] 
    
    D = [S[0]*P[0]+S[1]*P[2], S[0]*P[1]+S[1]*P[3]] 
    
    yD1.append(D[0])
    
    yD2.append(D[1])
    
    print("D =", D) 



print("\n\n\nVerifica-se que a soma das probabilidades em cada caso é constante, como o esperado:") 

print("Soma(A) =", A[0]+A[1]) 

print("Soma(B) =", B[0]+B[1]) 

print("Soma(C) =", C[0]+C[1]) 

print("Soma(D) =", D[0]+D[1])


plt.plot(x, yA1, '-', color = 'red', label = 'JF situação 1')
plt.plot(x, yA2, '--',  color = 'darkred', label = 'BH situação 1')
plt.plot(x, yB1, '-', color = 'limegreen', label = 'JF situação 2')
plt.plot(x, yB2, '--', color = 'darkgreen', label = 'BH situação 2')
plt.plot(x, yC1, '-', color = 'royalblue', label = 'JF situação 3')
plt.plot(x, yC2, '--', color = 'darkblue', label = 'BH situação 3')
plt.plot(x, yD1, '-', color = 'gold', label = 'JF situação 4')
plt.plot(x, yD2, '--', color = 'darkgoldenrod', label = 'BH situação 4')

plt.legend()
plt.xlabel('Número de dias')
plt.ylabel('Número de carros')
plt.grid()
plt.savefig('grafico.pdf')
plt.show()

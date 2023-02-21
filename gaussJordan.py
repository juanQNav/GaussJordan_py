#Autor: QUISTIAN NAVARRO JUAN LUIS
# 19/feb/2023

#imprimimos la matriz
def printArray(array, ren, col):
    for i in range(ren):
        for j in range(col):
            if(j == col -1):
                print('|', end= ' ')
            print(array[i][j],end= ' ')
        print('\n')
#asignacion de memoria
def asignaMem(array,ren, col):
    for i in range(ren):
        array.append([])
        for j in range(col):
            array[i].append([])
#llenamos la matriz con los datos del archivo
def llenaArray(lines, array, ren, col): 
    for i in range(ren):
        aux = lines[i].split(',')
        for j in range(col):
            if aux[j] != aux[j]+'\n':
                array[i][j] = float(aux[j])
#algoritmo de Gauss Jordan
def gaussJordan(matriz, ren, col, matrizAux):
    for i in range(0, ren): #fila que no se modifica
        for j in range(0, ren):#fila con la que se efectua la resta
            cont = 0
            if i!= j:
                for k in range(0, col):
                    matrizAux[cont][k] = matriz[i][k]*matriz[j][i]
                cont+=1
                for k in range(0, col):
                    matrizAux[cont][k] = matriz[j][k]*matriz[i][i]
                for k in range(0, col):
                    matriz[j][k] = matrizAux[0][k]-matrizAux[1][k]
        print('*******************Paso ', i+1)
        printArray(matriz,ren,col)
    print('***************** MATRIZ RESULTANTE **********************')
    for i in range(0, ren):
        div = matriz[i][i]
        for j in range(0, col):
            matriz[i][j] = matriz[i][j] / div

#Cuerpo principal del programa
archivo_texto = open('matriz.txt','r')
firstLine = archivo_texto.readline()

ren = int(firstLine[0])
col = int(firstLine[2])
print('Matris de ',ren,' * ',col)

matriz = []
asignaMem(matriz, ren,col)

lines = archivo_texto.readlines() 
archivo_texto.close 

llenaArray(lines, matriz,ren,col)
print('***************** MATRIZ AUMENTADA **********************')
printArray(matriz, ren, col)


matrizAux = []
asignaMem(matrizAux, 2, col)

gaussJordan(matriz, ren, col, matrizAux)
printArray(matriz,ren,col)
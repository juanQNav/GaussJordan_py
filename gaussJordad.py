#imprimimos la matriz
def printArray(array, ren, col):
    for i in range(ren):
        for j in range(col):
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
#Cuerpo principal del programa
archivo_texto = open('matriz.txt','r')
firstLine = archivo_texto.readline()

ren = int(firstLine[0])
print(ren)
col = int(firstLine[2])
print(col)

matriz = []
asignaMem(matriz, ren,col)

lines = archivo_texto.readlines() 
archivo_texto.close 

llenaArray(lines, matriz,ren,col)

printArray(matriz, ren, col)

#algoritmo de gauss jordan
matrizAux = []
asignaMem(matrizAux, ren, col)

for i in range(0, ren):
    for j in range(0, 1):
            mult = matriz[i][j]
            for k in range(0,col):
                if i != j:
                    matrizAux[i][k] = matriz[j][k]* mult
                elif i < col:
                     matrizAux[i+1][k] = matriz[j+1][k]* mult
                else:
                     matrizAux[i-(i-1)][k] = matriz[j][k]* mult

print('*************************************************************')

printArray(matrizAux, ren, col)
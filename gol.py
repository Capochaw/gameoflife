from time import sleep

matrix = [
    [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
    [1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
    [1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
    [1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

def evalmatrix(matrix):
    retmatrix = matrix
    for i in range(len(matrix)):
        for q in range(len(matrix[i])):
            neighbours = 0
            if (i-1 >= 0):
                neighbours += matrix[i-1][q]
            if (q-1 >= 0):
                neighbours += matrix[i][q-1]
            if (i+1 < len(matrix)):
                neighbours += matrix[i+1][q]
            if (q+1 < len(matrix[i])):
                neighbours += matrix[i][q+1]
            if ((i+1 < len(matrix)) and (q+1 < len(matrix[i]))):
                neighbours += matrix[i+1][q+1]
            if ((i+1 < len(matrix)) and (q-1 >= 0)):
                neighbours += matrix[i+1][q-1]
            if ((i-1 >= 0) and (q+1 < len(matrix[i]))):
                neighbours += matrix[i-1][q+1]
            if ((i-1 >= 0) and (q-1 >= 0)):
                neighbours += matrix[i-1][q-1]
            if((matrix[i][q] == 1) and (neighbours <2)):
                retmatrix[i][q] = 0
            if((matrix[i][q] == 1) and (neighbours in [2,3])):
                retmatrix[i][q] = 1
            if((matrix[i][q] == 1) and (neighbours > 3)):
                retmatrix[i][q] = 0
            if((matrix[i][q] == 0) and (neighbours == 3)):
                retmatrix[i][q] = 1
    return retmatrix

def printmatrix(matrix):
    for i in range(len(matrix)):
        for q in range(len(matrix[i])):
            if(matrix[i][q] == 1):
                print("█",end='')
            else:
                print(" ",end='')
        print("")
    print("-0-")



def main():
    newmatrix = matrix
    while(True):
        printmatrix(newmatrix)
        sleep(0.4)
        newmatrix = evalmatrix(matrix)



if __name__ == "__main__":
    main()
